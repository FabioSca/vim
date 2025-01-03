# coding: utf-8
#

#
#
#

import apex
from apex.construct import Point3D, Point2D

import math
from operator import itemgetter
import sys

def createSPCForTopNode(name, topNode, coordSys):
    _target = apex.entityCollection()
    _target.append(topNode)

    _constraintProp = apex.attribute.createDisplacementConstraintProperties(
        constrainTranslationX=False,
        constrainTranslationY=False,
        constrainTranslationZ=False,
        constrainRotationX=True,
        constrainRotationY=False,
        constrainRotationZ=False)

    _orientation = apex.construct.createOrientationByCoordinateSystem(coordSys)

    constraint = apex.environment.createDisplacementConstraint(
        name=name,
        constraintType=apex.attribute.ConstraintType.General,
        applicationMethod=apex.attribute.ApplicationMethod.Direct,
        target=_target,
        constraintProperties=_constraintProp,
        orientation=_orientation,
        description="Rutman Fastener Top Node for: " + name)
    return constraint


def crossProduct(v1, v2):
    a1 = v1.getX()
    a2 = v1.getY()
    a3 = v1.getZ()

    b1 = v2.getX()
    b2 = v2.getY()
    b3 = v2.getZ()

    s1 = a2 * b3 - a3 * b2
    s2 = a3 * b1 - a1 * b3
    s3 = a1 * b2 - a2 * b1

    v = apex.construct.Vector3D(x=s1, y=s2, z=s3)

    return v


def createCoord2(name, n1, n2):
    _target = apex.ILocationCollection()
    _target.append(n1.getCoordinates())
    _target.append(n2.getCoordinates())

    c1 = apex.geometry.createCurve(target=_target, behavior=apex.geometry.CurveBehavior.Spline)

    _orientation = apex.construct.createOrientation(alpha=c1.getAlpha(), beta=c1.getBeta(), gamma=c1.getGamma())

    coordSys = apex.construct.createCoordinateSystemByEulerMethod(
        name=name,
        description="",
        coordType=apex.construct.CoordinateSystemType.Cartesian,
        origin=n1,
        orientation=_orientation)

    curves = apex.entityCollection()
    curves.append(c1)

    apex.deleteEntities(target=curves)

    return coordSys


def createCbush(name, plateNode, fastenerNode, thick, Eplate, NUplate, Efast, coord):
    # the cbush will reference the fastener coord frame which has x along the fastener
    # shaft.  this means that the cbush needs to reference y and z.
    if RutForm == 1:
        Sy = Eplate * thick / (1.0 - NUplate ** 2)
        d = (1.0 - NUplate ** 2) / Eplate + 1.0 / Efast
        Ry = (thick ** 3) / 12. / d
    else:
        Sy = thick / (1.0 / Eplate + 1.0 / Efast)
        Ry = (thick ** 3) / 12.0 / (1.0 / Eplate + 1.0 / Efast)

    Sz = Sy
    Rz = Ry

    _endPoint1 = apex.construct.createLocationByEntity(entity=plateNode)
    _endPoint2 = apex.construct.createLocationByEntity(entity=fastenerNode)

    _orientation = apex.construct.createOrientationByCoordinateSystem(coord)

    bushProps = apex.attribute.createConnectorProperties(
        translationalStiffnessX=0.,
        translationalStiffnessY=Sy,
        translationalStiffnessZ=Sz,
        rotationalStiffnessX=0.,
        rotationalStiffnessY=Ry,
        rotationalStiffnessZ=Rz,
        linkMaterial=None)
    bushConnector = apex.attribute.createConnector(
        name=name + "_CBUSH",
        connectorType=apex.attribute.ConnectorType.Bushing,
        connectorProperties=bushProps,
        applicationMethod1=apex.attribute.ApplicationMethod.Direct,
        applicationMethod2=apex.attribute.ApplicationMethod.Direct,
        end1InterfacePoint=_endPoint1,
        end2InterfacePoint=_endPoint2,
        orientation=_orientation,
        description="")
    return bushConnector


