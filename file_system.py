"""
File:    file_system.py
Author:  Sina Roomi
Date:    12/11/2022
Section: 43
E-mail:  sinar1@umbc.edu
Description:
  This program mimics a command prompt and recreates it base operations like
  ls, cd, mkdir,etc. 
"""
"""
    Description:
      
    :param:
    :param:
    :return:
"""


def pwd(current_location):
    """
    Description:
      Displays the current spot the user is in and removes 
      any periods that the user doesn't need to see
    :param: current_location: Where the user is currently in the file_system
    :return: a path that is readable for the user
    """
    
    new_location = current_location.split(".")
    new_location = "".join(new_location)
    return new_location

def find_last_directory(current_path, my_file_system):
    """
    Description:
      The function takes a path and finds the last
      directory
    :param: path: the current path the user is in
    :param: my_file_system: The whole file system
    :return: the directory at the end of the path
    """
    result = my_file_system
    for dir in current_path:
        result = result[dir]
    return result

    first_spot = my_file_system[location[0]]
    location.remove(location[0])
    for key in location:
        first_spot = first_spot[key]
    return first_spot

def mkdir(name, current_path, my_file_system):
    """
    Description:
      The function takes the user's current location in the file_system
      and creates a new directory with the name provided by the user
    :param: name: the name the user wants the directory to be called
    :param: current_path: the current path the user is in
    :param: my_file_system: The whole file system
    :return:
    """
    dict_name = f"{name}/"
    location = current_path.split(".")
    if location[-1] == "/":
        my_file_system["/"][dict_name] = {}
    else:
        last_spot = find_last_directory(location, my_file_system)
        last_spot[dict_name] = {}


def ls_v2(a_directory):
    """
    Description:
      Finds all the keys in a given directory
    :param: a_directory: any directory
    :return: all keys in that directory
    """
    return a_directory.keys()

def printLs(a_list, full_path):
    """
    Description:
      prints out all data from a list and also displays
      the full path of where that data is from
    :param: a_list: a list with keys
    :param: full_path: absolute path to the directory that the keys are from
    """ 
    print(f"Contents of {pwd(full_path)}")
    for i in a_list:
        if i[-1] == "/":
            print(i[:-1])
        else:
            print(i)


def validate_user_path(path):
    """
    Description:
      Checks if the path is a correct length and removes any foward slash
      from the end of the path
    :param: path: a path 
    :return: either a corrected path or the orginal path if it needed no changes
    """
    if not len(path) == 0 and path[-1] == "/":
        return path[:-1]
    return path  


def parse_user_input(user_input):
    """
    Description:
      Takes a path and parses it in so that it is usalbe
    :param: user_input: a path that was provide by the user
    :return: a path that is usable for other functions
    """
    user_path = user_input.split("/")
    for i in range(len(user_path)):
        if user_path[0] == "":
            user_path[i] = str(user_path[i]) + "/"
        else:
            user_path[i] = "." + str(user_path[i]) + "/"
    return "".join(user_path)

    
def convert_relative_path_to_absolute_path(relative_path,current_path):
    """
    Description:
      When given a relative path, the function takes the current path and adds
      the relative to it
    :param: relative_path: relative_path provided by the user
    :param: current_path: where the user is current is in
    :return: the updated path
    """
    return current_path + relative_path
    

def user_Ls(argument, current_location):
    """
    Description:
      Takes a argument from the user, either a "", a relative path, or a absolute path.
      The function then prints either the keys in the current path or the keys in the path
      the user wants to look at.
    :param: argument: the user's input
    :param: current_location: where the user is current in
    :return: prints out all the keys in the directory that the user wanted
    """
    if argument == "":
        curr = current_location.split(".")
        cur_dir = find_last_directory(curr, my_file_system)
        printLs(ls_v2(cur_dir), current_location)
    else:
        new_path = validate_user_path(argument)
        new_path = parse_user_input(new_path)
        if new_path[0] != "/":
            new_path = convert_relative_path_to_absolute_path(new_path, current_location)
        curr = new_path.split(".")
        cur_dir = find_last_directory(curr, my_file_system)
        printLs(ls_v2(cur_dir), new_path)


def cd(argument , current_location , my_file_system):
    """
    Description:
      When the user types cd, the function first checks to see if the argument is a (/),(..),
      or if it has (txt) in the name. Then the function checks to see the directory that the user
      wants to go in exist and if it does, the current_location changes to where the user wanted to
      go. The function also can take a relative or absolute path and change directories.
    :param: argument: the user's input
    :param: current_location: where the user is current in
    :my_file_system: The entire file_system
    :return: an updated current_location
    """
    if argument == "/":
       current_location = f"/"
       return current_location
    elif argument == "":
        return current_location
    elif argument == "..":
        location = current_location.split(".")
        if len(location) > 1:
            location = location[:-1]
            current_location = ".".join(location)
            return current_location
        else:
            print("Can't go further back than this.")
            return current_location
    elif ".txt" in argument:
        print("Can't cd into a txt file.")
        return current_location
    elif len(argument.split("/")) > 1:
        return cd_with_path(argument, current_location)
    else:
        #checks if / is in the name. If not, adds / to the end of the name
        if argument[-1] != "/":
            argument = f"{argument}/"
        list_of_keys = list(my_file_system["/"].keys())
        if argument[-1] == "/" and argument in list_of_keys:
            current_location += f".{argument}"
            return current_location
        
        location = current_location.split(".")
        last_spot = find_last_directory(location, my_file_system)
        if argument[-1] == "/" and argument in last_spot.keys():
            current_location += f".{argument}"
            return current_location
        else:
            print(f"No such directory")
            return current_location


