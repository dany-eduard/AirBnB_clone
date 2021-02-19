#!/usr/bin/python3
"""
The Line Command To The APi (BackEnd)
"""

import re
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class to setup the command interpreter """
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. """
        argsLine = line.split()

        if line == "":
            print("** class name missing **")
            #return false
        elif argsLine[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            my_object = self.__classes[argsLine[0]]()
            print(my_object.id)
            my_object.save()

    def do_show(self, line):
        """ Prints the string representation of an instance based on the
            class name and id """
        argsLine = line.split()
        lenArgs = len(argsLine)

        if (self.__check_if_exist(argsLine, lenArgs) != 1):

            searchId = argsLine[0] + "." + argsLine[1]
            dictInstan = models.storage.all()

            if searchId in dictInstan.keys():
                print(dictInstan[searchId])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)."""
        argsLine = line.split()
        lenArgs = len(argsLine)
        if (self.__check_if_exist(argsLine, lenArgs) != 1):

            searchId = argsLine[0] + "." + argsLine[1]
            dictInstan = models.storage.all()

            if searchId in dictInstan.keys():
                del dictInstan[searchId]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute(save the change into the JSON file)"""
        argsLine = line
        lenArgs = len(argsLine)

        if self.__check_if_exist(argsLine, lenArgs) == 1:
            pass
        elif (lenArgs == 2):
            print("** attribute name missing **")
        elif (lenArgs == 3):
            print("** value missing **")
        else:
            searchId = argsLine[0] + "." + argsLine[1]
            dictInstan = models.storage.all()
            if searchId in dictInstan.keys():
                if argsLine[3]:
                    argsLine[3] = argsLine[3].replace('"', "")
                try:
                    argsLine[3] = int(argsLine[3])
                except ValueError:
                    try:
                        argsLine[3] = float(argsLine[3])
                    except ValueError:
                        argsLine[3] = argsLine[3]
                dictInstan[searchId].__dict__[argsLine[2]] = argsLine[3]
                dictInstan[searchId].save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
            based or not on the class name."""
        argsLine = line.split()
        if line == "" or argsLine[0] in self.__classes:
            dictInstan = models.storage.all()
            listClasses = []
            for key, value in dictInstan.items():
                if line in key:
                    listClasses.append(value.__str__())
            print(listClasses)
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        " To retrieve the number of instances of a class "
        argsLine = line.split()
        if line == "" or argsLine[0] in self.__classes:
            dictInstan = models.storage.all()
            count = 0
            for key, value in dictInstan.items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """ Dafault function """
        lineSplit = line.split('.')
        if len(lineSplit) > 1:
            class_name = lineSplit[0]
            function_name = lineSplit[1].split('"')[0] + line[-1]
            strParameters = lineSplit[1][:-1].replace('"',"").replace("(",",")
            listParameters = strParameters.split(",")
            listParameters[0] = class_name
            strParameters = " ".join(listParameters)
            print(class_name)
            print(function_name)
            if function_name[:-1] == "all()":
                print("all")
                self.do_all(class_name)
            if function_name[:-1]  == "count()":
                print("count")
                self.do_count(class_name)
            if function_name == "show()":
                print("show")
                self.do_show(strParameters)
            if function_name == "destroy()":
                print("destroy")
                self.do_destroy(strParameters)
            if function_name == "update()":
                print("update")
                self.do_update(strParameters)
        else:
            cmd.Cmd.default(self, line)

    def __check_if_exist(self, argsLine, lenArgs):
        """Function that check if the class exist or the instance missing"""
        if lenArgs == 0:
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
