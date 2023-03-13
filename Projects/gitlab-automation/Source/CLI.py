

# Cli Command that reads the gitlab url, key, and scope (group or project) out of a config and builds a .resource class file that has the storngly typed properties so you can do gitlabinstance.fanuc.issues-ngc

# You can then do one for projects (issues, merge requests, scripts, labels), groups (labels, etc),syncing across multiple groups and projects (issues and merge requests and branches)
import gitlab
from Config import Config

gl = gitlab.Gitlab(url=Config.url_gitlab, private_token=Config.gitlab_access_token)

if Config.Runtime.Mode:
    gl.auth()
    gl.enable_debug()


class CLI:
    def Start(self):
        # list all the projects
        projects = gl.projects.list(iterator=True)
        for project in projects:
            print(project.name_with_namespace, flush=True)



    def Run_IPH(self):
        # gl = gitlab.Gitlab(url=Config.url_gitlab, private_token=Config.gitlab_access_token)

        issues_ngc = gl.projects.get(252)
        edoc = gl.projects.get(548)
        controller = gl.projects.get(269)