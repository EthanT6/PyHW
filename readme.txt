This repository is for the purpose of learning the basics of Git and Github, while also practicing Python.

Git and Github How-To

Create a project folder.
mkdir PyHW

Open your project folder.
cd PyHW/

Initialize a Git repository.
git init

Create a file.
touch readme.txt

Stage your changes
git status
git add readme.txt
git status

Commit your Changes w/ a comment.
git commit -m "Practicing Staging and Commit"

Create a branch of master.
git branch
git checkout -b test-branch

Merge your branch with master
git merge test-branch

Add your repo origin
git remote add origin <Repo URL>

Push your repo to github
git push -u origin master

Clone an existing repo
git clone <Repo URL>
