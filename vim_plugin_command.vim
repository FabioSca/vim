" vim: foldmethod=marker

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => PLUGIN 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

nmap <F8> :TagbarToggle<CR>
let g:tagbar_ctags_bin = '~/.vim/bundle/ctags_bin/ctags.exe'

""""""""""""""""""""""
" vim-bufferline {{{  
" """"""""""""""""""""
let g:bufferline_echo = 0
let g:bufferline_active_buffer_left = '['
let g:bufferline_active_buffer_right = ']'
let g:bufferline_inactive_highlight = 'airline_c'
let g:bufferline_active_highlight = 'airline_c'
" }}}

" => bufExplorer plugin {{{  
""""""""""""""""""""""""""""""
" let g:bufExplorerDefaultHelp=0
" let g:bufExplorerShowRelativePath=1
" let g:bufExplorerFindActive=1
" let g:bufExplorerSortBy='name'
" map <leader>o :BufExplorer<cr>
" }}}



let g:deoplete#enable_at_startup = 1
let g:float_preview#docked = 0
set completeopt-=preview " use floating window instead
" autocmd InsertLeave  * silent! pclose! " auto close preview
" autocmd CompleteDone * silent! pclose! " auto close preview (for c-y)
inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"


" You Complete Me
"""""""""""""""""""""""""""""""""""""""""""""""""""""
" let g:ycm_min_num_of_chars_for_completion = 1
" let g:ycm_min_num_identifier_candidate_chars = 0
" let g:ycm_collect_identifiers_from_comments_and_strings = 0
" let g:ycm_complete_in_strings = 1
" let g:ycm_complete_in_comments = 1
" let g:ycm_server_log_level = 'warning'
" let g:ycm_autoclose_preview_window_after_completion = 1
" let g:ycm_autoclost_preview_window_after_insertion = 1
" let g:ycm_confirm_extra_conf = 0            
" let g:ycm_key_invoke_completion = '<c-z>'
" noremap <c-z> <NOP>
" let g:ycm_semantic_triggers =  {
"     \ 'c,cpp,python,java,go,erlang,perl': ['re!\w{2}'],
"     \ 'cs,lua,javascript': ['re!\w{2}'],
"     \ }
" " 
" set completeopt=menu,menuone
" let g:ycm_add_preview_to_completeopt = 0
" "letPlug 'mhinz/vim-signify' g:ycm_show_diagnostics_ui = 0
" let g:ycm_filetype_whitelist = { 
"     \ "h":1,
"     \ "c":1,
"     \ "hh":1,
"     \ "cpp":1, 
"     \ "hpp":1,
"     \ "objc":1,
"     \ "sh":1,
"     \ "zsh":1,
"     \ "python":1,
"     \ "vim":1,
"     \ "go":1,
"     \ }
" 
" let g:ycm_key_list_select_completion = ['<C-j>', '<Down>']
" let g:ycm_key_list_previous_completion = ['<C-k>', '<Up>']
" " set global extra conf
" " let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
" " set for virtualenv


let g:python3_host_prog="C:/Anaconda3/python.exe"
let g:ycm_server_python_interpreter = "C:/Anaconda3/python.exe"
let &pythonthreedll='C:/Anaconda3/python36.dll'
let &pythonthreehome='C:/Anaconda3'
let &PYTHONHOME='C:/Anaconda3'
let PYTHONHOME='C:/Anaconda3'

"if has("win32")
"    let g:ycm_python_binary_path = "C:\Anaconda3\python.exe"

" let $PYTHONHOME = "D:\\Python36_32bit"
let g:ycm_error_symbol = '>>'
let g:ycm_warning_synbol = '--'

" You Complete Me
" nnoremap <Leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR>
" let g:_fengleyl_keymap.d = 'ycm-show-detailed-diagnostic'
" let g:_fengleyl_keymap.j = {
"     \ 'name': '+jump',
"     \ 'd': 'ycm#goto-definition-else-declaration',
" \ }



