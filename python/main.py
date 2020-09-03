import vim
import datetime
import math

import calender

longestDate = 27 # len(Wednesday 10 September 2020) = 27
headerlength = longestDate + 4 * 2 + 2 # 2 spaces

def pad(input):
    padding_length = (27 - len(input)) / 2
    padding_left = ' ' * (math.floor(padding_length) + 1)
    padding_right = ' ' * (math.ceil(padding_length) + 1)
    return padding_left + input + padding_right

def get_datestring(tomorrow=False):
    date = datetime.date.today()
    if tomorrow:
        date = date + datetime.timedelta(days=1)
    return '=' * 4 + pad(date.strftime("%A %d %B %Y")) + '=' * 4

def add_date(datestring):
    vim.current.buffer.append(['','=' * headerlength, datestring, '=' * headerlength,'@TODO',''])

def search(pattern):
    result = vim.eval('search("'+ pattern+'", "c")')
    return result

def scroll_to_bottom():
    length = len(vim.current.buffer)
    vim.current.window.cursor = (length,0)

def add_entry(tomorrow=False):
    datestring = get_datestring(tomorrow)

    # check if we already have $currentday
    if int(search(datestring)) == 0:
        scroll_to_bottom()
        add_date(datestring)

def add_note():
    add_entry()
    # scroll to @TODO
    search('@TODO')
    # go up 1 line
    vim.current.window.cursor = (vim.current.window.cursor[0]-1,0)

def add_todo():
    add_entry()
    scroll_to_bottom()

def add_from_calender():
    add_entry()
    scroll_to_bottom()
    events = calender.get_events()
    vim.current.buffer.append(events)

def add_todo_tomorrow():
    add_entry(True)
    scroll_to_bottom()
