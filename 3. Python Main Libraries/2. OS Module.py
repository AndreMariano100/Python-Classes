'''
The OS module in Python provides functions for interacting with the operating system.

Methods         Syntax / Description
chdir()         os.chdir(path) This method changes the current working directory to path.
getcwd()        os.getcwd() This method returns a string representing the current working directory.
mkdir()         os.mkdir(path) This method creates the directory named path. If the directory
                already exists, FileExistsError is raised.
remove()        os.remove(path) This method removes (deletes) the file path. If the path is a directory,
                OSError is raised. Use rmdir() to remove directories. In Windows,
                attempting to remove a file that is in use causes an exception to be
                raised; in Linux, the directory entry is removed but the storage
                allocated to the file is not made available until the original file is
                no longer in use.
rmdir()         os.rmdir(path) This method removes (deletes) the directory path. It only works
                when the directory is empty, otherwise, OSError is raised.
walk()          os.walk(top, topdown=True)
                This method generates the file names in a directory tree by walking
                the tree either top-down or bottom-up. For each directory in the
                tree rooted at directory top (including top itself), it yields a 3-tuple
                (dirpath, dirnames, filenames). The dirpath is a string, the path to
                the directory. The dirnames is a list of the names of the
                subdirectories in dirpath (excluding ‘.’ and ‘..’). The filenames is a
                list of the names of the non-directory files in dirpath. Note that the
                names in the lists contain no path components. To get a full path
                (which begins with top) to a file or directory in dirpath, do os.path.
                join(dirpath, name).
rename()        os.rename(old_name, new_name)
                This method is used to rename the file from old_name to new_name.
listdir()       os.listdir(path=‘.’) This method returns a list containing the names of the entries in the
                directory given by path. The list is in arbitrary order and does not
                include the special entries ‘.’ and ‘..’ even if they are present in the
                directory.


import os.path

Methods             Syntax Description
join()              os.path.join(path, *paths) This method is used to join one or more path components
                    intelligently. The return value is the concatenation of path and any
                    members of *paths with exactly one directory.
exists()            os.path.exists(path) This method returns True if path refers to an existing path else returns
                    False for broken links.
isfile()            os.path.isfile(path) This method returns True if path is an existing regular file.
isdir()             os.path.isdir(path) This method returns True if path is an existing directory.
getmtime()          os.path.getmtime(path) This method returns the time of last modification of path.
abspath()           os.path.abspath(path) This method returns a normalized absolutized version of the
                    pathname path.
path.isabs()        os.path.isabs(path) This method returns True if path is an absolute pathname.
relpath()           os.path.relpath(path, start=os.curdir)
                    This method returns a relative filepath to path either from the current
                    directory or from an optional start directory.
dirname()           os.path.dirname(path) This method returns the directory name of the pathname path.
basename()          os.path.basename(path) This method returns the base name of pathname path.
split()             os.path.split(path) This method splits the pathname path into a pair, (head, tail) where
                    the tail is the last pathname component and the head is everything
                    leading up to that. The tail part will never contain a slash; if path
                    ends in a slash, the tail will be empty. If there is no slash in the path,
                    the head will be empty. If the path is empty, both head and tail are
                    empty.
splitext()          os.path.splitext(path) This method splits the pathname path into a pair (root, ext) such that
                    root + ext == path where ext begins with a period and contains at
                    most one period and root is everything leading up to that.
getsize()           os.path.getsize(path) This method returns the size, in bytes, of path.
'''
import os

# Current working directory
print(os.getcwd())

# Change directory
os.chdir('C:\TEMP')
print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.name)