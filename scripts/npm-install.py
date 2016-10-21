# npm-install.py (via https://github.com/idleberg/sublime-developer-scripts)

import os, sublime, sublime_plugin, subprocess

# Array of required Node packages
packages = [
    
]

def conf_error(me):
    sublime.error_message("No packages specified in config")

def npm_error(me):
    import sys, webbrowser

    if sublime.ok_cancel_dialog("Some package dependencies could not be installed automatically. Please refer to the installation guide to resolve this problem.\n\nDo you want to open the website for this package?", "Open website"):
        webbrowser.open("https://packagecontrol.io/packages/"+me)
    sys.exit()

def plugin_loaded():
    from package_control import events
    from subprocess import check_call

    # Get name of package
    me = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

    if events.install(me) or events.post_upgrade(me):

        # Get absolute package path
        package_path = sublime.packages_path() + '/' + me

        # Install packages specified in the array
        if len(packages) > 0:
            for package in packages:
                if package:
                    try:
                        os.chdir(package_path)
                        sublime.status_message("[%s] npm install -g %s" % ( me, package))
                        check_call(['npm', 'install', '-g',  package])
                        sublime.status_message("[%s] Completed" % me)

                    except subprocess.CalledProcessError:
                        npm_error(me)

                else:
                    conf_error(me)

        # Install packages from package.json
        elif len(packages) is 0 and os.path.isfile(package_path + "/package.json"):

            try:
                os.chdir(package_path)
                sublime.status_message("[%s] npm install" % me)
                check_call(['npm', 'install', '-g', '--production'])
                sublime.status_message("[%s] Completed" % me)

            except subprocess.CalledProcessError:
                npm_error(me)