def createRbar(name, aNode, bNode, _dependentDOF):
    #   THIS ACTUALLY CREATES AN RBE2
    _endPoint1 = apex.construct.createLocationByEntity(aNode)
    _endPoint2 = apex.construct.createLocationByEntity(bNode)
    rigidlinkrepproperties_2 = apex.attribute.createRigidLinkRepProperties()

    connector = apex.attribute.createConnectorDiscrete(
        name=name,
        connectorProperties=rigidlinkrepproperties_2,
        applicationMethod1=apex.attribute.ApplicationMethod.Direct,
        applicationMethod2=apex.attribute.ApplicationMethod.Direct,
        end1InterfacePoint=_endPoint1,
        end2InterfacePoint=_endPoint2,
        description="",  # defaults to " "
        end1IndependentDOF="123456",
        end1DependentDOF="",
        end2IndependentDOF="",
        end2DependentDOF=_dependentDOF,
    )
    return connector


def createFlexConnector(name, fastenerDia, fastenerMatl, n0, n1):
    _endPoint1 = apex.construct.createLocationByEntity(entity=n0)
    _endPoint2 = apex.construct.createLocationByEntity(entity=n1)

    flexConnectorProps = apex.attribute.createConnectorProperties(
        diameter=fastenerDia,
        linkMaterial=fastenerMatl)
    flexConnector = apex.attribute.createConnector(
        name=name + "_BAR",
        connectorType=apex.attribute.ConnectorType.FlexibleLink,
        connectorProperties=flexConnectorProps,
        applicationMethod1=apex.attribute.ApplicationMethod.Direct,
        applicationMethod2=apex.attribute.ApplicationMethod.Direct,
        end1InterfacePoint=_endPoint1,
        end2InterfacePoint=_endPoint2,
        description="")
    return flexConnector


def myDot(aVec, bVec):
    # THIS RETURNS COS(THETA)
    dot = aVec.getX() * bVec.getX()
    dot += aVec.getY() * bVec.getY()
    dot += aVec.getZ() * bVec.getZ()

    cosTheta = dot / aVec.getLength() / bVec.getLength()

    return cosTheta


def dotProduct(aVec, bVec):
    dot = aVec.getX() * bVec.getX()
    dot += aVec.getY() * bVec.getY()
    dot += aVec.getZ() * bVec.getZ()

    return dot


def createVector3D(p1, p2):
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    dz = p2.getZ() - p1.getZ()

    vec = apex.construct.Vector3D(dx, dy, dz)

    return vec


def makeUnitVector(vec):
    x = vec.getX() / vec.getLength()
    y = vec.getY() / vec.getLength()
    z = vec.getZ() / vec.getLength()

    v = apex.construct.Vector3D(x, y, z)

    return v


def scaleVector(scaleFactor, vec):
    vx = scaleFactor * vec.getX()
    vy = scaleFactor * vec.getY()
    vz = scaleFactor * vec.getZ()

    vv = apex.construct.Vector3D(vx, vy, vz)

    return vv


def addVectors(vec1, vec2):
    vx = vec1.getX() + vec2.getX()
    vy = vec1.getY() + vec2.getY()
    vz = vec1.getZ() + vec2.getZ()

    vv = apex.construct.Vector3D(vx, vy, vz)

    return vv


def getNormalAtNode(nn):
    elms = nn.getElements()
    # for the moment, i am just going to get the normal of the first element
    norm = elms[0].getNormal()

    return norm


