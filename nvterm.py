#!/usr/bin/env python
import argparse
import os
import re
import sys
import fileinput

def getAllFiles(directory, fileExtention=".txt"):
  fileList = []
  for top, dirs, files in os.walk(directory):
    for nm in files:
      if nm.endswith(fileExtention):
        fileList.append(nm) 
  return fileList

# this is to help with cross compatibility between platforms
def getHomeDir():
  if re.match("linux.*", sys.platform) is not None:
    return os.getenv("HOME")

def searchFileNames(fileList, searchString):
  # Uses an unmatched list and a match list because once a file is matched, there is no
  # reason to search it again.
  unmatchedList = []

  matchedList = fileList[0]
  if fileList[0] == "":
    matchedList = []

  for filename in fileList[1]:
    if re.match(".*{}.*".format(searchString), filename, flags=re.DOTALL) is not None:
      matchedList.append(filename)
    else:
      unmatchedList.append(filename)
  return [matchedList, unmatchedList]

def searchFileContents(directory, fileList, searchString):
  unmatchedList = fileList[1]
  matchedList = fileList[0]
  if fileList[0] == "":
    matchedList = []

  fullpathnames = []
  for filename in fileList[1]:
    fullpathnames.append(os.path.join(directory, filename))
  
  completeFiles = fileinput.input(fullpathnames)
  for line in completeFiles:
    if re.match(".*{}.*".format(searchString), line, flags=re.DOTALL) is not None:
      matchedItem = re.sub(re.escape(directory + "/"), "", completeFiles.filename())
      matchedList.append(matchedItem)
      unmatchedList.remove(matchedItem)
      completeFiles.nextfile()

  return [matchedList, unmatchedList]

# Setup the argument list.
parser=argparse.ArgumentParser(description="search a Notes directory for a string")
# Optional argument to change from the default notes directory
parser.add_argument("-d, --directory", dest="directory", default="~/Dropbox/Notes",
                    help="The directory where the notes are stored (~/Dropbox/Notes by" +
                    "default) ")
parser.add_argument("-e, --editor", dest="editor", default="gvim", help="The editor to " +
                    "to use (the default is gvim)")

# Argument of what to search for
parser.add_argument('search_string', help="The string to search for")
args = parser.parse_args()

# Handle the ~ for home dir
args.directory = re.sub("~", getHomeDir(), args.directory)

# The format for files is [[Matched],[Unmatched]]
files = ["", getAllFiles(args.directory)]
files = searchFileNames(files, args.search_string)
files = searchFileContents(args.directory, files, args.search_string)

# open up the files with the editor
if files[0] is not "":
  if type(files[0]) is list:
    for filename in files[0]:
      os.system('{} "{}"'.format(args.editor, os.path.join(args.directory, filename)))
  else:
    os.system('{} "{}"'.format(args.editor, os.path.join(args.directory,filename)))
