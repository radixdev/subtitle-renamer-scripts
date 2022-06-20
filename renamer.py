import os
import sys
import shutil
from glob import glob
from os.path import join
from os.path import basename
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

workingDir = str(sys.argv[1])
print("workingDir", workingDir)

# Verify we're in the right spot
subsDir = join(workingDir, "Subs")
if (not os.path.isdir(subsDir)):
  print(workingDir, "is not a directory with subtitles in it")
  sys.exit(1)

# Files that are 1 layer deep
movieFiles = glob(subsDir + "/*.srt")

# Files that are 2 layers deep
showFiles = glob(subsDir + "/**/*.srt")

# Gets the ISO code "en", "fr", etc.
# from the file basename
def getLangCode(filename):
  n = filename.lower()
  threshold = 0.6
  if (similar("eng.srt", n) > threshold):
    return "en"
  # Add other language codes here if you like
  return None

# Get the parent folder name as the fallback option!
workingDirBasename = basename(workingDir)

# Check that a file with this name actually exists in the folder
def filter_movie_extensions(filepath):
  exts = [".mp4" , ".mkv", ".mov"]
  return os.path.splitext(filepath)[1] in exts

# Check if a file with the parent dir name in
# the title and a video file extension afterwards.
#
# e.g. for checkedName = "AVENGERS.1080p"
# "C/dir/to/movie/AVENGERS.1080p/" and a
# "C/dir/to/movie/AVENGERS.1080p/AVENGERS.1080p.mp4"
# right afterwards
def does_working_dir_contains_matching_media(checkedName):
  movieSeemingFiles = filter(filter_movie_extensions, glob(workingDir + "/" + checkedName + ".*"))
  return len(list(movieSeemingFiles)) > 0

# Fix the movie files
# C/dir/to/movie/AVENGERS.1080p/
#   AVENGERS.1080p.mp4
#   Subs
#       2_English.srt
if (does_working_dir_contains_matching_media(workingDirBasename)):
  for filePath in movieFiles:
    print("on movie file", filePath)
    movieBaseName = basename(filePath)
    langCode = getLangCode(movieBaseName)
    if (langCode is None):
      print("Can't determine language code for =>", movieBaseName)
      next
    # print("langCode", langCode)

    # do the file move
    newFile = join(workingDir, workingDirBasename + "." + langCode + ".srt")
    print("performing copy")
    print (filePath)
    print ("------>")
    print (newFile)
    shutil.copyfile(filePath, newFile)

    # Don't move more than the first file!
    break
else:
  print("This is not a movie directory", workingDir)

# Fix the TV show files
# C/dir/to/show/PENTHOUSE.1080p/
#   PENTHOUSE.S01E01.1080p.mp4
#   Subs
#     PENTHOUSE.S01E01.1080p
#       2_English.srt