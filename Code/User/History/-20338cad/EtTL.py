# ---------------------------------------------------------------------

#
# Notes:
# an important resource is the h5py module that is used to read the
# h5 file. some useful documentation can be found here:
#  https://docs.h5py.org/en/stable/quick.html#quick
#
# The xml template is stored in the mentat development folder:
#     ...\source\marc\hdf\schema\Marc_2021.3.xml
#
# with the implementation of file locking, the library uses the status_
# flags field in the superblock to mark a file as in writing or SWMR
# writing mode when a file is opened. The library will clear this field
# when the file closes. However, a situation may occur where an open
# file is closed without going through the normal library file closing
# procedure, and this field will not be cleared as a result. An example
# would be if an application program crashed. This situation will
# prevent a user from opening the file. The h5clear tool will clear the
# status_flags field. To use, open a CMD shell in the following folder
# and type:
# c:\yourpath\mentat\python\win8664\bin\h5clear-shared.exe -s h5file.h5
#
# ---------------------------------------------------------------------
import numpy as np
import h5py
import math
import sys
import shutil
import pprint

def pad_string(s, length):
    return s.ljust(length)[:length].encode('utf-8')

def get_all_paths(hdf):
    all_paths = []


    def collect_all_paths(name, obj):
        all_paths.append(name)  # Aggiungi il percorso alla lista


    # Usa il metodo .visititems() per visitare ricorsivamente tutti gli oggetti
    hdf.visititems(collect_all_paths)
    print(all_paths)

def dataset_print(data1,elem=0):

    # esempio di un valore scalare 
    #      elem size=0 inc intpoint set layer subinc img
    # data1[0][0][0][1][0][0][0][0]

    intpoints = data1.shape[2]
    int1 = 0
    print("element intID ", elem , " value : ", data1[elem][0][int1][0][0][0][0])




def dataset_dump(data1):
    """
    """
    arr_str = np.array2string(data1, separator=', ', formatter={'float_kind': lambda x: "%.2f" % x})
    print("data shape ", data1.shape)

    # Semplifica e reshape
    simplified_array = np.squeeze(data1)
    #reshaped_array = simplified_array.reshape(2, 16)

    # Stampa con formattazione
    np.set_printoptions(precision=2, suppress=True)
    print("simple form ", simplified_array.shape)
    print(simplified_array)

def get_group_h5_scalar(file ,dataset_path ):
    """
    <dataset name="Element_Type" type="floating-point" ndims="8 { -1,1,-1,Nint,-1,-1,-1,-1}">
            <dim 0="Element List"/>
            <dim 1="Scalar Value" size="1"/>
            <dim 2="Increment ID"/>
            <dim 3="Int. Point ID" size="Nint" description="Nint is the number of integrations points for Element Type"/>
            <dim 4="Set ID"/>
            <dim 5="Layer ID"/>
            <dim 6="Sub-increment ID"/>
            <dim 7="Real-Imag Values"/>
    </dataset>
    
    
    """
    print(' ***** reading h5 file: ', file)


    with h5py.File(file, 'r') as hdf:

        all_paths = get_all_paths(hdf)

        #   Cerca i risultati
        

        if dataset_path in hdf:
            g1 = hdf.get(dataset_path)
            if str(type(hdf[dataset_path])) == "<class 'h5py._hl.group.Group'>":
                print("group ", dataset_path, " found.")
            #data1 = hdf[dataset_path][()]  # Leggi i dati nel dataset

            #dataset_print(data1)


            # all_data = np.array([data1, data2])
            # data5 = np.amax(all_data, axis=0)
            # print("Dati letti con successo:")
            # print(data4)
        else:
            print(f"dataset {dataset_path} does not exist.")
        hdf.close()

    return g1

def get_precision(hdf):
    
    g1 = hdf.get('Marc')

    precision = g1.attrs.get('precision')
    # it could be single or double precision
    if precision[0] == 0:
        prec = 'Single'
    elif precision[0] == 1:
        prec = 'Double'
    # inform user
    print(' : H5 File precision:\t', prec)
    # set data types based on precision for
    # later use
    if precision[0] == 0:
        dtype_int = 'i4'
        dtype_float = 'float32'
    elif precision[0] == 1:
        dtype_int = 'i8'
        dtype_float = 'float64'

    return dtype_int, dtype_float

    

def add_res(file2,g1):

    print(' ***** reading h5 file: ', file2)


    with h5py.File(file2, 'a') as hdf:

        all_paths = get_all_paths(hdf)

        dtype_int, dtype_float = get_precision(hdf)

        g_elem=hdf.get('Marc/Results/Element')
        elem_post_summary = g_elem["Element Post Summary"]
        """
        <dim 1="Value" size="3">
          <column 0 description="Element Postcode" description="Appendix Table 3"/>
          <column 1 description="Layer"/>
          <column 2 description="1:Scalar 2:Vector 3:Tensor"/>
        </dim 1>
        """

        elem_post_code = len(elem_post_summary[0])

        check_res=False
        var_cercata = -3
        for i in range(elem_post_code) :
            tipo_res = elem_post_summary[i][0][0]

            if tipo_res == var_cercata:
                check_res = True
                print("risultato trovato ", elem_post_code[i][0][0])

        if check_res == False:
            user_postcode = np.zeros((1,3,1))
            user_postcode[0][0][0] = -3  # ID variabile output
            user_postcode[0][2] = 1   # scalare
            #print(user_postcode)
            
            elem_post_summary = np.append(elem_post_summary, user_postcode, axis=0)

            del hdf['Marc/Results/Element/Element Post Summary']
            dset = hdf.create_dataset('/Marc/Results/Element/Element Post Summary', dtype=dtype_int, data=elem_post_summary)

            print("aggiunta risultato ", elem_post_summary.shape)

    gcrea = hdf.create_group('Marc/Results/Element/Scalar/Resultant', track_order=True)


if __name__ == '__main__':

    file = 'm3_job1.h5'
    path_scalare = 'Marc/Results/Element/Scalar/'
    var1 = 'PRIMO_RES'
    g1_path1 = path_scalare + var1
    g1 = get_group_h5_scalar(file, g1_path1)
        
    #dataset_path2 = path_scalare + var1
    #g2 = read_h5_scalar(file,dataset_path2)
    file2 = file.split(".")[0] + "_mod.h5"
    shutil.copyfile(file, file2)

    add_res(file2,g1)

    print('\n HDF5 Results File Processing End')
print(' ----------------------------------\n')
