import readline
import sys
import os

# Global readline instructions
readline.parse_and_bind('tab: complete')


def cmdExit():
    return -1

def cmdPwd():
    sys.stdout.write(os.getcwd())
    return 1

global_cmd_dict = {
        'exit': cmdExit,
        'pwd': cmdPwd
        }

global_cmd = ['exit', 'pwd']
def cmd_split_line(line):
    list_args = line.split( )
    return list_args

def cmd_exec(args):
    for w in args:
        if w in global_cmd:
            print w
            status = global_cmd_dict[w]()
    return status


def cmd_loop():
    line, args, status = "", "", 1
    i = 0
    while status > 0:
        sys.stdout.write('$ ')
        line = raw_input()
        args = cmd_split_line(line)
        status = cmd_exec(args)

        line, args = "", ""
        sys.stdout.write('\n')


if __name__ == "__main__":
    cmd_loop()
