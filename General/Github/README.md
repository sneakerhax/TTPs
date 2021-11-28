# General - Github

## Github site

**Fork** (performed by clicking fork on main project) - Forks copy of git repo to our account

## Git command line

```
git clone <fork>
```
  
  Clones fork to our local system 

```
git status
```

Make sure local copy is clean and checks status

```
git add <file>
```

Adds file to staging area

```
git commit -m <comment>
```

commits changes (git commit -a -m “commit notes”) adds files and commits

```
git log —status
```

Detailed information about commits

```
git remote add origin https://github.com/repo/git.git
```

Add origin to local repo

```
git push -u origin main
```

Pushes main branch to remote git repo and store so you can just (git push)

```
git pull origin main
```

Pulls changes from remote repo

```
git diff HEAD
```

Diff for changes from origin main

```
git reset <file>
```

Unstage file

```
git checkout — <file>
```

Remove changes before last commit

```
git branch <branch_name>
```

Create a new branch off your main branch

```
git branch
```

List current branch

```
git checkout <branch_name>
```

Switch branches to specified branch name

```
git checkout -b <branch_name>
```

Create branch and move to it

```
git rm ‘*.txt’
```

Remove all text files

```
git rm -r <folder_name>
```

Remove folder from tracking

```
git merge <branch_name>
```

merge branch into main

```
git branch -d <branch_name>
```

Cleanup/remove branch

```
git push
```

Push changes to remote repo

```
git commit -a
```

Delete files that are no longer there while committing

```
git -C <repo_location> pull
```

Git pull a different directory