" jedi-vim {{{

" "if has('python3') || has('python3/dyn')
"   let g:jedi#force_py_version = 3.6
"   
"   let g:jedi#goto_command = "<Leader>jd"
"   let g:jedi#show_call_signatures = 2
"   let g:jedi#goto_assignments_command = "<Leader>ja"
"   let g:jedi#goto_definitions_command = ""
"   let g:jedi#documentation_command = "K"
"   let g:jedi#usages_command = "<Leader>ju"
"   let g:jedi#completions_command = "<C-Space>"
"   let g:jedi#rename_command = "<Leader>jr"
" "else
" "  let g:jedi#auto_initialization = 0
" "  let g:jedi#squelch_py_warning = 1
" "endif


"set pyxversion=3

"Python 3 executable file location


let $PYTHONPATH = "D:/Python36_32bit;D:/Python36_32bit/Lib"
let $PYTHONHOME = "D:/Python36_32bit"
let g:python3_host_prog = 'D:/Python36_32bit/python.exe'
set pythonthreedll=python36.dll

if has('windows')
   " let $PYTHON_DLL = "C:\Anaconda3"
   " let g:python3_host_prog = "C:/Anaconda3/python.exe"
   
   " set pythonthreehome="C:/Anaconda3/python.exe"
endif


 if vimrc#plugin#check#has_jedi()
" 
    let g:jedi#completions_enabled = 1
    
    
    let g:jedi#auto_initialization    = 0 
    let g:jedi#auto_vim_configuration = 0 
    let g:jedi#popup_on_dot           = 0 
    let g:jedi#popup_select_first     = 0 
    let g:jedi#show_call_signatures   = 0 
    let g:jedi#force_py_version = 3.6
" 
"   let g:jedi#goto_command             = '<C-X><C-G>'
"   let g:jedi#goto_assignments_command = '<C-X>a'
"   let g:jedi#goto_definitions_command = '<C-X><C-D>'
"   let g:jedi#documentation_command    = '<C-X><C-K>'
"   let g:jedi#usages_command           = '<C-X>c'
"   let g:jedi#completions_command      = '<C-X><C-X>'
"   let g:jedi#rename_command           = '<C-X><C-R>'
"   let g:jedi#goto_stubs_command       = '<C-X><C-S>'
" 
"   augroup jedi_vim_settings
"     autocmd!
"     autocmd FileType python call vimrc#jedi#mappings()
"   augroup END
 endif

" }}}



