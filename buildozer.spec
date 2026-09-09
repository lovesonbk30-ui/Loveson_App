[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets minimum Android SDK versions
android.minapi = 21
android.ndk = 25b

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (bool) If True, then skip trying to update the Android sdk
# Very useful to avoid long downloads during GitHub Actions builds
android.skip_update = False

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) The Android arch to build for
# armeabi-v7a for older 32-bit devices, arm64-v8a for modern 64-bit phones
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
