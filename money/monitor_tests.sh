#!/bin/bash
# Runs tests when files change, and displays result in a floating window.
# This requires:
# 1) libnotify-bin Debian/Ubuntu package
# 2) nose Python package
# 3) nose-gnome-notify Python package
#      http://code.google.com/p/nose-gnome-notify/
# 4) tdaemon.py Python script
#      https://github.com/brunobord/tdaemon

tdaemon.py --custom-args "--with-nosegnomenotify"
