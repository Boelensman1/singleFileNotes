if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

if exists('g:singleFileNotes_plugin_loaded')
    finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import main
EOF


function! AddNote()
    python3 main.add_note()
endfunction
command! -nargs=0 AddNote call AddNote()

"function! AddTodoFromCalender()
    "python3 main.add_from_calender()
"endfunction
"command! -nargs=0 AddTodoFromCalender call AddTodoFromCalender()

function! AddTodo()
    python3 main.add_todo()
endfunction
command! -nargs=0 AddTodo call AddTodo()

function! AddTodoTomorrow()
    python3 main.add_todo_tomorrow()
endfunction
command! -nargs=0 AddTodoTomorrow call AddTodoTomorrow()

" Add mappings that iterm uses 
:map ,,addnote <Esc>:call AddNote()<CR>
:imap ,,addnote <Esc>:call AddNote()<CR>

:map ,,addtodo <Esc>:call AddTodo()<CR>
:imap ,,addtodo <Esc>:call AddTodo()<CR>

:map ,,addtodotomorrow <Esc>:call AddTodoTomorrow()<CR>
:imap ,,addtodotomorrow <Esc>:call AddTodoTomorrow()<CR>

let g:singleFileNotes_plugin_loaded = 1
