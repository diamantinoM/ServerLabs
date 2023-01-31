"""
$ copy fich1 fich2
file copied

$ copy fich1 direc/fich2
file copied

$ copy fich1
wrong number of arguments: missing arguments

$ dir direc
...

$ dir .
...
"""

import cmd
import sys
import binutils


class Shell(cmd.Cmd):
    # fix tab-completion behaviour on OS X (which uses libedit)
    if sys.platform == 'darwin':  
        import readline
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")

    prompt = "$ "

    def do_copy(self, args):
        """copy <file1> <file2>"""
        files = args.split()
        if len(files) != 2:
            print("wrong number of arguments: missing arguments")
        else:
            nbytes = binutils.copy(*files)
            print("Bytes copied:", nbytes)

    def do_dir(self, args):
        """dir [<direc>]"""
        print(args)

    def do_bye(self, arg):
        print("Bye, bye...")
        return True


if __name__ == '__main__':
    Shell().cmdloop()