" vim-airline
"" airline configuration {{{

let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#branch#vcs_priority = ["git"]

set laststatus=2
let g:airline_powerline_fonts = 0
let g:airline_detect_spell=0

if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif
" unicode symbols
"let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
"let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.crypt = '🔒'
"let g:airline_symbols.linenr = '␊'
"let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.maxlinenr = '☰'
"let g:airline_symbols.maxlinenr = ''
let g:airline_symbols.branch = '⎇'
"let g:airline_symbols.paste = 'ρ'
"let g:airline_symbols.paste = 'Þ'
"let g:airline_symbols.paste = '∥'
let g:airline_symbols.paste = 'PASTE'
let g:airline_symbols.spell = 'Ꞩ'
let g:airline_symbols.notexists = '∄'
let g:airline_symbols.whitespace = 'Ξ'

"" powerline symbols
"let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
"let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
"let g:airline_symbols.branch = ''
"let g:airline_symbols.readonly = ''
"let g:airline_symbols.linenr = ''
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
""-let g:airline_theme = 'powerlineish'
""---let g:airline#extensions#branch#enabled = 1
""---let g:airline#extensions#ale#enabled = 1
""---let g:airline#extensions#tabline#enabled = 1
""---let g:airline#extensions#tagbar#enabled = 1
""---let g:airline_skip_empty_sections = 1

" " Vim-Airline Configuration
" let g:airline#extensions#tabline#enabled = 1
" let g:airline_powerline_fonts = 1 
" let g:airline_theme='hybrid'
" let g:hybrid_custom_term_colors = 1
" let g:hybrid_reduced_contrast = 1 

" vim-airline
""-- if !exists('g:airline_symbols')
""--   let g:airline_symbols = {}
""-- endif
""-- 
""-- if !exists('g:airline_powerline_fonts')
""--   let g:airline#extensions#tabline#left_sep = ' '
""--   let g:airline#extensions#tabline#left_alt_sep = '|'
""--   let g:airline_left_sep          = '▶'
""--   let g:airline_left_alt_sep      = '»'
""--   let g:airline_right_sep         = '◀'
""--   let g:airline_right_alt_sep     = '«'
""--   let g:airline#extensions#branch#prefix     = '⤴' "➔, ➥, ⎇
""--   let g:airline#extensions#readonly#symbol   = '⊘'
""--   let g:airline#extensions#linecolumn#prefix = '¶'
""--   let g:airline#extensions#paste#symbol      = 'ρ'
""--   let g:airline_symbols.linenr    = '␊'
""--   let g:airline_symbols.branch    = '⎇'
""--   let g:airline_symbols.paste     = 'ρ'
""--   let g:airline_symbols.paste     = 'Þ'
""--   let g:airline_symbols.paste     = '∥'
""--   let g:airline_symbols.whitespace = 'Ξ'
""-- else
""--   let g:airline#extensions#tabline#left_sep = ''
""--   let g:airline#extensions#tabline#left_alt_sep = ''
""-- 
""--   " powerline symbols
""--   let g:airline_left_sep = ''
""--   let g:airline_left_alt_sep = ''
""--   let g:airline_right_sep = ''
""--   let g:airline_right_alt_sep = ''
""--   let g:airline_symbols.branch = ''
""--   let g:airline_symbols.readonly = ''
""--   let g:airline_symbols.linenr = ''
""-- endif


" VimFiler {{{

" let g:vimfiler_as_default_explorer = 1
" call vimfiler#custom#profile('explorer', 'context', {
"       \  'safe': 0,
"       \  'simple': 0
"       \ })
" autocmd FileType vimfiler nmap <buffer> i :VimFilerPrompt<CR>
" let g:vimfiler_tree_leaf_icon = '¦'
" let g:vimfiler_tree_opened_icon = '▾'
" let g:vimfiler_tree_closed_icon = '▸'

" let g:vimfiler_file_icon = '-'
" let g:vimfiler_marked_file_icon = '*'
"}}}

" => MRU plugin {{{  
""""""""""""""""""""""""""""""
let MRU_Max_Entries = 400
map <leader>f :MRU<CR>
" }}}

" => Startify {{{  
""""""""""""""""""""""""""""""
" :h g:startify_enable_unsafe
" let g:startify_enable_unsafe = 1
" }}}

" => Easymotion  {{{  
""""""""""""""""""""""""""""""
let g:EasyMotion_do_mapping = 0 " Disable default mappings
map <leader>e <Plug>(easymotion-overwin-f2)
let g:EasyMotion_smartcase = 1

""""""""""""""""""""""""""""""
" }}}

" => Leader {{{  
""""""""""""""""""""""""""""""
source ~/vim_main/vim_mappings.vim
" }}}

" => YankStack  una specie di Emacs   {{{  
""""""""""""""""""""""""""""""
"let g:yankstack_yank_keys = ['y', 'd']

"nmap <c-p> <Plug>yankstack_substitute_older_paste
"nmap <c-n> <Plug>yankstack_substitute_newer_paste
" }}}

" => CTRL-P   {{{  
""""""""""""""""""""""""""""""
" let g:ctrlp_working_path_mode = 0
" 
" let g:ctrlp_map = '<c-f>'
" map <leader>j :CtrlP<cr>
" map <leader>p :CtrlP<cr>
" map <c-b> :CtrlPBuffer<cr>
" 
" let g:ctrlp_max_height = 20
" let g:ctrlp_custom_ignore = 'node_modules\|^\.DS_Store\|^\.git\|^\.coffee'
" }}}

" => ZenCoding   {{{  
""""""""""""""""""""""""""""""
" Enable all functions in all modes
let g:user_zen_mode='a'


""""""""""""""""""""""""""""""
" => snipMate (beside <TAB> support <CTRL-j>)
""""""""""""""""""""""""""""""
ino <c-j> <c-r>=snipMate#TriggerSnippet()<cr>
snor <c-j> <esc>i<right><c-r>=snipMate#TriggerSnippet()<cr>
" }}}

" => Vim grep     {{{  
""""""""""""""""""""""""""""""
let Grep_Skip_Dirs = 'RCS CVS SCCS .svn generated'
set grepprg=/bin/grep\ -nH
" }}}

" => Nerd Tree  {{{  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"let g:NERDTreeWinPos = "left"
"let NERDTreeShowHidden=1
"let NERDTreeIgnore = ['\.pyc$', '__pycache__']
"let g:NERDTreeWinSize=35
"map <leader>nn :NERDTreeToggle<cr>
"map <leader>nb :NERDTreeFromBookmark<Space>
"map <leader>nf :NERDTreeFind<cr>
" }}}
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
" 设置当文件被改动时自动载入
set autoread
au FocusGained * :checktime

"
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" => vim-multiple-cursors
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:multi_cursor_use_default_mapping=0
"
" Default mapping FABIO schiacca C-s invece di C-n  s come sublime text
"let g:multi_cursor_start_word_key      = '<C-n>'
let g:multi_cursor_start_word_key      = '<C-s>'
let g:multi_cursor_select_all_word_key = '<A-n>'
let g:multi_cursor_start_key           = 'g<C-n>'
let g:multi_cursor_select_all_key      = 'g<A-n>'
let g:multi_cursor_next_key            = '<C-n>'
let g:multi_cursor_prev_key            = '<C-p>'
let g:multi_cursor_skip_key            = '<C-x>'
let g:multi_cursor_quit_key            = '<Esc>'
let g:multi_cursor_quit_key            = '<Esc>'


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => surround.vim config
" Annotate strings with gettext 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
vmap Si S(i_<esc>f)
au FileType mako vmap Si S"i${ _(<esc>2f"a) }<esc>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => lightline   {{{  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ }

let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ ['mode', 'paste'],
      \             ['fugitive', 'readonly', 'filename', 'modified'] ],
      \   'right': [ [ 'lineinfo' ], ['percent'] ]
      \ },
      \ 'component': {
      \   'readonly': '%{&filetype=="help"?"":&readonly?"ðŸ”’":""}',
      \   'modified': '%{&filetype=="help"?"":&modified?"+":&modifiable?"":"-"}',
      \   'fugitive': '%{exists("*fugitive#head")?fugitive#head():""}'
      \ },
      \ 'component_visible_condition': {
      \   'readonly': '(&filetype!="help"&& &readonly)',
      \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))',
      \   'fugitive': '(exists("*fugitive#head") && ""!=fugitive#head())'
      \ },
      \ 'separator': { 'left': ' ', 'right': ' ' },
      \ 'subseparator': { 'left': ' ', 'right': ' ' }
      \ }
