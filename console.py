#!/usr/bin/python3
"""
The Line Command To The APi (BackEnd)
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ This class to setup the command interpreter """
    __classes = {"BaseModel": BaseModel, "User" : User}
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Method To Create A New Instance"""
        arrayLine = line.split(" ")
        if arrayLine[0] == "":
            print("** class name missing **")
            return False
        elif arrayLine[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            my_object = self.__classes[arrayLine[0]]()
            print(my_object.id)
            my_object.save()

    def do_show(self, line):
        """ Method to show all isntance"""

        arrayLine = line.split(" ")
        lenArray = len(arrayLine)

        if (self.__check_if_exist(arrayLine, lenArray) != 1):

            searchInstance = arrayLine[0] + "." + arrayLine[1]
            the_classes = models.storage.all()

            if searchInstance in the_classes.keys():
                print(the_classes[searchInstance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Destroy the objects if exist"""
        arrayLine = line.split(" ")
        lenArray = len(arrayLine)

        if (self.__check_if_exist(arrayLine, lenArray) != 1):

            searchInstance = arrayLine[0] + "." + arrayLine[1]
            the_classes = models.storage.all()

            if searchInstance in the_classes.keys():
                del the_classes[searchInstance]
                models.storage.save()
            else:
                print("** no instance found **")

    def __check_if_exist(self, arrayLine, lenArray):
        if arrayLine[0] == "":
            print("** class name missing **")
            return 1
        elif arrayLine[0] not in self.__classes:
            print("** class doesn't exist **")
            return 1
        elif (lenArray == 1):
            print("** instance id missing **")
            return 1

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