def setPartForNewNode(node, meshNodes):
    myModel = apex.currentModel()
    for key in meshNodes:
        if node.getId() in meshNodes[key]["nodes"]:
            mb = meshNodes[key]["meshBody"]
            # newkeys = key.split("/")
            new_path = key.rsplit('/', 1)[0]
            new_path = new_path.split('/', 1)[1]
            # print(new_path)
            part = myModel.getPart(new_path)
            assy = part.getParent()        
            isModel = isinstance(assy , apex.Model)

            if isModel:
                partPath = "/" + part.getName()
            else:
                partPath = part.getPath()[part.getPath().find("/") + 1:] + "/" + part.getName()

            myModel.setCurrentPart(partPath)
            break
    return part


def addUserAttributes(obj, name):
    obj.addUserAttribute(userAttributeName="rfastTool", stringValue="auRFAST")
    obj.addUserAttribute(userAttributeName="rfastName", stringValue=name)


def getPointMeshBody(part):
    meshes = part.getMeshes()
    for mesh in meshes:
        if isinstance(mesh, apex.mesh.PointMesh):
            attributes = mesh.getUserAttributes(userAttributeNames=["rfastTool", "rfastName"])
            if attributes.len() == 0: continue
            return mesh
    return None


def getPreviouslyUsedNodes():
    myModel = apex.currentModel()
    connectors = apex.entityCollection()
    assys = myModel.getAssemblies()
    if len(assys) == 0:
        print("\nERROR: No assembly in the model")
        print("ERROR: This is a requirement component  !!!\n")
        return
    parts = myModel.getParts()

    for assy in assys:
        connectors.extend(apex.attribute.getBushings([{"path": assy.getPath()}]))
        connectors.extend(apex.attribute.getFlexibleLinks([{"path": assy.getPath()}]))
    for part in parts:
        connectors.extend(apex.attribute.getBushings([{"path": assy.getPath()}]))
        connectors.extend(apex.attribute.getFlexibleLinks([{"path": assy.getPath()}]))

    rfastElms = []
    for conn in connectors:
        attrs = conn.getUserAttributes(userAttributeNames=["rfastTool", "rfastName"])
        if attrs.len() == 0: continue
        rfastElms.append(conn)

    if len(rfastElms) == 0: return None
    nodes = []
    for conn in rfastElms:
        inter1 = conn.getEnd1InterfacePoint()
        if inter1:  # in same case it return None to avoid errors
            nodes.append(inter1.getAssociatedEntity())
        inter2 = conn.getEnd1InterfacePoint()
        if inter2:
            nodes.append(inter2.getAssociatedEntity())
    return nodes


def main(dict={}):
    # _selected = apex.selection.getCurrentSelection()

    myModel = apex.currentModel()
    global RutForm

    RutForm = float(dict["RutForm"])
    matlName = dict["material"]
    fastenerDia = float(dict["diameter"])
    tol = float(dict["tolerance"])
    gripLength = float(dict["gripLength"])

    print("Rut Form:       " + str(RutForm))
    print("Diameter:       " + str(fastenerDia))
    print("Grip Length:    " + str(gripLength))
    print("Material:       " + matlName)
    print("Tolerance:      " + str(tol))

    if matlName == "None":
        print("No material selected!")
        return

    # get the material that goes with the selected material name
    matls = apex.catalog.getMaterials([{"path": myModel.getName() + "/Materials"}])
    if matls.len() == 0:
        matls = apex.catalog.getCatalogMaterial().getMaterials()

    fastenerMatl = None
    for matl in matls:
        if matl.getName() == matlName:
            fastenerMatl = matl
            break

    if fastenerMatl == None:
        print("Unknown material for fastener?")
        return

    if fastenerDia <= 0.0:
        print("Invalid fastener diameter!")
        return

    if tol <= 0.0:
        print("Invalid tolerance!")
        return

    if gripLength <= 0.0:
        print("Invalid grip length!")
        return

    try:
        apex.beginUndoIndent()
        main2(fastenerDia, gripLength, fastenerMatl, matlName, tol)
    finally:
        apex.endUndoIndent()


