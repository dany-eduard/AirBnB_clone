#!/usr/bin/python3
"""
The Line Command To The APi (BackEnd)
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ This class to setup the command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, line):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

    def emptyline(self):
        "Function that avoid that prints a new line with string"
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