" }}}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Vimroom  {{{  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:goyo_width=100
let g:goyo_margin_top = 2
let g:goyo_margin_bottom = 2
nnoremap <silent> <leader>z :Goyo<cr>
" }}}


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Vim-go
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" let g:go_fmt_command = "goimports"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Syntastic (syntax checker)   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:ale_linters = {
\   'javascript': ['jshint'],
\   'python': ['flake8'],
\   'go': ['go', 'golint', 'errcheck']
\}

nmap <silent> <leader>a <Plug>(ale_next_wrap)

" Disabling highlighting
let g:ale_set_highlights = 0

" Only run linting when saving the file
let g:ale_lint_on_text_changed = 'never'
let g:ale_lint_on_enter = 0


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Git gutter (Git diff)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:gitgutter_enabled=0
nnoremap <silent> <leader>d :GitGutterToggle<cr>


" If you use NERDCommenter:
let g:lmap.c = { 'name' : 'Comments' }
" Define some descriptions
let g:lmap.c.c = ['call feedkeys("\<Plug>NERDCommenterComment")','Comment']
let g:lmap.c[' '] = ['call feedkeys("\<Plug>NERDCommenterToggle")','Toggle']
" The Descriptions for other mappings defined by NerdCommenter, will default
" to their respective commands.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => vim-autoclose
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" let g:AutoClosePairs = "() {} \""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => delimitMate
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" let delimitMate_expand_cr = 1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Neocomplete Settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Neocomplete Plugin mappins
" inoremap <expr><C-g>     neocomplete#undo_completion()
" inoremap <expr><C-l>     neocomplete#complete_common_string()

