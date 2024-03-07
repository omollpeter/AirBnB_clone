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

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        arguments = cmd.Cmd.parseline(self, line)
        if arguments[0] is None:
            print("** class name missing **")
        else:
            if arguments[0] == BaseModel.__name__:
                new_model = BaseModel()
                setattr(new_model, "email", "omoll@email.com")
                storage.save()
            else:
                print("** class doesn't exist **")


    def help_create(self):
        print("Creates a new instance of BaseModel, saves it "
              + "(to the JSON file) and prints the id.\n"
              + "Example: create BaseModel\n")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        print(f"{line}")

    def help_show(self):
        print(" Prints the string representation of an "
              + "instance based on the class name and id.\n"
              + "Ex: $ show BaseModel 1234-1234-1234\n")

    def do_destroy(self, line):
        """
        Deletes an instance
        """
        pass

    def help_destroy(self):
        print("Deletes an instance based on the class name and id "
              + "(save the change into the JSON file).\n"
              + "Ex: $ destroy BaseModel 1234-1234-1234\n")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on class name
        """
        args = cmd.Cmd.parseline(self, line)
        print(args[:-1])

    def help_all(self):
        print("Prints a list of all string representation of all "
              + "instances based or not on the class name.\n"
              + "Ex: $ all BaseModel or $ all\n")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        pass

    def help_update(self):
        print("Updates an instance based on the class name "
              + "and id by adding or updating attribute (save the "
              + "change into the JSON file).\n"
              + "Ex: $ update BaseModel 1234-1234-1234 email 'bnb@mail.com'\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
