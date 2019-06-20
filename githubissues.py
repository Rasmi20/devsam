# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:58:30 2019

@author: 163437
"""

from github import Github


# using username and password
g = Github("Rasmi20", "Rojaqayyum31")

#repositorr_name
#repository = organization.get_repo(repository_name)

# or using an access token
#g = Github("access_token")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
#g = Github(base_url="https://{hostname}/api/v3")

#List repository for user
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

#List Lables for speciific  project
#repo = g.get_repo("d83arun/kibana")
repo = g.get_repo("Hygieia/Hygieia")
labels = repo.get_labels()
for label in labels:
    print(label)


#get git logs

    

#List Branched for specific repo
print(list(repo.get_branches()))


#List overall commits for repo and Files for specific commits
print('commits')
commits = repo.get_commits()
for commit in commits[:10]:
    print(commit)
    print(commit.files)
    print('etag ',commit.etag)
    print('comments ' , commit.get_comments())

#List comments  for repo    
comments = repo.get_comments()
for comment in comments:
    print('repo comment', comment)


#List commits for specific Branch

branches = list(repo.get_branches())
for branch in branches:
    c = branch.commit.sha
    print('branch commit', c)
    
    branch_commits = repo.get_commits(sha=c)
    print('branch commits',branch_commits)
    
    for branch_commit in branch_commits[:10]:
        print('Branch Commit',branch_commit)
        print('Branch Commit Files',branch_commit.files)
        print('Branch commit etag ',branch_commit.etag)
        print('Branch  commit comments ' , branch_commit.get_comments())
        print('Branch  commit total comments Count ' , branch_commit.get_comments().totalCount)
        for branch_comment in branch_commit.get_comments():
            print('branch comment', branch_comment)
    


