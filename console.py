#!/usr/bin/python3
"""
Defines the HBNB console.
"""
from ast import parse
import cmd
import models
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface for interacting
    with an Airbnb application console.

    Args:
        cmd (cmd.Cmd, optional): This is the base class from the `cmd` module
                                 that provides functionalities for building
                                 command-line interfaces.
                                 Inheriting from `cmd.Cmd` allows this class
                                 to define
                                 commands and handle user input for the
                                 Airbnb console.
                                 Defaults to None (automatically inherited).
    """
    prompt = "(hbnb) "

    def precmd(self, line):
        """
        Override the precmd method to split the command line into arguments
        and strip trailing whitespace from each argument before executing
        any command.
        """
        if not line.strip():
            print("** empty input **")
            return ''

        args = line.split()
        processed_args = [arg.rstrip() for arg in args]
        return ' '.join(processed_args)

    def do_quit(self, args):
        """
        quits when prompted
        """
        exit()

    def do_EOF(self, args):
        """
        EOF signal to exit the program.
        """
        exit()

    def do_create(self, obj_type):
        """
        Creates an instance.
        """
        if obj_type == "" or obj_type is None:
            print("** class name missing **")
        elif obj_type not in storage.classList():
            print("** class doesn't exist **")
        else:
            new_obj = storage.classList()[obj_type]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classList():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classList():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classList():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classList():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, arg):
        """
        Update a class instance based on the class name and id by adding
        or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in storage.classList():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = ' '.join(args[3:])

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** can't update id, created_at, or updated_at **")
            return

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