def cd_with_path(path, current_location):
    """
    Description:
      A helper function for the cd function. Takes a relative or absolute path and
      updates the current_location because of it.
    :param: path: a path 
    :param: current_location: where the user is current in
    :return: an updated current_location
    """ 
    new_path = parse_user_input(validate_user_path(path))
    if path[0] == "/":
        current_location = new_path
        return current_location
    if new_path[0] != "/":
        new_path = convert_relative_path_to_absolute_path(new_path, current_location)
        current_location = new_path
        return current_location


def touch(name,current_location, my_file_system):
    """
    Description:
      Takes the user's current_location and creates a text file with the name provide
    :param: name: name of the file
    :param: current_location: where the user is currently located in
    :param: my_file_system: the entire file system
    """
    file_name = name
    if ".txt" not in file_name:
        file_name += ".txt"
        
    location = current_location.split(".")
    if location[-1] == "/":
        my_file_system["/"][file_name] = ""
    else:
        last_spot = find_last_directory(location, my_file_system)
        last_spot[file_name] = ""

def rm(name, current_location, my_file_system):
    """
    Description:
      Takes the name the user provided and first checks to see if the file with that
      name exists, and if it does, removes that file from the directory
    :param: name: name of the file
    :param: current_location: where the user is currently located in
    """

    file_to_remove = name
    check_file = file_to_remove.split(".")
    if "txt" in check_file:
        location = current_location.split(".")
        if location[-1] == "/" and file_to_remove in my_file_system["/"].keys():
            del my_file_system["/"][file_to_remove]
        elif location[-1] == "/" and file_to_remove not in my_file_system["/"].keys():
            print(f"{file_to_remove} not found.")
        else:
            last_spot = find_last_directory(location, my_file_system)
            find_keys = last_spot.keys()
            if file_to_remove in find_keys:
                del last_spot[file_to_remove]
            elif file_to_remove not in find_keys:
                print(f"{file_to_remove} not found.")
    else:
        print("Can't use rm for dictionaries.")


def isDirectory(name):
    """
    Description:
      Checks if a name is a directory or not
    :param: name: name of the directory
    :return: True or False if the name is a directory
    """
    return name[-1] == "/"

def locate(find_name, cur_dir):
    """
    Description:
      This function recursively searches for a file and returns the absolute
      location of every file that was found
    :param: find_name: name of the file to search for
    :param: cur_dir: the current directory the user is in
    :return: a list of paths
    """
    list_of_paths = []
    for key in cur_dir.keys():
        if isDirectory(key):
            path = locate(find_name, cur_dir[key])
            for file in path:
                list_of_paths.append(key+file)
        else:
            if find_name == key:
                list_of_paths.append(find_name)

    return list_of_paths

def print_locate():
    """
    Description:
      Calls the locate function and prints out the list of paths
    """
    if current_location == "/":
        system_to_use = my_file_system
    else:
        system_to_use = find_last_directory(current_location, my_file_system)

    find_file = locate(argument, system_to_use)
    if find_file:
        for i in find_file:
            print(i)
    else:
        print("No files were found.")


def ask_for_input():
    """
    Description:
      The function asks the user for input
    :return: a list of what the user typed
    """
    user_input = input("> ").strip()
    return user_input.split(" ")


def check_string(a_list):
    """
    Description:
      Checks if the user input from ask_for_input is valid for the program if not,
      it calls ask_for_input until it is valid
    :param: a_list: a list to check
    :return: returns the user input as a list 
    """
    if len(a_list) > 2:
        #check while loop
        while len(a_list) > 2 and len(a_list) < 1:
            a_list = ask_for_input()
    return a_list

if __name__ == '__main__':
    #Linux Shell/File System Manager (main program)
    #("/") is the root
    my_file_system = {
        "/": {
            
        }
    }    
    current_location = f"/"

    user_input = check_string(ask_for_input())
    argument = ""
    if len(user_input) > 1:
        argument = user_input[1]

    while user_input[0] != "exit":
        if user_input[0] == "pwd":
            print(pwd(current_location))
        elif user_input[0] == "mkdir":
            mkdir(argument , current_location , my_file_system)
        elif user_input[0] == "ls":
            user_Ls(argument, current_location)
        elif user_input[0] == "cd":
            current_location = cd(argument, current_location, my_file_system)
        elif user_input[0] == "touch":
            touch(argument, current_location, my_file_system)
        elif user_input[0] == "rm":
            rm(argument, current_location, my_file_system)
        elif user_input[0] == "locate":
            print_locate()
            
        user_input = check_string(ask_for_input())
        argument = ""
        if len(user_input) > 1:
            argument = user_input[1]