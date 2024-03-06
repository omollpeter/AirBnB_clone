#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
It contains the following class definitions:
    HBNBCommand - Inherits from the cmd module

"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Entry point for the command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quits the command line interpreter
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        Handles Ctrl-D
        """
        return True

    def help_EOF(self):
        print("Exits the command line interpreter using Ctrl-D\n")

    def emptyline(self):
        """
        Overrides the default emptyline(). Doesn't execute anything
        """

        return ""

    def do_create(self, class_):
        """
        Creates a new instance of BaseModel
        """
        pass

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) "
              + "and prints the id. Example: create BaseModel\n")

    def do_show(self, class_, id):
        """
        Prints the string representation of an instance
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
