#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
It contains the following class definitions:
    HBNBCommand - Inherits from the cmd module

"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models import storage
import re
import json
from datetime import datetime


classes = ["BaseModel", "User", "City", "Place", "Amenity", "State", "Review"]


def parse_line_with_args_double_quotes(match, line):
    """
    Parses a args that contains string args in double
    quotes
    """
    for i in range(len(match)):
        previous = match[i]
        match[i] = match[i].replace(" ", "_")
        line = line.replace(previous, match[i])
    args = line.split()
    for i in range(len(match)):
        idx = args.index(match[i])
        args[idx] = args[idx].replace("_", " ").strip('"')
    return args


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
        pattern = r'(".*?")'
        match = re.findall(pattern, line)
        if match:
            args = parse_line_with_args_double_quotes(match, line)
        else:
            args = line.split()
        if not args:
            print("** class name missing **")
        else:
            if args[0] in classes:
                if args[0] == BaseModel.__name__:
                    new_model = BaseModel()
                    print(new_model.id)
                    storage.save()
                elif args[0] == User.__name__:
                    new_user = User()
                    print(new_user.id)
                    storage.save()
                elif args[0] == City.__name__:
                    new_city = City()
                    print(new_city.id)
                    storage.save()
                elif args[0] == Place.__name__:
                    new_place = Place()
                    print(new_place.id)
                    storage.save()
                elif args[0] == State.__name__:
                    new_state = State()
                    print(new_state.id)
                    storage.save()
                elif args[0] == Amenity.__name__:
                    new_amenity = Amenity()
                    print(new_amenity.id)
                    storage.save()
                elif args[0] == Review.__name__:
                    new_review = Review()
                    print(new_review.id)
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
        pattern = r'(".*?")'
        match = re.findall(pattern, line)
        if match:
            args = parse_line_with_args_double_quotes(match, line)
        else:
            args = line.split()

        if not args:
            print("** class name missing **")
        else:
            if len(args) >= 2:
                if args[0] in classes:
                    storage.reload()
                    key = args[0] + "." + args[1]
                    all_instances = storage.all()
                    if key in all_instances.keys():
                        print(all_instances[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")

    def help_show(self):
        print(" Prints the string representation of an "
              + "instance based on the class name and id.\n"
              + "Ex: $ show BaseModel 1234-1234-1234\n")

    def do_destroy(self, line):
        """
        Deletes an instance
        """
        pattern = r'(".*?")'
        match = re.findall(pattern, line)
        if match:
            args = parse_line_with_args_double_quotes(match, line)
        else:
            args = line.split()
        if not args:
            print("** class name missing **")
        else:
            if len(args) >= 2:
                if args[0] in classes:
                    key = args[0] + "." + args[1]
                    all_instances = storage.all()
                    if key in all_instances.keys():
                        del all_instances[key]
                        storage.update_objects(all_instances)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")

    def help_destroy(self):
        print("Deletes an instance based on the class name and id "
              + "(save the change into the JSON file).\n"
              + "Ex: $ destroy BaseModel 1234-1234-1234\n")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on class name
        """
        pattern = r'(".*?")'
        match = re.findall(pattern, line)
        storage.reload()
        if match:
            args = parse_line_with_args_double_quotes(match, line)
        else:
            args = line.split()

        if not args:
            objects = storage.all()
            objects_list = [objects[key] for key in objects.keys()]
            print(objects_list)
        elif args[0] in classes:
            objects = storage.all()
            objects_list = []
            for key in objects.keys():
                if key.startswith(args[0]):
                    objects_list.append(objects[key])
            print(objects_list)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints a list of all string representation of all "
              + "instances based or not on the class name.\n"
              + "Ex: $ all BaseModel or $ all\n")

    def do_count(self, line):
        """
        Prints count of instances based on class name
        """
        pattern = r'(".*?")'
        match = re.findall(pattern, line)
        storage.reload()
        if match:
            args = parse_line_with_args_double_quotes(match, line)
        else:
            args = line.split()

        if args[0] in classes:
            objects = storage.all()
            objects_list = []
            for key in objects.keys():
                if key.startswith(args[0]):
                    objects_list.append(objects[key])
            print(len(objects_list))
        else:
            print("** class doesn't exist **")

    def help_count(self):
        print("Prints count of instances based on class name\n"
              + "Ex: $ count BaseModel\n")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        pattern = r'(".*?")'
        match = re.findall(pattern, line)
        if match:
            args = parse_line_with_args_double_quotes(match, line)
        else:
            args = line.split()

        if not args:
            print("** class name missing **")
        else:
            if len(args) >= 4:
                if args[0] in classes:
                    key = args[0] + "." + args[1]
                    all_instances = storage.all()
                    if key in all_instances.keys():
                        pattern1 = r'^-?\d+$'
                        pattern2 = r'^-?\d+(\.\d+)?([eE][+-]?\d+)?$'
                        if re.match(pattern1, args[3]):
                            args[3] = int(args[3])
                        elif re.match(pattern2, args[3]):
                            args[3] = float(args[3])
                        path = storage.get_path()
                        content = {}
                        with open(path, "r", encoding="utf-8") as file:
                            content = json.load(file)

                        for key_, value in content.items():
                            if key_ == key:
                                update = datetime.now().isoformat()
                                value["updated_at"] = update
                                value[args[2]] = args[3]

                        with open(path, "w", encoding="utf-8") as file:
                            json.dump(content, file)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 3:
                print("** value missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 1:
                print("** instance id missing **")

    def help_update(self):
        print("Updates an instance based on the class name "
              + "and id by adding or updating attribute (save the "
              + "change into the JSON file).\n"
              + "Ex: $ update BaseModel 1234-1234-1234 email 'bnb@mail.com'\n")

    def default(self, line):
        """
        Executes command that do not follow the do_* criterion
        """
        line = line.strip()
        args = line.split(".")
        if len(args) == 1:
            print("** unknown command **")
        else:
            cls_name = args[0]

            pattern1 = r'([a-z]+)'
            pattern2 = r'(\(.*\))'
            pattern3 = r'(\{.*\})'
            command = re.search(pattern1, args[1])
            if command:
                command = command.group(1)
                arguments = re.search(pattern2, args[1])
                if arguments:
                    arguments = arguments.group(1).strip("()")
                    dict_in_args = re.search(pattern3, arguments)
                    if dict_in_args and command == "update":
                        dict_in_args = dict_in_args.group(1)
                        dict_ = dict_in_args.replace("'", '"')
                        dict_ = json.loads(dict_)
                        id_ = arguments.split(", ")[0].strip('"')
                        for key, value in dict_.items():
                            k_v = key + " " + str(value)
                            update_args = cls_name + " " + id_ + " " + k_v
                            self.do_update(update_args)
                    else:
                        arguments = arguments.split(", ")
                        args_no_quote = [arg.strip('"') for arg in arguments]
                        str_args = " ".join(arg for arg in args_no_quote)
                        str_args = cls_name + " " + str_args
                        if command == "all":
                            self.do_all(str_args)
                        elif command == "show":
                            self.do_show(str_args)
                        elif command == "update":
                            self.do_update(str_args)
                        elif command == "destroy":
                            self.do_destroy(str_args)
                        elif command == "count":
                            self.do_count(str_args)
                        else:
                            print("** unknown command **")
                else:
                    print("** unknown command **")
            else:
                print("** unknown command **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
