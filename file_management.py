import os

# read all the files in a folder
# INPUT: folder - the folder to read the files from
#        verbose - if True, prints the name of each file
# OUTPUT: a list of files in the folder
def read_files_in_folder(folder, verbose=False):
    files = os.listdir(folder)
    if verbose:
        for file in files:
            print("Found file: " + file)
    if verbose:
        print("Found " + str(len(files)) + " files")
    return files

# read all the files in a folder with a specific extension
# INPUT: folder - the folder to read the files from
#        extension - the extension to look for
#        verbose - if True, prints the name of each file
# OUTPUT: a list of files in the folder with the extension
def read_files_in_folder_with_extension(folder, extension, verbose=False):
    files = os.listdir(folder)
    files_with_extension = []
    for file in files:
        if file.lower().endswith("." + extension.lower()):
            files_with_extension.append(file)
            if verbose:
                print("Found file: " + file)
    if verbose:
        print("Found " + str(len(files_with_extension)) + " files with extension " + extension)
    return files_with_extension

# delete a list of files in a folder
# INPUT: input_folder - the folder to delete the files from
#        files - the list of files to delete
#        verbose - if True, prints the name of each file
# OUTPUT: the number of deleted files
def delete_files_in_folder(input_folder, files, verbose=False):
    count = 0
    for file in files:
        os.remove(input_folder + file)
        count += 1
        if verbose:
            print("Deleted file: " + file)
    if verbose:
        print("Deleted " + str(count) + " files")
    return count

# strip a list of files of their extensions
# INPUT: files - the list of files to strip
#        verbose - if True, prints the name of each file
# OUTPUT: a list of files without extensions
def strip_extensions(files, verbose=False):
    stripped_files = []
    for file in files:
        stripped_files.append(file.split(".")[0])
        if verbose:
            print("Stripped file: " + file)
    if verbose:
        print("Stripped files: " + str(stripped_files))
    return stripped_files

# add a list of extensions to a list of files
# INPUT: files - the list of files to add extensions to
#        extensions - the list of extensions to add
#        verbose - if True, prints the name of each file
# OUTPUT: a list of files with extensions
def add_extensions(files, extensions, verbose=False):
    extended_files = []
    for file in files:
        for extension in extensions:
            extended_files.append(file + "." + extension)
            if verbose:
                print("Added extension: " + file + "." + extension)
    if verbose:
        print("Extended files: " + str(extended_files))
    return extended_files

# apply .lower() on a list of files
# INPUT: files - the list of files to apply .lower() on
#        verbose - if True, prints the name of each file
# OUTPUT: a list of files with .lower() applied
def lower_files(files, verbose=False):
    lower_files = []
    for file in files:
        lower_files.append(file.lower())
        if verbose:
            print("Lowered file: " + file)
    if verbose:
        print("Lowered files: " + str(lower_files))
    return lower_files

# read files with a specific extension from a folder, strip of their extensions, add extensions, and delete the ones with the new extensions in another folder
# INPUT: input_folder - the folder to read the files from
#        input_extension - the extension to look for
#        output_extensions - the list of extensions to add
#        target_folder - the folder to delete the files from
#        verbose - if True, prints the name of each file
# OUTPUT: Number of deleted files
def read_strip_add_delete_in_list(input_folder, input_extension, target_folder, output_extensions, verbose=False):
    files = read_files_in_folder_with_extension(input_folder, input_extension, verbose)
    stripped_files = strip_extensions(files, verbose)
    extended_files = add_extensions(stripped_files, output_extensions, verbose)
    extended_files_lower = lower_files(extended_files, verbose)
    return delete_files_in_folder(target_folder, extended_files_lower, verbose)


# read files with a specific extension from a folder, strip of their extensions, add extensions, and delete all the files that are not the newly created ones in a folder
# INPUT: input_folder - the folder to read the files from
#        input_extension - the extension to look for
#        output_extensions - the list of extensions to add
#        target_folder - the folder to delete the files from
#        verbose - if True, prints the name of each file
# OUTPUT: Number of deleted files
def read_strip_add_delete_not_in_list(input_folder, input_extension, target_folder, output_extensions, verbose=False):
    files = read_files_in_folder_with_extension(input_folder, input_extension, verbose)
    stripped_files = strip_extensions(files, verbose)
    extended_files = add_extensions(stripped_files, output_extensions, verbose)
    extended_files_lower = lower_files(extended_files, verbose)
    files_to_delete = read_files_in_folder(target_folder, verbose)
    files_to_delete_lower = lower_files(files_to_delete, verbose)
    files_to_delete = [file for file in files_to_delete_lower if file not in extended_files_lower]
    return delete_files_in_folder(target_folder, files_to_delete, verbose)

