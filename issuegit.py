# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:16:03 2019

@author: 163437
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:58:30 2019

@author: 163437
"""

from github import Github
import json
import csv
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


# using username and password

g = Github("Rasmi20", "Rojaqayyum31")

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))


repo = g.get_repo("Hygieia/Hygieia")
tags = repo.get_tags()
for tag in tags[:10]:
    print('tag',tag)
labels = repo.get_labels()
for label in labels[:10]:
    print(label)


#List Branched for specific repo
print(list(repo.get_branches()[:10]))

#get Issues

issues = repo.get_issues()

issue_store = []


for issue in issues[:200]:
    issues_json=[]
#    print('issue body',issue.body)
#    print('issue No. of comments',issue.comments)
#    print('Comments',issue.get_comments())
    comments = issue.get_comments()
    issue_comment_list = []
    """
    for comment in comments:
        issue_comment = {}
        issue_comment['id'] = comment.id
        issue_comment['body'] = comment.body
        issue_comment['commented_by'] = comment.user.login
        #issue_comment_list.append(json.dumps(issue_comment))
        issue_comment_list.append(issue_comment)
#        print('issue_comment',comment)        
#        print ('issue comment id', comment.id)
#        print('issue comment body', comment.body)        
#        print('Login User', comment.user.login)
        """
    
       
    issues_json.append(issue_comment_list)
    issues_json.append(issue.body)
    issues_json.append(issue.id)
    issues_json.append(issue.number)
    issues_json.append(issue.title)
    issues_json.append(issue.created_at)
    issues_json.append(issue.updated_at)
    issues_json.append(issue.state)
    issues_json.append(issue.comments)
    with open('people1.csv', 'a') as csvFile:
       writer = csv.writer(csvFile) 
       writer.writerow(issues_json)
    #print('issues_json' , issues_json)

"""
    print('issue_comment',issue_comment)
        
    print('issue ID',issue.id)
    print('issue Number',issue.number)
    print('issue body',issue.body)
    print('issue title',issue.title)
    print('issue created at',issue.created_at)
    print('issue updated at',issue.updated_at)
    print('issue state', issue.state)
    
"""
pull_store = []

#list pull requests
pulls = repo.get_pulls()
for pull in pulls[:200]:
    
    pull_json={}
    pull_json['body'] = pull.body
    pull_json['id'] = pull.id
    pull_json['no_comments'] = pull.comments
    pull_json['no_commits'] = pull.commits

#    print('pull body' ,pull.body)
#    print('pull No. of changed files', pull.changed_files)
#    print('pull No. of comments' , pull.comments)
#    print('pull No. of commits' , pull.commits)
#    print('pull request ID', pull.id)
#    print('Files' , pull.get_files())
    changed_file_list = []
    files = pull.get_files()
    for file in files:
        changed_files = {}
        changed_files['fileName'] = file.filename
        changed_files['sha'] = file.sha
        #changed_file_list.append(json.dumps(changed_files))
        changed_file_list.append(changed_files)
        #print('Changed Files' , file)
#        print('File Name', file.filename)
#        print('File sha', file.sha)
    pull_json['changed_files'] = changed_file_list
    
    pull_comment_list = []
    comments = pull.get_comments()
    for comment in comments:
        
        pull_comments = {}
        pull_comments['id'] = comment.id
        pull_comments['body'] = comment.body
        pull_comments['commented_by'] = comment.user.login
        #pull_comment_list.append(json.dumps(pull_comments))
        pull_comment_list.append(pull_comments)
        
#        print('pull_comment',comment)        
#        print ('pull comment id', comment.id)
#        print('pull comment body', comment.body)        
#        print('Login User', comment.user.login)
        
    pull_json['comments'] = pull_comment_list
    #pull_store.append(json.dumps(pull_json,default=json_serial))
    pull_store.append(pull_json)
    with open('pulls_dataset.json', 'w') as outfile:
        json.dump(pull_store, outfile,default=json_serial)
    
    #print('pull comment',pull_comment)
"""    
    commits = pull.get_commits()
    for commit in commits[:2]:
        print('pull commit', commit)
        print('commit message',commit.sha)
        
        
    #print('Pull get Commits ',pull.get_commits())
    #print('Pull get Issue Commits', pull.get_commits().totalCount)

"""

"""
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
for branch in branches[:10]:
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
    
"""
