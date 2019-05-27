import os

def find_files(suffix, path):
    if suffix == None:
        print("Invalid suffix")
        return
    return find_files_func(suffix, path, [])

def find_files_func(suffix, path, list):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    for entry in os.listdir(path):
        complete_path = os.path.join(path, entry)
        # Base case
        if os.path.isfile(complete_path):
            if complete_path.endswith(suffix):
                list.append(complete_path)
        elif (os.path.isfile(complete_path) == False):
            find_files_func(suffix, complete_path, list)
    
    return list

print()
print("Print all .c")
print(find_files(".c", "testdir"))
print()
print("Print all the .h")
print(find_files(".h", "testdir"))
print()
print("Print all the files")
print(find_files("", "testdir"))
print()
# Edge case None
print(find_files(None, "testdir"))
print()