" Recommended key-mappings.
" <CR>: close popup and save indent.
inoremap <silent> <CR> <C-r>=<SID>my_cr_function()<CR>

" <TAB>: completion.
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"

" <C-h>, <BS>: close popup and delete backword char.
" inoremap <expr><C-h> neocomplete#smart_close_popup()."\<C-h>"
" inoremap <expr><BS> neocomplete#smart_close_popup()."\<C-h>"

let g:acp_enableAtStartup = 0
let g:neocomplete#enable_at_startup = 1
let g:neocomplete#enable_smart_case = 1
let g:neocomplete#sources#syntax#min_keyword_length = 3

" Define dictionary.
let g:neocomplete#sources#dictionary#dictionaries = {
    \ 'default' : '',
    \ 'vimshell' : $HOME.'/.vimshell_hist',
    \ 'scheme' : $HOME.'/.gosh_completions'
        \ }

" Define keyword.
if !exists('g:neocomplete#keyword_patterns')
    let g:neocomplete#keyword_patterns = {}
endif
let g:neocomplete#keyword_patterns['default'] = '\h\w*'

" Enable heavy omni completion.
if !exists('g:neocomplete#sources#omni#input_patterns')
  let g:neocomplete#sources#omni#input_patterns = {}
endif

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => vim-leader-guide
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current
" position. Coc only does snippet and additional edit on confirm.
" <cr> could be remapped by other vim plugin, try `:verbose imap <CR>`.
if exists('*complete_info')
  inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"
else
  inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
endif

" Use `[g` and `]g` to navigate diagnostics
" Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming.
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code.
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder.
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap keys for applying codeAction to the current buffer.
nmap <leader>ac  <Plug>(coc-codeaction)
" Apply AutoFix to problem on the current line.
nmap <leader>qf  <Plug>(coc-fix-current)

" Map function and class text objects
" NOTE: Requires 'textDocument.documentSymbol' support from the language server.
xmap if <Plug>(coc-funcobj-i)
omap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap af <Plug>(coc-funcobj-a)
xmap ic <Plug>(coc-classobj-i)
omap ic <Plug>(coc-classobj-i)
xmap ac <Plug>(coc-classobj-a)
omap ac <Plug>(coc-classobj-a)

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of LS, ex: coc-tsserver
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocAction('format')

" Add `:Fold` command to fold current buffer.
" command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add (Neo)Vim's native statusline support.
" NOTE: Please see `:h coc-status` for integrations with external plugins that
" provide custom statusline: lightline.vim, vim-airline.
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Mappings for CoCList
" Show all diagnostics.
nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions.
nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
" Show commands.
nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document.
nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols.
nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list.
nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>