def main2(fastenerDia, gripLength, fastenerMatl, matlName, tol):
    myModel = apex.currentModel()

    # get all nodes in the model from the mesh bodies
    allParts = myModel.getParts(True)

    _selected = apex.selection.getCurrentSelection()
    if _selected.len() == 0:
        for part in allParts: _selected.extend(part.getPoints())

    if _selected.len() == 0:
        print("There are no points in the model!")
        return

    # I am gathering mesh body nodes so that i can associate newly created nodes with the proper Part later in the script
    nodes = apex.entityCollection()
    meshedParts = apex.entityCollection()
    meshNodes = {}
    for part in allParts:
        meshes = part.getMeshes()
        if meshes.len() == 0: continue
        meshedParts.append(part)
        for mesh in meshes:
            newkey = mesh.getPath()+"/"+mesh.getName()
            meshNodes[newkey] = {"meshBody":mesh, "nodes":[]}
            nn = mesh.getNodes()
            nodes.extend(nn)
            for n in nn: meshNodes[newkey]["nodes"].append(n.getId())

    # if there are no meshes, there is no need to create fasteners
    if meshedParts.len() == 0:
        print("No meshed surfaces in any Part!")
        return
    # if there are no nodes, there is no need to create fasteners
    if nodes.len() == 0:
        print("No nodes in the model?")
        return

    # the selected points represent the fastener locations.  for now, i am only allowing points to be selected
    selPoints = apex.entityCollection()
    nuova_lista = apex.entityCollection()
    punti_da_elim = apex.entityCollection()
    lista_coord = []

    for punto in _selected:
        # risultato = punto.findCoincidentObjects (_selected, tolerance=0.001)
        loc1 = punto.getLocation()
        coord1 = [loc1.x, loc1.y, loc1.z]
        print("=" * 10, coord1)

        if len(lista_coord) == 0:
            lista_coord.append(coord1)
            selPoints.append(punto)
            continue

        meas1_m = 1.0e20
        for coord_old in lista_coord:
            meas1 = (coord1[0] - coord_old[0]) ** 2 + \
                    (coord1[1] - coord_old[1]) ** 2 + \
                    (coord1[2] - coord_old[2]) ** 2
            if meas1 < meas1_m:
                meas1_m = meas1

        if meas1 < 0.001:
            print("coincident points")
            continue
        else:
            selPoints.append(punto)

    #
    #    if punto not in risultato:
    #        nuova_lista.append(punto)
    #    else:
    #        punti_da_elim.extend(risultato)

    # for pto in nuova_lista:
    #    if pto not in punti_da_elim:
    #        selPoints.append(pto)

    if len(_selected) != len(selPoints):
        print("I have found duplicate location in the selection from ", len(_selected), " to ", len(selPoints))

    # selPoints = [sel for sel in _selected]  # this is assuming only points were selected

    mySearch = apex.utility.ProximitySearch()
    nip = [node for node in nodes]  # create a list of nodes, this is all nodes in the model
    mySearch.insertList(nip)

    # + I can only use nodes once.  i cannot re-use fastener nodes for other fasteners.
    # + This of course only works within the script.  i am not currently screening for pre-created fasteners
    usedNodes = []
    usedNodeIds = []

    nodes = getPreviouslyUsedNodes()
    if nodes != None:
        for node in nodes:
            usedNodes.append(node.asNode())
            usedNodeIds.append(node.asNode().getId())
    # + Each selected point is assumed to represent a fastener location.  The fastener will be located based
    # on the closest node to the point.  Currently there are no restrictions on the "closest" node.  In the future
    # I may limit it based on Part or similar

    print("Processing " + str(len(selPoints)) + " points for fasteners ...")
    numRfast = 0
    for point in selPoints:
        connData = []  # data associated with this fastener
        name = "RF-" + point.getName()
        print("Searching for close nodes at point: " + point.getName())
        # Nearest point may be tricky.  In the PCL that I wrote for rutman fasteners, I also had a search direction.  Here I do not.
        # Hopefully, I do not find and create fasteners within the plane of the plate.
        nearestObjects = mySearch.findNearestObjects(point.getLocation(),
                                                     6)  # I am doing 6 here in case some nodes are already used.  the number 6 is not magical.
        foundObjects = nearestObjects.foundObjects()
        dists = nearestObjects.getDistances()
        foundNearNode = False
        for item in enumerate(foundObjects):
            count = item[0]
            nearNode = item[1]
            dist = dists[count]
            # If the point is on the plate or perhaps a seed point, then a small tolerance is likely good here.  A larger tolerance
            # would be appropriate if the point is perhaps between the plates.  For now, I am using the user defined tolerance
            if dist > tol: continue
            if nearNode.getId() in usedNodeIds: continue  # can only use a node once
            connectedElms = nearNode.getElements()
            if connectedElms.len() == 0: continue  # the node must be connected to an element
            connectedElmIds = [elm.getId() for elm in connectedElms]
            foundNearNode = True
            break
        print("   Near node identified: " + str(foundNearNode))
        if foundNearNode == True:
            print("   Near node ID: " + str(nearNode.getId()))
            print("   Near node distance: " + str(dists[count]))
        else:
            print("   No near node found for point: " + point.getName())
            continue

        # At this point, I have a node that is within tolerance of the start location

        # Now find nodes close to my starting node
        nearestObjects = mySearch.findNearestObjects(nearNode,
                                                     30)  # nothing magical about 30, this may need to be increased
        foundObjects = nearestObjects.foundObjects()
        dists = nearestObjects.getDistances()
        vectors = nearestObjects.getVectors()

        # Search for the closest node to the node just found.  This will be used to define the orientation
        # of the fastener
        debug1 = False

        foundNearNode = False
        for item in enumerate(foundObjects):
            count = item[0]  # use this to locate this item in dists and vectors
            obj = item[1]  # this is the current near node for consideration
            if obj.getId() == nearNode.getId():
                if debug1:
                    print("debug: masternode")
                continue  # cannot find or reuse the start node
            if obj.getId() in usedNodeIds:
                if debug1:
                    print("debug: cannot reuse a node that has already been found")
                continue  # cannot reuse a node that has already been found
            elms = obj.getElements()
            if len(elms) == 0:
                if debug1:
                    print("debug: must connect to a node that connects to an element")
                continue  # must connect to a node that connects to an element
            foundConnectedElm = False
            for elm in elms:
                if elm.getId() in connectedElmIds:  # cannot connect to a node with shared element, can only use an element 1 time
                    foundConnectedElm = True
                    break
            if foundConnectedElm: continue

            if dists[count] <= gripLength:  # we have found a candidate node
                if debug1:
                    print("debug: # we have found a candidate node")

                # why am i multiplying by -1?
                x = -1 * vectors[count].getX() / vectors[count].getLength()
                y = -1 * vectors[count].getY() / vectors[count].getLength()
                z = -1 * vectors[count].getZ() / vectors[count].getLength()
                axisVec = apex.construct.Vector3D(x, y, z)

                nearNodeVec = getNormalAtNode(nearNode)
                cosTheta = myDot(axisVec, nearNodeVec)
                if abs(abs(cosTheta) - 1.0) > .0002:
                    if debug1:
                        print("debug: # vectors not aligned skipping ")
                    continue  # vectors not aligned.  this is about 1.15deg
                foundNodeVec = getNormalAtNode(obj)
                cosTheta = myDot(axisVec, foundNodeVec)
                if abs(abs(cosTheta) - 1.0) > .0002: continue  # vectors not aligned.  this is about 1.15deg

                foundNodes = [nearNode, obj]  # nodes in this fastener
                foundNodeIds = [nearNode.getId(), obj.getId()]
                usedNodes.append(nearNode)  # nodes in any fastener
                usedNodes.append(obj)
                usedNodeIds.append(nearNode.getId())
                usedNodeIds.append(obj.getId())
                for elm in elms:
                    connectedElms.append(elm)
                    connectedElmIds.append(elm.getId())
                foundNearNode = True
                print("   Found node near node: " + obj.getId())
                print("   Distance: " + str(dists[count]))
                print("   Axis Vector")
                print("   X: " + str(axisVec.getX()))
                print("   Y: " + str(axisVec.getY()))
                print("   Z: " + str(axisVec.getZ()))
                break

        if foundNearNode == False:
            print("   Node near node not found")
            continue

        # have found 2 nodes for the rutman fastener.  need to look if there are more within the griplength

        # create an aligned box to search for more fastener nodes within the griplength
        # get a 2nd node on an element that connects to the nearNode.  this will help define the box width
        ee = nearNode.getElements()[0]  # get a nearNode element
        nn = ee.getNodes()  # get all nodes on the element
        for n in nn:  # find a node that is not the nearNode
            if n.getId() != nearNode.getId(): break
        # create a unit vector from the nearNode to the newly found node (n)
        vv = createVector3D(nearNode, n)
        s = makeUnitVector(vv)

        vv = scaleVector(1.05 * gripLength,
                         axisVec)  # scale the axisVec so that it corresponds to the gripLength + fudge
        ss = scaleVector(1.1 * fastenerDia, s)  # scale the s vector so that it corresponds to the fastenerDia + fudge
        xx = addVectors(vv, ss)  # add these vectors.  this gives us loc1 for the axis aligned bounding box
        loc1 = apex.Coordinate(nearNode.getX() + xx.getX(), nearNode.getY() + xx.getY(), nearNode.getZ() + xx.getZ())

        vv = scaleVector(-1.05 * gripLength,
                         axisVec)  # scale the axisVec in the opposite direction so that it corresponds to the -gripLength - fudge
        ss = scaleVector(-2 * fastenerDia,
                         s)  # add these vectors.  this gives us loc2 for the axis aligned bounding box
        xx = addVectors(vv, ss)
        loc2 = apex.Coordinate(nearNode.getX() + xx.getX(), nearNode.getY() + xx.getY(), nearNode.getZ() + xx.getZ())

        # I MUST CHECK TO SEE IF THIS WORKS FOR LOC1, LOC2 NOT ALIGNED WITH GLOBAL AXES

        aaObjects = mySearch.findObjectsAABoundingBox(loc1, loc2)
        for obj in aaObjects:
            if debug1:
                print("debug: searching into a box", obj.getId())
            if not isinstance(obj, apex.mesh.Node): continue  # I am only looking for nodes
            if obj.getId() in foundNodeIds: continue  # cannot reuse a node
            if obj.getId() in usedNodeIds:  continue  # cannot reuse a node
            elms = obj.getElements()
            if elms.len() == 0: continue  # node must connect to an element
            foundConnectedElm = False
            for elm in elms:
                if elm.getId() in connectedElmIds:
                    foundConnectedElm = True
                    break
            if foundConnectedElm: continue  # can only connect to an element once

            # check that nearNode-obj vector aligns with axisVec
            vv = createVector3D(nearNode, obj)
            v = makeUnitVector(vv)
            cosTheta = myDot(axisVec, v)
            if abs(abs(cosTheta) - 1.0) > .0002: continue  # vectors not aligned.  this is about 1.15deg

            # If I am here the vectors are aligned
            foundNodes.append(obj)  # this node is part of the fastener
            foundNodeIds.append(obj.getId())
            usedNodes.append(obj)
            usedNodeIds.append(obj.getId())

        # Now I need to sort the found nodes in ascending order based on the axisVector
        cData = [[nearNode, 0.0]]
        for node in foundNodes:
            if node.getId() == nearNode.getId(): continue  # near node has already been added to cData

            vec = createVector3D(nearNode, node)  # create a vector from the nearNode to the current node
            dot = dotProduct(vec, axisVec)  # dot should be (hopefully) the location of the node along the axis

            cData.append([node, dot])
        sortedData = sorted(cData, key=itemgetter(1), reverse=False)  # ascending order sort on dot

        connData = sortedData
        print(str(len(connData)) + " nodes found for fastener")
        # At this point connData is simply
        # 0 = node connected to plate elm
        # 1 = distance
        # create coordinate frame
        coord = createCoord2(name, connData[0][0], connData[1][0])


        # CREATE NODES FOR THE FASTENERS (EXCEPT THE TOP AND BOTTOM, THOSE ARE CREATED LATER)

        createdNodes = True
        for data in connData:
            node = data[0]
            elms = node.getElements()
            # for now just get data for first element
            try:
                section = elms[0].getSection()
                thick = section.getThickness()
                matl = elms[0].getMaterial()
                E = matl.getElasticModulus()
                NU = matl.getPoissonRatio()

                if NU is None or NU == 0:
                    if RutForm == 1:
                        NU = 0.0
                        print("WARNING: Poisson's ratio = 0 for material: ", matl.getName())

                if debug1:
                    print("debug: ", section, thick, matl, E, NU)
            except:
                try:
                    # 1-6-2023:  for now, if a field exists, use this thickness
                    thick = elms[0].getThickness()
                    if thick is None or thick <= 0.0:
                        fields = elms[0].getFields()
                        if fields.len() == 0:
                            try:
                                thick = elms[0].getElementProperty2D().getProperties2DModel("PSHELL").getProperty("T")
                            except:
                                print("\nERROR: No 2D Element Properties assigned!\n")
                        else:
                            for field in fields:
                                fieldData = field.getDiscreteValue(
                                    type=apex.attribute.DiscreteFEMFieldType.DiscreteThicknessField)
                                for key in fieldData.keys():
                                    try:
                                        k = fieldData[key]['element_ids'].index(int(elms[0].getId()))
                                        thick = fieldData[key]["values"][k]
                                    except:
                                        pass
                                    if thick != None:
                                        print("\nERROR: no thickness properties ", )
                                        break
                                if thick != None:
                                    print("\nERROR: no thickness properties ", )
                                    break

                    # print(f"final thick: {thick}")
                    matlId = elms[0].getElementProperty2D().getProperties2DModel("PSHELL").getProperty("MID1")
                    matl = apex.catalog.getMaterialByID(matlId)
                    # matl    = elms[0].getMaterial()
                    # if matl == None: matl = fastenerMatl     # FM this needs work
                    E = matl.getMaterialModel("MAT1").getProperty('E')
                    NU = matl.getMaterialModel("MAT1").getProperty('NU')
                    if NU is None or NU == 0:
                        if RutForm == 1:
                            NU = 0.0
                            print("WARNING: Poisson's ratio = 0 for material: ", matl.getName())
                except:
                    createdNodes = False
                    break
            nodePart = setPartForNewNode(node, meshNodes)
            pointMesh = getPointMeshBody(
                nodePart)  # i am leaving this and subsequent occurances for the moment.  not sure this does anything

            # THICKNESS CHECK
            if thick is None or thick <=0:
                print("\nERROR: No thickness assigned! ")
                sys.exit()

            if pointMesh is None:
                nn = apex.mesh.createNodeByPickLocation(target=node, location=node)
            else:
                pointMesh.createNode(location=node)
            data.append(nn)
            data.append(thick)
            data.append(E)
            data.append(NU)

            foundNodes.append(nn)
            foundNodeIds.append(nn.getId())
            usedNodes.append(nn)
            usedNodeIds.append(nn.getId())
        # print(f"createdNodes: {createdNodes}")
        if createdNodes == False: continue

        # print("length of connData: "+str(len(connData)))
        # connData
        # 0 = node connected to plate elm
        # 1 = distance
        # 2 = new node created to connect bar
        # 3 = thickness of plate
        # 4 = E
        # 5 = NU
        # CREATE FASTENER BAR ELEMENTS AND PLATE RBAR ELEMENTS

        # print(connData)
        for k in range(len(connData) - 1):
            # create flexible connector
            nPlate0 = connData[k][0]  # node for 1st plate
            nPlate1 = connData[k + 1][0]  # node for 2nd plate
            n0 = connData[k][2]  # new node for 1st plate
            n1 = connData[k + 1][2]  # new node for 2nd plate

            nPlate0.assignAnalysisSystem(coord)
            nPlate1.assignAnalysisSystem(coord)
            n0.assignAnalysisSystem(coord)
            n1.assignAnalysisSystem(coord)

            flex = createFlexConnector(name, fastenerDia, fastenerMatl, n0, n1)
            addUserAttributes(flex, name)
            nodeTie = createRbar(name, nPlate0, nPlate1, "156")
            # addUserAttributes(nodeTie, name)

        # CREATE CBUSH CONNECTING PLATES TO THE FASTENERS
        try:
            Efast = fastenerMatl.getMaterialModel('MAT1').getProperty('E')
        except:
            Efast = fastenerMatl.getElasticModulus()
        for data in connData:
            nPlate = data[0]  # node connected to plate element
            nn = data[2]  # new node connected to bar element
            # print('Efast',Efast)
            cBush = createCbush(name, nPlate, nn, data[3], data[4], data[5], Efast, coord)
            addUserAttributes(cBush, name)

        # CREATE TOP BAR AND RBAR ELEMENT
        nTop = connData[0][0]  # node for top plate
        thick = connData[0][3]  # thickness of top plate
        # need to know the part this top node is in
        setPartForNewNode(nTop, meshNodes)

        # do i need to check if I don't find a part?
        x = nTop.getX() - .5 * thick * axisVec.getX()
        y = nTop.getY() - .5 * thick * axisVec.getY()
        z = nTop.getZ() - .5 * thick * axisVec.getZ()
        pt = apex.geometry.createPointXYZ(x=x, y=y, z=z)
        vv = pt.getVertices()
        nn = apex.mesh.createNodeByPickLocation(target=vv[0], location=apex.Coordinate(pt.getX(), pt.getY(), pt.getZ()))
        nn.assignAnalysisSystem(coord)
        flex = createFlexConnector(name, fastenerDia, fastenerMatl, nn, connData[0][2])
        addUserAttributes(flex, name)
        nodeTie = createRbar(name, nn, nTop, "1456")
        # addUserAttributes(nodeTie, name)

        # spc = createSPCForTopNode(name, nn, coord)
        # addUserAttributes(spc, name)

        # CREATE BOTTOM BAR AND RBAR ELEMENT
        k = len(connData) - 1
        nBot = connData[k][0]  # node for bottom plate
        thick = connData[k][3]  # thickness of bottom plate
        # need to know the part this bottom node is in
        # need to know the part this top node is in
        setPartForNewNode(nBot, meshNodes)

        # do i need to check if I don't find a part?
        x = nBot.getX() + .5 * thick * axisVec.getX()
        y = nBot.getY() + .5 * thick * axisVec.getY()
        z = nBot.getZ() + .5 * thick * axisVec.getZ()
        pt = apex.geometry.createPointXYZ(x=x, y=y, z=z)
        vv = pt.getVertices()
        nn = apex.mesh.createNodeByPickLocation(target=vv[0], location=apex.Coordinate(pt.getX(), pt.getY(), pt.getZ()))
        nn.assignAnalysisSystem(coord)
        flex = createFlexConnector(name, fastenerDia, fastenerMatl, connData[k][2], nn)
        addUserAttributes(flex, name)
        nodeTie = createRbar(name, nBot, nn, "56")
        # addUserAttributes(nodeTie, name)

        numRfast += 1

    print("Rutman fasteners created: " + str(numRfast))


