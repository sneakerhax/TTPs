# General - Github

### Basic commands and terms

Fork (performed by clicking fork on master project) - Forks copy of git repo to our account

git clone <fork> - Clones fork to our local system 

git status - Make sure local copy is clean and checks status

git add - Adds file to staging area

git commit -m “comment” - commits changes (git commit -a -m “commit notes”) adds files and commits

git log —status - Detailed information about commits

git remote add origin https://github.com/repo/git.git

git push -u origin master - Pushes master branch to remote git repo and remember so you can just (git push)

git pull origin master - Pulls changes from remote repo

git diff HEAD - Diff for changes from origin master

git reset <file> - Unstage file

git checkout — <file> - Remove changes before last commit

git branch <branch_name> - Create a new branch off your master branch

git branch - See what branch your currently on

giit checkout <branch_name> - Switch branches to specified branch name

git checkout -b <branch_name> - Create branch and move to it

git rm ‘*.txt’ - Remove all text file

git rm -r <folder_name> - Remove folder

git merge <branch_name> - merge branch into master

git branch -d <branch_name> - Cleanup/remove branch

git push - Push changes to remote repo

git commit -a - Delete files that are no longer there while committing
