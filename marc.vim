
setlocal foldmethod=expr
setlocal foldexpr=MarkdownFolds()

function! MarkdownFolds()
	let thisline = getline(v:lnum)
	if match(thisline,'^[a-z]') >= 0
		return ">1"
	else	
	 return "="
endfunction


