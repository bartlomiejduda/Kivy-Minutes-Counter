[app]

# (str) Title of your application
title = Minutes Counter

# (str) Application versioning (method 1)
version = 0.4

# (str) Package name
package.name = minutescounter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.duda

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==1.11.1

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
presplash.filename = %(source.dir)s/splash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
author = © Bartlomiej Duda

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.11.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
#android.permissions = INTERNET

# (int) Android API to use
android.api = 27

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 28

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /home/kivy/Android/android-ndk-r17c/

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /home/kivy/Android/android-sdk-28/



# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.arch = armeabi-v7a

#
# Python for android (p4a) specific
#

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
p4a.source_dir = /home/kivy/Repos/python-for-android/




[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

