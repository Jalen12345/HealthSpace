# Git

## What is Git?

- Git is a **Version Control System**
  - Can recover previous versions of your work
- Can be used to collaborate with other programmers (what we'll be doing!)

- Git is the most commonly used version control system for computer programmers (pretty much everyone and every company use Git)

## How Does Git Work?

- Git stores your code in snapshots
  - These snapshorts are called **commits** because the developer "commits" them to the log
- Thses commits are all stores in a **repository**, which stores other metadata like when the commit was made or who made the commit

# Git Diagram

![Envisioning Git](https://www.dougmahugh.com/content/images/2019/01/GitCommands-2.png)

# Git Basics

## Vocab

**Directory** - A folder on a computer system

**Commit** - A snapshot of your code at the time the commit was made

**Repository** - Where all the commits are stored

**Local Repository** - The repository on your computer

**Origin** - A repository hosted on a server (usually GitHub)

## git init / git clone

**Init**

- Creates empy repository in the current directory
- There will be no commits or files traked initally
- Usage: 

```bash
git init
```

**Clone**

- Downloads an external repository and sets it up as a local repository in the current directory
- Usage:

```bash
git clone {url}			
```

## git add

- Marks files to be committed in the next commit
- Git does **NOT** commit the files automitically
- Usage

```bash
#add a specific file or directory
git add {file/directory}
#add all the files you've changed since the last commit (won't add new files though)
git add -A
#add all files in the current directory (including in all sub-directories)
git add .
```

**N.B.** `git add` will *not* add files in the folder `.gitignore`

**Useful**: `git status` will show if your branch is up to date and the changes that need to be committed

## git commit

- This will commit staged files to the repository
- Attach your email/name and when you make the commit
- Usage:

```bash
#will commit and open up editor to add message
git commit
#will commit with specified message
git commit -m "My commit message"
#will commit all the changed files (w/ message)
git commit -am "Commit all changed"
```

**N.B.** can use `git log` to see all the commits

## git push

- uploads any new commits to Origin
- Usage:

```bash
#will "push" your code in the commit to the origin (assuming you have privileges)
git push
```

## git pull

- Downloads any commits in the origin but not in your local repository (updates your repository to the origin's version)
- Usage:

```bash
#will "pull" the latest version form the origin
git pull
```

# Merging & Conflicts

- So far, everything we've done has been in sequential order
  - Usually everything is all good since people are doing things in order or working on different parts and/or different times
  - However, when you're working with mutliple people on a project, this may not always be the case!
- *What would happen if* we tried to change the same thing at the same time?

## Merge Conflicts

- git will tell you is you have a merge conflict
- it wil mark the origin's version with `HEAD` and your version with a `=====`  and ending with a hexadecimal code (your local computer)
- Then you...
  1. Remove what git has labeled
  2. Figure out what you want to do (combine the differences, get rid of one, or do something else)
  3. Push the new code 

# Git Branching

## Branches: Why we need them

- Useful for avoiding merge conflicts (deal with issues on a separate branch before putting on the main one)
- Helps to keep things organized by sectioning off different parts to different branches

## Branching Diagram

![Git Branches: List, Create, Switch to, Merge, Push, &amp; Delete](https://www.nobledesktop.com/image/gitresources/git-branches-merge.png)

## How to use branches

### git checkout

- Allows you to "check out" a given branch
- Create a new branch
- Usage:

```bash
#look an existing branch
git checkout "existing-branch"
#create a new branch
git checkout -b "new-branch"
```

### git merge

- "Merges" a branch onto the current branch
  - *This is actually part of what happens when you run* `git pull`
- Usage:

```bash
#Merge a specified branch onto the branch you're currently on
git merge "other-branch"
```

**Caution**: Can cause merge conflicts!

## Pull Requests (GitHub)

- **Pull Requests** are Github's way for people to review code before merging it
  - Show that something is complete/ready so that it can added to the main branch (usually after some review)
  - <u>a Github feature (not part of Git)</u>
- Simply push your code to GitHub and open one
- You can also do things like label, attach media, assign reviewers, and autmoatically run unit tests!

