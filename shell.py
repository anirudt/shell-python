#!/usr/bin/python

import readline
import sys
import os

# Global readline instructions
readline.parse_and_bind('tab: complete')
f = open(os.getcwd()+'/.hist', 'ab')
readline.read_history_file(os.getcwd() + '/.hist')

# Handles exit
def cmdExit(args=None):
    return -1

# Handles pwd
def cmdPwd(args=None):
    sys.stdout.write(os.getcwd())
    return 1

def cmdCd(args):
    global f
    f.close()
    os.chdir(args[1])
    f = open(os.getcwd()+'/.hist', 'ab')
    readline.read_history_file(os.getcwd() + '/.hist')
    sys.stdout.write(os.getcwd())
    return 1

def cmdOutsource(args):
    os.system('/usr/bin/'+args[0]+' '+args[1])
    return 1

#-------------------------------------------------------------------
global_cmd_dict = {
        'exit': cmdExit,
        'pwd': cmdPwd,
        'cd': cmdCd
        }

global_cmd_outSource = ['vi', 'vim', 'ssh']

def cmd_split_line(line):
    list_args = line.split( )
    return list_args

def cmd_exec(args):
    status = 0
    for w in args:
        if w in global_cmd_dict.keys():
            status = global_cmd_dict[w](args)
            break
        if w in global_cmd_outSource:
            status = cmdOutsource(args)
            break
    if status==0:
        sys.stdout.write("anirudt-shell: command not found: "+args[0])
        return 100
    return status


def cmd_loop():
    line, args, status = "", "", 1
    i = 0
    while status > 0:
        prompt = os.getcwd()+"$ "
        line = raw_input(prompt)
        args = cmd_split_line(line)
        if status == 1:
            f.write(line+'\n')

        status = cmd_exec(args)
        line, args = "", ""
        sys.stdout.write('\n')


if __name__ == "__main__":
    cmd_loop()
