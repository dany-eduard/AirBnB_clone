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
    __classes = {"BaseModel": BaseModel, "User": User}
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Method To Create A New Instance"""
        argsLine = line.split()
        if argsLine[0] == "":
            print("** class name missing **")
            return False
        elif argsLine[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            my_object = self.__classes[argsLine[0]]()
            print(my_object.id)
            my_object.save()

    def do_show(self, line):
        """ Method to show all isntance"""

        argsLine = line.split()
        lenArgs = len(argsLine)

        if (self.__check_if_exist(argsLine, lenArgs) != 1):

            searchInstance = argsLine[0] + "." + argsLine[1]
            the_classes = models.storage.all()

            if searchInstance in the_classes.keys():
                print(the_classes[searchInstance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Do """
        argsLine = line.split()
        lenArgs = len(argsLine)

        if (self.__check_if_exist(argsLine, lenArgs) != 1):

            searchInstance = argsLine[0] + "." + argsLine[1]
            the_classes = models.storage.all()

            if searchInstance in the_classes.keys():
                print(the_classes[searchInstance])
            else:
                print("** no instance found **")

    def do_update(self, line):
        """ Destroy the objects if exist"""
        argsLine = line.split()
        lenArgs = len(argsLine)

        if (self.__check_if_exist(argsLine, lenArgs) == 1):
            pass
        elif (lenArgs == 2):
            print("** attribute name missing **")
        elif (lenArgs == 3):
            print("** value missing **")
        else:
            searchInstance = argsLine[0] + "." + argsLine[1]
            the_classes = models.storage.all()
            if searchInstance in the_classes.keys():
                if argsLine[3]:
                    argsLine[3] = argsLine[3].replace('"', "")
                    print(argsLine[3])
                the_classes[searchInstance].__dict__[argsLine[2]] = argsLine[3]
                models.storage.save()
            else:
                print("** no instance found **")

    def __check_if_exist(self, argsLine, lenArgs):
        if argsLine[0] == "":
            print("** class name missing **")
            return 1
        elif argsLine[0] not in self.__classes:
            print("** class doesn't exist **")
            return 1
        elif (lenArgs == 1):
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
