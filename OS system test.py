import os
from datetime import datetime

#//shows current directory
##print(os.getcwd())

#/changes directory
os.chdir('/Users/xanderrutherford-parish/Desktop/')

#/ shows all files in current directory (try puting it in a list to search for files)
#print(os.listdir())

#/makes files in current directory
#os.mkdir("OS_TESTING_FILE")

#/same as before but also addes a sub file
#os.makedirs("OS_TESTING_FILE/SUB_TESTING")

#/same as os.makedirs and mkdir but its for deleting files
#os.rmdir("file name")
#os.removedirs("file names")

#/renames files found in current directory
#os.rename("OS_TESTING_FILE","NEW_OS_TESTING_NAME")


#/ prints out stats of the file (look up what the different stats mean
#print(os.stat("OS_TESTING_NAME"))

#/ prints a files statistic for time last modified in an understandable manner
#mod_time = os.stat("OS_TESTING_NAME").st_mtime
#print(datetime.fromtimestamp(mod_time))


#/ goes down the whole tree of the directory and shows all files, files in them,
#/ and all the paths to get to that files. (video says its good for finding file locations)
for dirpath, dirnames, filenames in os.walk('/Users/xanderrutherford-parish/Desktop/App'):
    print("current Path", dirpath)
    print("Directories", dirnames)
    print("files", filenames)
    print()
