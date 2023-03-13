import os

# Cli Command that reads the gitlab url, key, and scope (group or project) out of a config and builds a .resource class file that has the storngly typed properties so you can do gitlabinstance.fanuc.issues-ngc

# You can then do one for projects (issues, merge requests, scripts, labels), groups (labels, etc),syncing across multiple groups and projects (issues and merge requests and branches)
import gitlab
from git import Repo

from Config import Config

gl = gitlab.Gitlab(url=Config.url_gitlab, private_token=Config.gitlab_access_token)

if Config.Runtime.Mode:
    gl.auth()
    gl.enable_debug()


class BranchTask:
    # Dependent Configuration
    # - Custom Project Configuration

    # Custom Task Configuration:
    # - Project
    # - Version
    # - BranchPrefix
    #   - BranchVersion
    #   - BranchPrefix


    def __init__(self, project, version, story):
        self.Project = project

        _BranchVersion = version
        _BranchUser = 'angelo.savich'
        _BranchPrefix = f'user/{_BranchUser}/{_BranchVersion}/'
        self.BranchSource = f'{_BranchPrefix}{story}-update-help-edoc'

        _ReleaseTarget = 'prerelease'
        self.BranchTarget = f'{_BranchVersion}/{_ReleaseTarget}'

    def Run(self):
        self.Project.branches.create({'branch': self.BranchSource, 'ref': self.BranchTarget})

class MergeRequestTask:

    def __init__(self, project, version, story):
        self.Project = project

        self._BranchVersion = version
        _BranchUser = 'angelo.savich'
        _BranchPrefix = f'user/{_BranchUser}/{self._BranchVersion}/'
        self.BranchSource = f'{_BranchPrefix}{story}-update-help-edoc'

        _ReleaseTarget = 'prerelease'
        self.BranchTarget = f'{self._BranchVersion}/{_ReleaseTarget}'

        self.Title=None
    def SetTitle(self, title):
        self.Title = title
    def Run(self):
        # self.Project.branches.create({'branch': self.BranchSource, 'ref': self.BranchTarget})

        Assignee= 64   # '@krasny.darren.fac'
        Reviewer= 61 # '@merchant.daniel.fac'

        self.Title = self.Title if self.Title else f'Updates iPendant Help Screens' # for {self._BranchVersion}'

        mr =  self.Project.mergerequests.create({'source_branch': self.BranchSource,
                                           'target_branch': self.BranchTarget,
                                           'title':  self.Title,
                                           'labels': ['Automation | iPendant Help'],
                                                 'assignee_id': Assignee,
                                                 'reviewer_ids': [Reviewer]
                                                 })


class CLI:
    def Start(self):
        # list all the projects
        projects = gl.projects.list(iterator=True)
        for project in projects:
            print(project.name_with_namespace, flush=True)



    def Run_IPH(self):
        # gl = gitlab.Gitlab(url=Config.url_gitlab, private_token=Config.gitlab_access_token)



        DATA_EDOC = './Data/ipendant-help/edoc'
        # Get Branch
        # Repo.clone_from('git@gitlab.one.fanuc.com:fac/facrd/edoc.git',  os.path.join("./Data/ipendant-help/edoc"), branch="V10.10/prerelease")

        # Go through each help screen folder
        # If it's a new screen, add in the database a new column with a new UUID and add the help_id for the screen.
            # Theres a new UUID for each help screen path & h actually think about this more... just need it to build easy.


        # Get Project
        #########################
        edoc = gl.projects.get(548)

        # Merge Request - edoc
        #########################
        version = 'v10.10'
        story='1637'

        # Make branch
        task = BranchTask(edoc, version, story)
        task.Run()

        # Make Request
        task = MergeRequestTask(edoc, version, story)
        task.SetTitle('Fixes Brake Check Screen - Help Id Mismatch')
        task.Run()

        issues_ngc = gl.projects.get(252)
        controller = gl.projects.get(269)

