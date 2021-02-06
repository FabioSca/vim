
" Space as leader
" let mapleader = " "
let g:mapleader = " "

" turn off key mappings
let g:gitgutter_map_keys = 0

" Define prefix dictionary
let g:lmap =  {}

" main menu
let g:lmap.f = { 'name' : 'File Menu' }

nmap <silent> <leader>fd :e $MYVIMRC<CR>
let g:lmap.f.d = ['e $MYVIMRC', 'Open vimrc']

nmap <silent> <leader>ft :Explore<CR>
let g:lmap.f.t = ['Vexplore', 'Open File Tree View']


call leaderGuide#register_prefix_descriptions("<Space>", "g:lmap") 
nnoremap <silent> <leader> :<c-u>LeaderGuide '<Space>'<CR>
vnoremap <silent> <leader> :<c-u>LeaderGuideVisual '<Space>'<CR>






nnoremap <localleader> :<c-u>LeaderGuide  ','<CR>
vnoremap <localleader> :<c-u>LeaderGuideVisual  ','<CR>
" This variant won't habe any group names.

" Group names can be defined by filetype. Add the following lines:
let g:llmap = {}
autocmd FileType tex let g:llmap.l = { 'name' : 'vimtex' }
call leaderGuide#register_prefix_descriptions(",", "g:llmap")
" to name the <localleader>-n group vimtex in tex files.



let g:olmap = {}

let g:olmap.a=['Ag', 'ag search']

call leaderGuide#register_prefix_descriptions("o", "g:olmap") 
nnoremap <silent> o :<c-u>LeaderGuide 'o'<CR>

let g:glmap = {}
call leaderGuide#register_prefix_descriptions("g", "g:glmap") 
nnoremap <silent> g :<c-u>LeaderGuide 'g'<CR>


" ========

"

" define prefix dictionary
let g:lmap={}

" git menu
let g:lmap.g={
              \'name' : 'Git',
              \'s' : ['Gstatus', 'Status'],
              \'p' : ['Gpull', 'Pull'],
              \'u' : ['Gpush', 'Push'],
              \'c' : ['Gcommit', 'Commit'],
              \'w' : ['Gwrite', 'Write'],
              \'d' : ['Gdiff', 'Diff'],
              \'l' : ['Glog', 'Log'],
              \'f' : ['Gfetch', 'Fetch'],
              \'b' : ['Gblame', 'Blame'],
              \'k' : ['Gitv', 'Gitk']
              \}

" gitgutter hunks menu
" let g:lmap.g.h={
"                 \'name' : 'Hunks',
"                 \'p' : ['call feedkeys("\<Plug>GitGutterPreviewHunk")', 'Preview'],
"                 \'u' : ['call feedkeys("\<Plug>GitGutterUndoHunk")', 'Undo'],
"                 \'s' : ['call feedkeys("\<Plug>GitGutterStageHunk")', 'Stage']
"                 \}
" 
" " nerdcommenter menu
" let g:lmap.c={
"               \'name' : 'Comments',
"               \' ' : ['call feedkeys("\<Plug>NERDCommenterToggle")', 'Toggle'],
"               \'$' : ['call feedkeys("\<Plug>NERDCommenterToEOL")', 'From cursor to EOL'],
"               \'a' : ['call feedkeys("\<Plug>NERDCommenterAltDelims")', 'Switch to alternate delimiters'],
"               \'A' : ['call feedkeys("\<Plug>NERDCommenterAppend")', 'Add comment at EOL'],
"               \'b' : ['call feedkeys("\<Plug>NERDCommenterAlignBoth")', 'Aligned both sides'],
"               \'c' : ['call feedkeys("\<Plug>NERDCommenterComment")', 'Comment'],
"               \'i' : ['call feedkeys("\<Plug>NERDCommenterInvert")', 'Toggle selected line(s)'],
"               \'l' : ['call feedkeys("\<Plug>NERDCommenterAlignLeft")', 'Aligned left side'],
"               \'m' : ['call feedkeys("\<Plug>NERDCommenterMinimal")', 'Minimal'],
"               \'n' : ['call feedkeys("\<Plug>NERDCommenterNested")', 'Nested'],
"               \'s' : ['call feedkeys("\<Plug>NERDCommenterSexy")', 'Sexy'],
"               \'u' : ['call feedkeys("\<Plug>NERDCommenterUncomment")', 'Uncomment'],
"               \'y' : ['call feedkeys("\<Plug>NERDCommenterYank")', 'Yank & comment']
"               \}
" 
" " test menu
" let g:lmap.e={
"               \'name' : 'Test',
"               \'t' : ['TestNearest', 'Nearest'],
"               \'T' : ['TestFile', 'This file'],
"               \'a' : ['TestSuite', 'All'],
"               \'l' : ['TestLast', 'Last'],
"               \'g' : ['TestVisit', 'Open test file']
"               \}
" 
" " toggles
" let g:lmap.t={
"               \'name' : 'Toggles',
"               \'l' : ['LToggle', 'Location list'],
"               \'q' : ['call asyncrun#quickfix_toggle(8)', 'Quickfix window'],
"               \'N' : ['NERDTreeToggle', 'NERDTree'],
"               \'t' : ['TagbarToggle', 'Tagbar'],
"               \'n' : ['NumbersToggle', 'Numbers'],
"               \'u' : ['UndotreeToggle', 'Undotree']
"               \}

" searches
"let g:lmap.a=['Ag', 'ag search']
"if has('mac')
"    let g:lmap.d=['Dash', 'Dash search']
"endif

call leaderGuide#register_prefix_descriptions("\\", "g:lmap")
nnoremap <silent> <leader> :<c-u>LeaderGuide '<leader>'<CR>
vnoremap <silent> <leader> :<c-u>LeaderGuideVisual '<leader>'<CR>
