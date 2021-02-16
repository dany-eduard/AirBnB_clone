#!/usr/bin/python3
"""
The Line Command To The APi (BackEnd)
"""
import cmd
import

class HBNBCommand(cmd.Cmd):
    """ This class to setup the command interpreter """
    __classes = {"BaseModel"}
    prompt = "(hbnb) "

    def do_create(self, line):

        arrayLine = line.split(" ")

        if arrayLine[0] == "":
            print("** class name missing **")
        elif arrayLine[0] not in  self.__classes:
            print("** class doesn't exist **")

    def do_show(self, line):

        arrayLine = line.split(" ")
        if arrayLine[0] == "":
            print("** class name missing **")
        elif arrayLine[0] not in  self.__classes:
            print("** class doesn't exist **")
        elif (len(arrayLine) == 1):
            print("** instance id missing **")

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
