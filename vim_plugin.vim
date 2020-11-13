

" Disable file type for vundle
filetype off                  " required

" - Avoid using standard Vim directory names like 'plugin'
"
" FABIO ad Agosto 2019 cambiato in https://github.com/junegunn/vim-plug
" vundle forse non + supportato
"
call plug#begin('~/.vim/plugged')

" Make sure you use single quotes

" Fabio plugin in SpaceVim
" startify troppo lento sembra problema noto probabile casino con altri plugin 
" forse messo per primo non rallenta
Plug 'mhinz/vim-startify'


" On-demand loading
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'tiagofumo/vim-nerdtree-syntax-highlight', { 'on': 'NERDTreeToggle' }
Plug 'Xuyuanp/nerdtree-git-plugin', { 'on': 'NERDTreeToggle' }
"Plug 'OrangeT/vim-csharp', {'for':'cs'}
let g:vue_pre_processors = []


" Plugin outside ~/.vim/plugged with post-update hook
" Plug 'junegunn/fzf', { 'do': './install --bin' }
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Ag plugin
Plug 'rking/ag.vim', { 'on': 'Ag' }


" Utility
"Plug 'scrooloose/nerdtree'
" Plug 'ryanoasis/vim-devicons'  " va in conflitto con altri non accendere

Plug 'Shougo/unite.vim'
Plug 'Shougo/vimfiler.vim'
Plug 'romgrk/vimfiler-prompt'


Plug 'majutsushi/tagbar', {'on':'TagbarToggle'}
"Plug 'ervandew/supertab' " fa casino con jedi 
" Plug 'BufOnly.vim'
Plug 'wesQ3/vim-windowswap'

" Plug 'SirVer/ultisnips'
Plug 'godlygeek/tabular'
" Plug 'ctrlpvim/ctrlp.vim'
" Plug 'benmills/vimux'           " interagisce con tmux
Plug 'jeetsukumaran/vim-buffergator'   " ricordare solo che ,b apre buffergator list puo essere sostituido :b TAB
Plug 'bling/vim-bufferline'
" Plug 'ap/vim-buftabline'   " niente di che

Plug 'gilsondev/searchtasks.vim'
"Plug 'Shougo/neocomplete.vim'

" Plug 'tpope/vim-dispatch'   " tolto non so che fa

" Plug 'mru.vim'
" Plug 'francoiscabrol/ranger.vim'


" Plug 'hecal3/vim-leader-guide'
Plug 'liuchengxu/vim-which-key'
" Plug 'Shougo/unite'
"
Plug 'sunaku/vim-shortcut'
"Plug 'easymotion/vim-easymotion'

Plug 'terryma/vim-multiple-cursors'


" Apri una shell
Plug 'Shougo/vimproc.vim'
Plug 'shougo/vimshell.vim'

Plug 'voldikss/vim-floaterm'

" Generic Programming Support 
Plug 'universal-ctags/ctags'
" Plug 'honza/vim-snippets'
" Plug 'Townk/vim-autoclose'      " no serve progetto chiuso
" Plug 'Raimondi/delimitMate'     " chiude le parentesi
Plug 'tomtom/tcomment_vim'        " commenta e toglie commenti con shortcut
Plug 'tobyS/vmustache'            " no usero mai serve per script
" Plug 'janko-m/vim-test'         " lancia test
" Plug 'maksimr/vim-jsbeautify'   " javascript
Plug 'vim-syntastic/syntastic'
" Plug 'neomake/neomake'

" Markdown / Writting
" Plug 'reedes/vim-pencil'
" Plug 'tpope/vim-markdown'
" Plug 'jtratner/vim-flavored-markdown'
" Plug 'LanguageTool'

" Git Support
" Plug 'kablamo/vim-git-log'
" Plug 'gregsexton/gitv'
" Plug 'tpope/vim-fugitive'
" Plug 'jaxbot/github-issues.vim'

" PHP Support
" Plug 'phpvim/phpcd.vim'
" Plug 'tobyS/pdv'

" Cheat sheet
Plug 'tinyheero/vim-myhelp' " Personal vim-cheatsheet


" Elm Support
" Plug 'lambdatoast/elm.vim'

" Theme / Interface
" Plug 'AnsiEsc.vim'
Plug 'ryanoasis/vim-devicons'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Plug 'sjl/badwolf'
" Plug 'tomasr/molokai'
" Plug 'morhetz/gruvbox'
" Plug 'zenorocha/dracula-theme', {'rtp': 'vim/'}
" Plug 'junegunn/limelight.vim'
" Plug 'mkarmona/colorsbox'
" Plug 'romainl/Apprentice'
" Plug 'Lokaltog/vim-distinguished'
" Plug 'chriskempson/base16-vim'
" Plug 'w0ng/vim-hybrid'
" Plug 'AlessandroYorba/Sierra'
Plug 'daylerees/colour-schemes'

" Atom One Dark theme.
Plug 'joshdick/onedark.vim'

Plug 'crusoexia/vim-monokai'
" Plug 'effkay/argonaut.vim'
" Plug 'ajh17/Spacegray.vim'
" Plug 'atelierbram/Base2Tone-vim'
" Plug 'colepeters/spacemacs-theme.vim'

" Python

" Use release branch (recommend)
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" Or build from source code by using yarn: https://yarnpkg.com
Plug 'neoclide/coc.nvim', {'do': 'yarn install --frozen-lockfile'}





" QUESTO BUONO MA PROVO COC
" if has('nvim')
"   Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
" else
"   Plug 'Shougo/deoplete.nvim'
"   Plug 'roxma/nvim-yarp'
"   Plug 'roxma/vim-hug-neovim-rpc'
"   Plug 'deoplete-plugins/deoplete-jedi'
" endif

" Plug 'Valloric/YouCompleteMe'  "meglio non usarlo in Windows
" Plug 'davidhalter/jedi-vim'


" Plug 'zchee/deoplete-jedi'


" Initialize plugin system
call plug#end()

