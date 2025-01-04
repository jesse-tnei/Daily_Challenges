import os
import datetime

# We add the file path to the parent directory in read more (r at beginning)
# The r prevents the system from reading the backslash as a different instruction e.g., \n which would mean next time
path_to_project = r"N:\Bute Energy\16193 - Stage 3 Workshop (Bute Energy)"

def folder_creation_time_check(path):
    # Using the path, we obtain the paths to the specific items within the folder
    # Note that os.listdir produces a list of the items in the parent folder
    # Then os.path.join concatenates the parent path with the item in the folder
    paths_to_items_in_parent_folder = [os.path.join(path_to_project, item) for item in os.listdir(path_to_project)]

    # Then we get the list of items in the first folder
    path_to_items_in_first_folder = [os.path.join(paths_to_items_in_parent_folder[0], item) for item in os.listdir(paths_to_items_in_parent_folder[0])]

    # We don't care if they are files or folders, we just want to see the most recently updated item in the first folder
    unix_modification_time = [os.stat(each_path).st_atime for each_path in path_to_items_in_first_folder]

    # Then we sort them out - the least integer comes first hence the earliest time first
    unix_modification_time.sort()

    # Then we convert these times to datetime format and print out the first and the last item
    sorted_time_in_datetime_format = [datetime.datetime.fromtimestamp(unix_time) for unix_time in unix_modification_time]
    print(f'Earliest modification is {sorted_time_in_datetime_format[0]}, while latest modification is {sorted_time_in_datetime_format[-1]}')

# Then we call the function
folder_creation_time_check(path_to_project)