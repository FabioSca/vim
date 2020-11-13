" vim: foldmethod=marker

" Shortcuts {{{{
" <tab> Switch between the splits
nnoremap <tab> <C-W><C-W>

" {V,H} create v/h split
nmap <leader>V :vnew<CR>
nmap <leader>H :new<CR>

" Show nerdTree
" nnoremap <leader>n :NERDTreeToggle<CR>

" Remove highlight
nnoremap qq :nohl<CR>

" Remap quit
" nnoremap q :close<CR>

" Remaps leader keys
nnoremap ; :

" Show MRU
" nnoremap <leader>m :Mru<CR>

" C+w+{=,_,|} - Equal proporsions, maximise vertically, horizontally
" }}}}


" WhichKey {{{
"nnoremap <silent> <leader> :WhichKey '`'<CR>
set timeoutlen=300

let g:which_key_map =  {}
" }}}}

" Configs:            <leader>+c+{r,e,m,p,i,Z,U,M} {{{
let g:which_key_map['c'] = {
    \ 'name' : '+config',
    \ 'r'    : [':so ~/_vimrc'    , 'Reload _vimrc'         ],
    \ 'e'    : [':e ~/_vimrc'     , 'Edit _vimrc'           ],
    \ 'm'    : [':e ~/vim_mappings.vim' , 'Edit key WhichKey'],
    \ 'p'    : [':e ~/vim_plugin.vim'   , 'Edit Plugin '   ],
    \ 'i'    : [':e ~/vim_plugin_command.vim' , 'Edit plugin command'  ],
    \ 'Z'    : [':PluginInstall'  , 'Install plugins'       ],
    \ 'U'    : [':PluginUpdate'   , 'Update plugins'        ],
    \ 'M'    : [':Maps'           , 'Show mappings'         ],
    \ }
" }}}

