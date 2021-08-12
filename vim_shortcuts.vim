"
" => Shortcut
"
"
"
runtime plugin/shortcut.vim

" mappings {{{
  " Map shortcuts
"  Shortcut show shortcut menu and run chosen shortcut
"  \ noremap <silent> <Leader><Leader> :Shortcuts<Return>
"  Shortcut fallback to shortcut menu on partial entry
"  \ noremap <silent> <Leader> :Shortcuts<Return>
  
  
  " maximize or restore current window in split structure
  Shortcut maximize or restore current window in split structure 
      \ noremap <C-w>O :call <SID>MaximizeToggle()<CR>
  " noremap <C-w><C-o> :call <SID>MaximizeToggle()<CR>

  " remap arrow keys
  "nmap h :bprev<CR>
  Shortcut switch to previous buffer 
      \ nmap <S-Left> :bprev<CR>
  " :call LightLineBufferline()<CR>:call lightline#update()<CR>
  "nmap l :bnext<CR>
  Shortcut switch to next buffer 
      \ nmap <S-Right> :bnext<CR>
  " :call LightLineBufferline()<CR>:call lightline#update()<CR>

  " sane regex {{{
    nnoremap / /\v
    vnoremap / /\v
    nnoremap ? ?\v
    vnoremap ? ?\v
    nnoremap :s/ :s/\v
  " }}}

  " command-line window {{{
    "nnoremap q: q:i
    "nnoremap q/ q/i
    "nnoremap q? q?i
  " }}}

  " folds {{{
    "nnoremap zr zr:echo &foldlevel<CR>
    "nnoremap zm zm:echo &foldlevel<CR>
    "nnoremap zR zR:echo &foldlevel<CR>
    "nnoremap zM zM:echo &foldlevel<CR>
  " }}}

  " auto center {{{
    "nnoremap <silent> n nzz
    "nnoremap <silent> N Nzz
    "nnoremap <silent> * *zz
    "nnoremap <silent> # #zz
    "nnoremap <silent> g* g*zz
    "nnoremap <silent> g# g#zz
    "nnoremap <silent> <C-o> <C-o>zz
    "nnoremap <silent> <C-i> <C-i>zz
  "}}}

  " reselect visual block after indent {{{
    "vnoremap < <gv
    "vnoremap > >gv
  "}}}

  " make Y consistent with C and D. See :help Y.
  "nnoremap Y y$

  " hide annoying quit message
  "nnoremap <C-c> <C-c>:echo<CR>

  " window killer
    Shortcut close window or kill buffer 
        \ nnoremap <silent> Q :call CloseWindowOrKillBuffer()<CR>

  " applications {{{
    Shortcut (undotree) toggle undotree 
        \ nnoremap <silent>  <Leader>au :UndotreeToggle<CR>
  " }}}

  " buffers {{{
    Shortcut (fzf) open buffer
        \ nnoremap <silent> <Leader>bb :Buffers<CR>

  " }}}

  " files {{{
    Shortcut (fzf) open file in/under working directory 
      \ nnoremap <silent> <Leader>ff :Files<CR>

    Shortcut (fzf) open file relative to current file
        \ nnoremap <silent> <Leader>fF :execute 'Files' expand('%:h')<CR>

    Shortcut (fzf) open file from history
        \ nnoremap <silent> <Leader>fr :History<CR>

    Shortcut (nerdtree) open/close nerdtree in working directory
        \ nnoremap <silent> <Leader>ft :NERDTreeToggle<CR>

    Shortcut (nerdtree) open nerdtree in current buffer's directory
        \ nnoremap <silent> <Leader>fT :NERDTreeFind<CR>

    Shortcut (fzf) open file in git repository
        \ nnoremap <silent> <Leader>fg :GFiles<CR>

    Shortcut (fzf) open file in git status
        \ nnoremap <silent> <Leader>fG :GFiles?<CR>

  " }}}

  " " git/versions-control {{{

    Shortcut (fugitive) git blame 
        \ nnoremap <silent> <Leader>gb :Gblame<CR>

    Shortcut (fugitive) git commit 
        \ nnoremap <silent> <Leader>gc :Gcommit<CR>

    Shortcut (fugitive) git diff 
        \ nnoremap <silent> <Leader>gd :Gvdiff<CR>

    Shortcut (fugitive) git log 
        \ nnoremap <silent> <Leader>gl :Glog<CR>

    Shortcut (fugitive) git push 
        \ nnoremap <silent> <Leader>gp :Git push<CR>

    Shortcut (fugitive) git remove 
        \ nnoremap <silent> <Leader>gr :Gremove<CR>

    Shortcut (fugitive) git status 
        \ nnoremap <silent> <Leader>gs :Gstatus<CR>

    Shortcut (fzf) git commit history 
        \ nnoremap <silent> <Leader>gv :Commits<CR>

    Shortcut (fzf) git commit history of current buffer 
        \ nnoremap <silent> <Leader>gV :BCommits<CR>

    Shortcut (fugitive) git commit/write 
        \ nnoremap <silent> <Leader>ga :Gwrite<CR>

  " search/symbol {{{

    " search current word in current directory
    Shortcut (fzf) search word under cursor in current directory 
        \ nnoremap <silent> <Leader>sd :call fzf#vim#lines(expand('<cword>'))<CR>

    " search current word in current file
    Shortcut (fzf) search word under cursor in current file 
        \ nnoremap <silent> <Leader>sf :call fzf#vim#buffer_lines(expand('<cword>'))<CR>

    " search the selected text in current directory
    Shortcut (fzf) search selected text in current directory 
        \ vnoremap <silent> <Leader>sd :call fzf#vim#lines(<SID>GetVisualSelection())<CR>

    " search the selected text in current file
    Shortcut (fzf) search selected text in current file 
        \ vnoremap <silent> <Leader>sf :call fzf#vim#buffer_lines(<SID>GetVisualSelection())<CR>

    Shortcut (fzf) go to line in any file in directory
        \ nnoremap <silent> <Space>jF :Ag<Return>


    " " search specific content in current directory
    " nnoremap <SID>grep-in-directory :vimgrep /\<<C-r>=expand("<cword>")<CR>\>/j **/*<Left><Left><Left><Left><Left><Left><Left><Left><Left>
    " nmap <Leader>sgd <SID>grep-in-directory

    " " search specific content in current file
    " nnoremap <SID>grep-in-file :vimgrep /\<<C-r>=expand("<cword>")<CR>\>/j <C-r>%
    " nmap <Leader>sgf <SID>grep-in-file

    " " repeat last search
    " nnoremap <SID>grep-last :execute 'vimgrep /'.@/.'/g %'<CR>:copen<CR>
    " nmap <Leader>sl <SID>grep-last

    "  replace specific content
    Shortcut search and replace word under cursor 
        \ nnoremap <Leader>sr :%s/\<<C-r>=expand("<cword>")<CR>\>/<C-r>=expand("<cword>")<CR>/g<Left><Left>

    " replace the selected text
    Shortcut search and replace selected text 
        \ vnoremap <silent> <Leader>sr :call <SID>VisualSelection('replace')<CR>

    Shortcut search and replace 
        \ nnoremap <Leader>sR :%s///g<Left><Left><Left>

    if dein#is_sourced('asyncrun.vim')
      Shortcut create ctags 
          \ nnoremap <silent> <Leader>sta :AsyncRun! gtags;cscope -Rbq;ctags -R<CR>
      Shortcut remove ctags 
          \ nnoremap <silent> <Leader>stv :AsyncRun! rm tags;rm cscope.in.out;rm cscope.out;rm cscope.po.out;rm GTAGS;rm GRTAGS;rm GPATH<CR>
    endif

    " cscope
    if has("cscope")
        " go to definition
        "vnoremap <SID>gtags-definition <Esc>:execute 'Gtags ' . <SID>GetVisualSelection()
        Shortcut go to definition 
            \ nnoremap <Leader>std :Gtags -d <C-r>=expand("<cword>")<CR>

        " locate strings
        "nnoremap <SID>gtags-strings :execute 'Gtags -g ' . expand('<cword>')
        "vnoremap <SID>gtags-strings <Esc>:execute 'Gtags -g ' . <SID>GetVisualSelection()
        Shortcut locate word under cursor
            \ noremap <Leader>ste :Gtags -g <C-r>=expand("<cword>")<CR>

        " get a list of tags in specified files
        "vnoremap <SID>gtags-files <Esc>:execute 'Gtags -f ' . <SID>GetVisualSelection()
        Shortcut get list of tags in specified files 
            \ nnoremap <Leader>stf :Gtags -f %<CR>

        " go to definition or reference
        Shortcut go to definition of reference 
            \ nnoremap <Leader>stg :GtagsCursor<CR>

        " find reference
        "vnoremap <SID>gtags-reference <Esc>:execute 'Gtags -r ' . <SID>GetVisualSelection()
        Shortcut find reference 
            \ nnoremap <Leader>str :Gtags -r <C-r>=expand("<cword>")<CR>

        " locate symbols which are not defined in `GTAGS`
        "vnoremap <SID>gtags-symbols <Esc>:execute 'Gtags -s ' . <SID>GetVisualSelection()
        Shortcut locate symbols which are not defined in GTAGS 
            \ nnoremap <Leader>sts :Gtags -s <C-r>=expand("<cword>")<CR>
    endif

  "}}}

  " toggles {{{
    Shortcut toggle automatic symbol highlight 
        \ nnoremap <silent> <Leader>th :call AutoHighlightToggle()<CR>
    call AutoHighlightToggle() " enable default autohighlighting

    Shortcut (indent-guides) toggle indent guides 
        \ nnoremap <silent> <Leader>ti :IndentGuidesToggle<CR>

    Shortcut (tagbar) toggle tagbar 
        \ nnoremap <silent> <Leader>tt :TagbarToggle<CR>


    " Toggle between normal and relative numbering.
    Shortcut toggle between relative and normal numbering 
        \ nnoremap <leader>tr :call NumberToggle()<CR>

    
    Shortcut toggle chromatica syntax highlighting
        \ nnoremap <leader>tc :ChromaticaToggle<CR>

    " nnoremap <silent> <SID>quickfix :call <SID>ListToggle("Quickfix List", 'c')<CR>
    " nmap <Leader>tq <SID>quickfix

    " nnoremap <silent> <SID>whitespace :set list!<CR>
    " nmap <Leader>tw <SID>whitespace

  "}}}

  "  jump {{{

      " Jump to line in current buffer
      Shortcut (fzf) jump to line in current buffer 
          \ nnoremap <silent> <Leader>jl :BLines<CR>

      " Jump to line in all open buffers
      Shortcut (fzf) jump to line in all open buffers 
          \ nnoremap <silent> <Leader>jd :Lines <CR>

      Shortcut (fzf) jump to ctag in all open buffers
          \ nnoremap <silent> <Leader>jT :Tags<CR>

      Shortcut (fzf) jump to ctag in current buffer
          \ nnoremap <silent> <Leader>jt :BTags<CR>

      Shortcut (fzf) jump to mark in current buffer
          \ nnoremap <silent> <Leader>jm :Marks<CR>

      Shortcut (fzf) open file in filesystem
          \ nnoremap <Space>fF :Locate<Space>

  " history {{{
      Shortcut (fzf) repeat command from history
          \ nnoremap <silent> <Space>:. :History:<Return>

      Shortcut (fzf) repeat search from history
            \ nnoremap <silent> <Space>:/ :History/<Return>
  " }}}

  " windows {{{

    Shortcut balance windows 
        \ nnoremap <silent> <Leader>w= <C-w>=

    Shortcut toggle maximize 
        \ nnoremap <Leader>wm :call <SID>MaximizeToggle()<CR>

  " }}}

  " text {{{
    Shortcut format file 
        \ nnoremap <Leader>xf :call <SID>Preserve("normal gg=G")<CR>

    " repeatable copy and paste. fake the behavior in windows
    Shortcut repeatable paste 
        \ nnoremap <Leader>xp viw"zp

    Shortcut repeatable copy 
        \ nnoremap <Leader>xy "zyiw

    Shortcut repeatable paste (visual mode)
        \ vnoremap <Leader>xp "zp

    Shortcut repeatable copy (visual mode) 
        \ vnoremap <Leader>xy "zy

    " reselect last paste
    Shortcut reselect last paste 
        \ nnoremap <expr> <Leader>xr '`[' . strpart(getregtype(), 0, 1) . '`]'

    " formatting
    Shortcut strip trailing whitespaces 
        \ nnoremap <Leader>xt :call StripTrailingWhitespace()<CR>

    Shortcut sort selected lines 
        \ vnoremap <Leader>xls :sort<CR>

  " }}}

" Set to working directory of current open buffer: ,cd
Shortcut set cwd to directory of opened file
  \ nnoremap ,cd :cd %:p:h<CR>:pwd<CR>

" properly functioning paste
set pastetoggle=<F4>

Shortcut toggle linenumbers
  \ nnoremap <F5> :set nonumber! number?<CR>
Shortcut toggle show invisible chars
  \ nnoremap <F6> :set list! list?<CR>

" use C-r with visual selection for search and replace
vnoremap <C-r> "hy:%s/<C-r>h//g<left><left>
Shortcut toggle mark long lines and trailing whitespace
  \ nnoremap <F8> :call StyleCheckToggle()<cr>
Shortcut toggle quick reference trick
  \ nnoremap <F2> :call ToggleVimReference()<CR>

" Buffer management
Shortcut close buffer
  \ nnoremap <leader>bq :q<CR>
Shortcut save buffer
  \ noremap <leader>bw :w<CR>
Shortcut write and close buffer
  \ nnoremap <leader>bwq :wq<CR>

" Smart copying things
Shortcut clone and paste paragraph
  \ noremap <leader>cp yap<S-}>p

" Add empty line above/under without going into insert-mode
Shortcut insert line above
  \ noremap <leader>O O<Esc>j
Shortcut insert line under
  \ noremap <leader>o o<Esc>k

Shortcut toggle ale and gitgutter (quiet please!)
  \ nnoremap <Leader>t :GitGutterToggle<CR>
  " \ nnoremap <Leader>t :ALEToggle<CR>:GitGutterToggle<CR>
Shortcut open quickfix buffer
  \ nnoremap <Leader>qf :copen<CR>
Shortcut markdown: create table of content
  \ nnoremap <Leader>tc :Tocv<CR>
"}}}
