#!/usr/bin/python3
"""
The Line Command To The APi (BackEnd)
"""
import cmd
import models
from models.base_model import BaseModel

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
        else:
            my_object = eval(arrayLine[0]+ "()")
            print(my_object)

    def do_show(self, line):

        arrayLine = line.split(" ")
        lenArray = len(arrayLine)
        if arrayLine[0] == "":
            print("** class name missing **")
        elif arrayLine[0] not in  self.__classes:
            print("** class doesn't exist **")
        elif (lenArray == 1):
            print("** instance id missing **")
        elif lenArray >= 2:
            searchInstance = arrayLine[0] + "." + arrayLine[1]
            the_class =  models.storage.all()
            if searchInstance in the_class.keys():
                print(the_class[searchInstance])
            else:
                print("** no instance found **")


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