" Projects:           <leader>+p+{s,w,m,f,n,N} {{{
let g:which_key_map['p'] = {
    \ 'name' : '+projects'    ,
    \ 's'    : [':Rg '            , 'Search content'         ],
    \ 'w'    : [':Ag <C-R><C-W><CR>' , 'Search word'        ],
    \ 'm'    : [':LeaderfMru'    , 'Recent files'           ],
    \ 'f'    : [':LeaderfFile'   , 'Fuzzy find'             ],
    \ 'n'    : [':NERDTreeFind'  , 'NERDTree'               ],
    \ 'd'    : [':NERDTree D:\'  , 'NERDTree D:\'               ],
    \ 'N'    : [':NERDTreeToggle', 'NERDTreeToggle'         ]
    \ }
" }}}
" Splits:             <leader>+s+{n,v,c,h,j,k,l,=,_,|} {{{
let g:which_key_map['s'] = {
    \ 'name' : '+splits'      ,
    \ 'n'    : [':new'        , 'New split (hor)'           ],
    \ 'v'    : [':vnew'       , 'New split (ver)'           ],
    \ 'c'    : [':close'      , 'Close split'               ],
    \ 'h'    : ['<C-W>h'      , 'Focus split left'          ],
    \ 'j'    : ['<C-W>j'      , 'Focus split below'         ],
    \ 'k'    : ['<C-W>k'      , 'Focus split above'         ],
    \ 'l'    : ['<C-W>l'      , 'Focus split right'         ],
    \ '='    : ['<C-W>='      , 'Equal width / height'      ],
    \ '_'    : ['<C-W>_'      , 'Full width'                ],
    \ '|'    : ['<C-W>|'      , 'Full height'               ],
    \ }
" }}}
" Tabs:               <leader>+t+{n,l,h,c} {{{
let g:which_key_map['t'] = {
    \ 'name' : '+tabs'        ,
    \ 'n'    : [':tabnew'     , 'New tab'                   ],
    \ 'l'    : [':tabnext'    , 'Next tab'                  ],
    \ 'h'    : [':tabprev'    , 'Previous tab'              ],
    \ 'c'    : [':tabclose'   , 'Close tab'                 ],
    \ }
" }}}
" Buffers:            <leader>+b+{s,l,h,d,t,f,T,q,Q,n,w} {{{
let g:which_key_map['b'] = {
    \ 'name' : '+buffer'      ,
    \ '1'    : [':b1' , '1'            ],
    \ '2'    : [':b2' , '2'            ],
    \ 's'    : [':LeaderfBuffer' , 'Find buffer'            ],
    \ 'l'    : [':bnext'         , 'Next buffer'            ],
    \ 'h'    : [':bprev'         , 'Previous buffer'        ],
    \ 'd'    : [':bdel'          , 'Delete buffer'          ],
    \ 't'    : [':LeaderfBufTag' , 'Search tags'            ],
    \ 'f'    : [':LeaderfFunction', 'Search functions'      ],
    \ 'T'    : [':Tagbar'        , 'Tagbar'                 ],
    \ 'q'    : [':copen'         , 'Open quickfix'          ],
    \ 'Q'    : [':cclose'        , 'Close quickfix'         ],
    \ 'n'    : [':call multiple_cursors#new("n", 1)' , 'Close quickfix'],
    \ 'w'    : [':w'             , 'Write buffer'           ],
    \ }
" }}}
" Mode:                 <leader>+m+{w,z,g,s,n,N} {{{
let g:which_key_map['m'] = {
    \ 'name' : '+mode'      ,
    \ 'w'    : [':Goyo'     , 'Write mode (toggle)'         ],
    \ 'z'    : [':ZoomWin'  , 'Zoom window (toggle)'        ],
    \ 'g'    : [':GitGutterToggle', 'Toggle gutter'         ],
    \ 's'    : [':Startify' , 'Start up page'               ],
    \ 'n'    : [':set number!' , 'Toggle numbers'           ],
    \ 'N'    : [':set relativenumber!' , 'Toggle rel numbers']
    \ }
" }}}

" Nastran: <leader>+n+{n,h,r} {{{
let g:which_key_map['n'] = {
    \ 'name' : '+nastran'       ,
    \ 'n'    : [':set colorcolumn=0' , "nohighlight" ],
    \ 's'    : [':set syn=nastran' ,"syntax"],
    \ 'z'    : [':set foldexpr=""' ,"nofold"],
    \ 'f'    : [':call NastranFold()' ,"fold"],
    \ 'r'    : [':silent ! start cmd /k C:\MSC.Software\lancia_nastran.bat % %:p:h <CR>'    , 'RUN'                        ]
    \ }
" }}}

" VCS: <leader>+v+{a,P,f,p,s,c,b,l,d} {{{
let g:which_key_map['v'] = {
    \ 'name' : '+vcs'       ,
    \ 'a'    : [':Gwrite'   , 'Add'                         ],
    \ 'P'    : [':Gpush'    , 'Push'                        ],
    \ 'f'    : [':Gfetch'   , 'Fetch'                       ],
    \ 'p'    : [':Gpull'    , 'Pull'                        ],
    \ 's'    : [':Gstatus'  , 'Status'                      ],
    \ 'c'    : [':Gcommit'  , 'Commit'                      ],
    \ 'b'    : [':Gblame'   , 'Blame'                       ],
    \ 'l'    : [':GV', 'Log'                                ],
    \ 'd'    : [':Gdiff'    , 'Diff'                        ]
    \ }
" }}}
" Run: <leader>+r+{a,s,t} {{{
let g:which_key_map['r'] = {
    \ 'name' : '+run'       ,
    \ 'a'    : ['echo :AsyncRun '   , 'Async run'           ],
    \ 's'    : [':AsyncStop'        , 'Stop async run'      ],
    \ 't'    : [':terminal bash'    , 'Open a terminal'     ],
    \ }
" }}}

let g:which_key_map.V = 'which_key_ignore'
let g:which_key_map.H = 'which_key_ignore'
let g:which_key_map.q = 'which_key_ignore'
"let g:which_key_map.n = 'which_key_ignore'

call which_key#register("<space>", "g:which_key_map")
nnoremap <silent> <leader> :<c-u>WhichKey "<space>"<CR>
vnoremap <silent> <leader> :<c-u>WhichKeyVisual "<space>"<CR>
nnoremap <silent> <leader>pw :Ag <C-R><C-W><CR>
" }}}

