# git-clone.py (via https://github.com/idleberg/sublime-developer-scripts)

import os, sublime, sublime_plugin, subprocess

# Array of Git repositories
repositories = [

]

def conf_error(me):
    sublime.sublime.error_message("[%s] No repository specified" % me)

def git_error(me):
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
        if len(repositories) > 0:
            for repository in repositories:
                if repository:
                    try:
                        os.chdir(package_path)
                        repository_dir = os.path.basename(repository)

                        # git-pull if directory exists
                        if os.path.isdir(repository_dir):
                            os.chdir(repository_dir)
                            sublime.status_message("[%s] git pull" % me)
                            check_call(['git', 'pull', repository])

                        # git-clone
                        else:
                            sublime.status_message("[%s] git clone" % me)
                            check_call(['git', 'clone', repository])

                    except subprocess.CalledProcessError:
                        git_error(me)

                    sublime.status_message("[%s] Completed" % me)

                else:
                    conf_error(me)
        else:
            conf_error(me)