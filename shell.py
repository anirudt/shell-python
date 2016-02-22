
def cmd_loop():
    line, args, status = "", "", 1
    i = 0
    while status > 0:
        print "$ "
        line = cmd_read_line()
        args = cmd_split_line(line)
        status = cmd_exec(args)

        line, args = "", ""


if __name__ == "__main__":
    cmd_loop()
