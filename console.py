#!/usr/bin/python3
"""Defines HBNB Console"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb)'
    __classes = ["BaseModel"]
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class_name>
        """
        args = split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval("{}()".format(args[0]))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        Usage: show <class_name> <id>
        """
        args = split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = ("{}.{}".format(args[0], args[1]))
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes Instance by class name and id
        Usage: destroy <class_name> <id>
        """
        args = split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = ("{}.{}".format(args[0], args[1]))
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances
        Usage: all <class_name>   OR       all <>
        """
        args = split(arg)
        objects = storage.all()
        if not args:
            print([str(objects[key]) for key in objects])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if args[0] == key.split('.')[0]])

    def do_update(self, arg):
        """updates the instance
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = ("{}.{}".format(args[0], args[1]))
            obj = storage.all()[key]
            attr_name = args[2]
            attr_value = args[3]
            setattr(obj, attr_name, attr_value)
            obj.save

            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
