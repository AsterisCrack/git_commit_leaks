# git_commit_leaks
## Quick finder for leaks in git commits

This program is an ETL that will go through all commits in a git repository branch and look for key words that may be compromising.
After it is done, it will save all of the data inside a readable .txt document and inside a json file for future use.
Also, it is possible to mount everything on a docker image.

### Instructions:
First of all, clone the repo you want to investigate and change the repo folder location inside the python program.
Then, type the branch you want to investigate in the corresponding variable inside the python program.
Finally, execute.
If you want to mount the docker image, change the location of the repo folder following the COPY command of the dockerfile.
Finally, run this command on your terminal:
docker mount -t git_commit_leaks
