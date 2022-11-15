#usr/bin/python

import pandas as pd
from git import Repo

import re, signal, sys, time
from progress.bar import ChargingBar as Bar

def handler_signal(signal, frame):
    print("\n\n [!] Out ..........\n")
    sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, handler_signal)

REPO_DIR = "./skale/skale-manager"

def extract(url):
    repo = Repo(url)
    commits = list(repo.iter_commits('HEAD'))
    return commits

def transform(commits):
    data = list()
    bar = Bar('Searching', max=len(commits))
    for commit in commits:
        found = re.findall("pass|PASS|Pass|password|PASSWORD|Password|secret|SECRET|Secret|key|KEY|Key", commit.message)
        if found:
            data.append([commit, found])
        bar.next()
    bar.finish()
    return data
        
def load(data):
    #Create a text file with the results
    with open("results.txt", "w") as f:
        bar = Bar('Saving data', max=len(data))
        for commit in data:
            s = f"Found {commit[1]} in commit with id {commit[0].hexsha}:\n{commit[0].message}\n"
            f.write(s)
            bar.next()
        bar.finish()
    #Print the results
    for commit in data:
        #The id of the commit is:
        s = f"Found {commit[1]} in commit with id {commit[0].hexsha}:\n{commit[0].message}\n"
        print(s)
    
    print("All data saved succesfully in results.txt")

if __name__ == '__main__':
    commits = extract(REPO_DIR)
    data = transform(commits)
    load(data)