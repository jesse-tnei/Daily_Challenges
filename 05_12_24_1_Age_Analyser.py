import os
import datetime

path_to_project = r"N:\Bute Energy\16193 - Stage 3 Workshop (Bute Energy)"
files = os.listdir(path_to_project)
print(
    files)  # Returns ['5 - Model', '1 - Admin', '2 - Client Data', '7 - Reports', '8 - Deliverables', '6 - Results', '4 - Calculations', '3 - Data']

# Trying to obtain the information in the first folder
path_to_folder_one = os.path.join(path_to_project, files[0])
print(path_to_folder_one)

# First we check to confirm if it's a folder
if os.path.isdir(path_to_folder_one):
    print('True')  # This prints out True
    info_of_files_in_folder = os.stat(path_to_folder_one)
    print(f'Info in folder: {info_of_files_in_folder}')
    # Returns: Info in folder: os.stat_result(st_mode=16895, st_ino=3868308, st_dev=1311684943, st_nlink=1, st_uid=0,
    # st_gid=0, st_size=0, st_atime=1733420537, st_mtime=1731491397, st_ctime=1695113152)
    # These are the properties that we can retrieve for folders. Refer to documentation for what each of them means

    # Next, we check and see what files we have within that directory
    files_in_folder_one = os.listdir(path_to_folder_one)
    path_to_files_in_folder_one = [os.path.join(path_to_folder_one, file) for file in files_in_folder_one]
    print(f'Files: {files_in_folder_one}')
    print(path_to_files_in_folder_one)

    # Check if all the files are files or if some of them are folders
    folder_check = [os.path.isdir(file_in_folder_one) for file_in_folder_one in files_in_folder_one]
    print(folder_check)  # returns [False, False, False, False, False, False] meaning all of them are folders

    # Let's check further into the first folder
    most_recent_access_time = [os.stat(file).st_atime for file in path_to_files_in_folder_one]
    print(most_recent_access_time)
    print(type(most_recent_access_time[0])) #This returned a float

    # Now we need to convert this into a proper date time format

    #First we sort out to find out the latest time
    most_recent_access_time.sort()
    print(most_recent_access_time)
    # Then we convert it into normal time
    normal_times = [datetime.datetime.fromtimestamp(item) for item in most_recent_access_time]

    # Now we can print the most recent time
    print(normal_times[0])

