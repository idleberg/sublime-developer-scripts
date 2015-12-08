# brew-install.py (via https://github.com/idleberg/sublime-developer-scripts)

import os, sublime, sublime_plugin, subprocess

# Array of required Brew packages
packages = [

]

def conf_error(me):
    sublime.error_message("No packages specified in config")

def brew_error(me):
    import sys, webbrowser

    if sublime.ok_cancel_dialog("Some package dependencies could not be installed automatically. Please refer to the installation guide to resolve this problem.\n\nDo you want to open the website for this package?", "Open website"):
        webbrowser.open("https://packagecontrol.io/packages/"+me)
    sys.exit()

def plugin_loaded():
    from package_control import events
    from subprocess import check_call

    # Get name of package folder
    me = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

    package_dir = sublime.packages_path() + '/' + me

    for package in packages:
        if package:

            try:
                os.chdir(package_dir)
                sublime.status_message("[%s] brew install %s" % ( me, package))
                check_call(['brew', 'install',  package])
                sublime.status_message("[%s] Completed" % me)

            except subprocess.CalledProcessError:
                brew_error(me)

        else:
            conf_error(me)
    else:
        conf_error(me)