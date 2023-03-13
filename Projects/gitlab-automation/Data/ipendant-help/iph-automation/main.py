# This is a sample Python script.
from config import Config

import gitlab


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

## Story 102 - Make a label init to make all the same labels in the corresponding proejcts

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Todo:
# Class to group up the projects you need or a task based on where you can set up the three tasks

# Change every iteration
IPH_ITERATION=f'19'

# Custom Project Configuration & Formatting

## Iteration
IPH_ITERATION_SUFFIX='i'
IPH_ITERATION_NAME=f'{IPH_ITERATION}{IPH_ITERATION_SUFFIX}'

## Branch Name
IPH_BRANCH_NAME_PREFIX = "story/"
IPH_BRANCH_NAME = f'{IPH_BRANCH_NAME_PREFIX}{IPH_ITERATION_NAME}-updates-edoc-ipendant-help'



class MergeRequestTask:

    def __init__(self, project):

        self.Project = project

        _BranchUser = 'angelo.savich'
        _BranchVersion = 'v10.13'
        _BranchPrefix = f'user/{_BranchUser}/{_BranchVersion}/'
        self.BranchSource = f'{_BranchPrefix}update-help-edoc-18'

        _ReleaseTarget = 'prerelease'
        self.BranchTarget = f'{_BranchVersion}/{_ReleaseTarget}'

    def Run(self):
        # self.Project.branches.create({'branch': self.BranchSource, 'ref': self.BranchTarget})

        Assignee= 64   # '@krasny.darren.fac'
        Reviewer= 61 # '@merchant.daniel.fac'

        _BranchVersion = 'v10.13'

        Title= f'18i - Updates iPendant Help for {_BranchVersion}'

        mr =  self.Project.mergerequests.create({'source_branch': self.BranchSource,
                                           'target_branch': self.BranchTarget,
                                           'title': 'Brake Check Screen',
                                           # 'labels': ['label1', 'label2'],
                                                 'assignee_id': Assignee,
                                                 'approver_ids': [Reviewer]
                                                 })


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def create_branch(project, branch_name, ref):
    project.branches.create({'branch': branch_name, 'ref': ref})

def create_merge_request():
    pass

def connect():


    gl = gitlab.Gitlab(url=Config.url_gitlab, private_token=Config.gitlab_access_token)
    gl.auth()
    gl.enable_debug()

    issues_ngc = gl.projects.get(252)
    edoc = gl.projects.get(548)
    controller = gl.projects.get(269)

    task = MergeRequestTask(controller)
    task.Run()
    #
    # label_ipendant_help_automation = issues_ngc.labels.get("Automation | iPendant Help")
    # issues = issues_ngc.issues.list(labels=[label_ipendant_help_automation.get_id()])
    # print(issues)
    #
    # whitelist = [1637]
    # next_build = "4"
    # # for issue in issues:
    #
    # target_branch = f'user/product.information.service/story/4'
    # # edoc_branch = edoc.branches.create({'branch': target_branch,
    # #                               'ref': 'v10.10/prerelease'})
    #
    # mr = edoc.mergerequests.create({'source_branch': target_branch,
    #                                    'target_branch': 'v10.10/prerelease',
    #                                    'title': 'Brake Check Screen',
    #                                    'labels': ['label1', 'label2']})
    # controller_branch = controller.branches.create({'branch': f'user/product.information.service/story/4',
    # #                                'ref': 'v10.10/prerelease'})

def get_issue(url, token, args):
    pass


if __name__ == '__main__':
    connect()