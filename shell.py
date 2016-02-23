#!/usr/bin/python

import readline
import sys
import os
import pdb
from termcolor import colored
import getpass

# Global readline instructions
readline.parse_and_bind('tab: complete')
f = open(os.getcwd()+'/.hist', 'ab')
readline.read_history_file(os.getcwd() + '/.hist')

username = getpass.getuser()
f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
ipaddr = f.read().rstrip()

def prompt_decor():
    f = os.popen('acpi | grep -oP "\d+(?=%)"')
    charge = f.read().rstrip()
    pwd = os.getcwd()

    prompt_string = colored(username, 'cyan') + " at " + colored(ipaddr, 'green') + \
                    ", " + charge +"% in " + pwd
    return prompt_string
    


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
    files_bin = os.listdir('/bin')
    files_usr_bin = os.listdir('/usr/bin')
    #pdb.set_trace()
    if args[0] in files_bin:
        os.system('/bin/'+' '.join(args))
        return 1
    if args[0] in files_usr_bin:
        os.system('/usr/bin/'+' '.join(args))
        return 1
    else:
        return 0

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
    #pdb.set_trace()
    status = 0
    for w in args:
        if w in global_cmd_dict.keys():
            status = global_cmd_dict[w](args)
            break
        else:
            status = cmdOutsource(args)
            if status == 1:
                break
    if status==0:
        sys.stdout.write("anirudt-shell: command not found: "+args[0])
        return 100
    return status


def cmd_loop():
    line, args, status = "", "", 1
    i = 0
    os.chdir('/home/anirudt')
    while status > 0:
        prompt = prompt_decor() + "\n" + "$ "
        line = raw_input(prompt)
        args = cmd_split_line(line)
        if status == 1:
            f.write(line+'\n')

        status = cmd_exec(args)
        line, args = "", ""
        sys.stdout.write('\n')


if __name__ == "__main__":
    cmd_loop()
