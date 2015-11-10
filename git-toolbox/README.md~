# git-toolbox
Repository for Fall 2015 Software Design - a toolbox exercise for learning more about using git

This is very specific information - to learn more about how to use git in a general sense, [this](https://www.atlassian.com/git/tutorials/) is one of my favorite sources.

## Git Skills

** Basic **
- Check state of repository
- Add files
- Commits (and good format)
- Pushing

** Additional **
- Adding interactively
- Branching
- Merge conflicts?
- Editing previous commits - interactive rebase

## Things to know when doing this toolbox:
- Everything written in angle brackets <like this> should be replaced by specific information by your system, and when you do so, youhe should not actually use the angle brackets when you run it.  For example, if I said to run the command `git commit -m "<your message here>"`, you might run the command `git commit -m "Awesome commit message"` (no angle brackets!)

## Practice basic skills

1. Fork this repository to your own GitHub account
2. Clone it to your local environment
3. Create a new file named `hello.py` and add a short Python program

### Notes on Commits
As you know, commits are a way to save a chunk of changes to your code at a specific point.  To this end, it's important to have good commit messages that tell you what changed about your code at each commit.

You can see previous commit messages by running the command:
```
git log
```
Which commit messages for this repository are informative?  Which are not?  

If you ever plan to contribute to open-source projects, you'll need your commit messages to be informative.  In general, that means you should rarely by using the -m flag: `git commit -m ""short commit message here"` because it doesn't allow a lot of information.

Typing `git commit` with no arguments will open up a text editor that you can type a more detailed commit into.  If you want to change the text editor it uses (TOTALLY optional), you can do so with the command:
``` $ git config --global core.editor neweditornamehere ```

In general, it's accepted in most coding communities that a commit message should take this general format:
```
<Section of code edited>: <Summary of changes made in present tense>

<Additional details of what changed>
```

All lines should be less than 80 characters long.  The additional details will probably be longer than this - you should manually press enter after about 80 characters to start a new line.

For example, as you saw when running `git log`, the second commit for this repository took this format:
```
Readme: Add some tasks regarding initial steps and commits

Took notes in the README to lay out an outline for this toolbox, and drafted
some initial steps for students to follow in cloning the repo and learning
about commits and commit messages.
```

With these guidelines in mind, commit your `hello.py` file with an appropriate commit message.

## Looking at Commits
A few commands that can tell you interesting information about your commits:
**Tip**: If you run a command that shows a lot of information, it will show a few lines and keep showing more as you hit enter.  If you want to *stop* seeing more info, type `q` to escape from git-showing-you-info mode.

- `git log` - we've seen this one, it will show a list of all previous commits.  
- `git show <commit checksum>` - each commit is assigned a unique 40-character checksum (displayed in git log).  You do **not** need to type out the whole checksum, just the first 4 or 5 characters such that it can uniquely identify a single commit.  This command will show the complete details of a single commit, compared to the previous commit.
- `git diff <commit checksum> <another commit checksum>` - this will show the difference between the first commit you give and the second.

## Editing Commits
Make a slight change to your `hello.py` file (maybe add a comment).  In general, when working on large projects, it's annoying to have small commits like this that only add one line of code, especially if it's just a typo and should be in the previous commit.  There's a couple ways to accomplish this.

### Un-committing and Re-committing
The current "working branch" of uncommitted changes is known in git as the HEAD.  Each previous commit is a previous version of the HEAD.  So in the same way you can run `git reset HEAD` to unstage some files you added, you can run that command with a different version of HEAD as well.

Say you want to undo the commit that you just made.  These of these commands will do this:
```git reset HEAD~1```
```git reset HEAD^```

The HEAD number modifiers count backwards.  Since "HEAD" is the current working version, "HEAD~1" is the most recent commit.  Using "HEAD~2" would reset everything to the second most recent commit, and so on.  In the same way, using one ^ after HEAD refers to HEAD~1, and HEAD^^ would be the same as HEAD~2.  

You can also reference the commit you want to reset directly by the first few characters of its checksum ID.
```git reset <commit checksum>```
However, there's a catch.  Resetiing HEAD~1 will reset UP TO AND INCLUDING the changes made in this commit.  However, if you try to reset with the checksum of this most recent commit, it will only reset UP TO that commit.  In order to actually reset the changes made in a commit, you need to give it the checksum of the commit one step earlier.

Pick a method, and reset the commit you just made.  Create a new commit that includes your new changes to `hello.py` and re-commit.

### Rebasing
Maybe you found that last method annoying, in having to type out your commit message all over again.  You ask, surely there must be a better way?  There is!  `git rebase` is a powerful tool, and we're just going to look at a few of its many abilities, but feel free to look further on your own.

Make another small change to `hello.py` and commit those changes as a new commit.

Run the command `git rebase -i`

This will open a text editor in which you are looking at a list of commits made, from oldest to newest.  Each one says "pick" next to it, which means it will be picked as a commit to be applied when you apply the rebase.  But you can change this word for different behavior.

- **reword** lets you edit a commit message - you can edit the first line of the message here in the rebase window, but if you want to edit some of the details this will allow that
- **edit** lets you go "back in time" to when that commit was being made, and add or remove files as you choose
- **squash** squashes this commit into the commit before it (above it in this list), and will concatenate their commit messages together
- **fixup** does the same thing as squash, but doesn't concatenate the messages and uses the previous message only

Be careful using rebase - if you delete lines here, you'll delete that commit and all changes you made in your code.

Go ahead and change the word "pick" next to your most recent commit to "squash", and exit and save the text editor.  It will open a new text editor asking you to confirm the concatentation of the commit messages.  Edit them as you like, then exit and save.  When rebase finishes, run `git log` to see that your previous two commits have now been squashed into a single commit.

## Branching
Make sure you have a decent understanding of what a "branch" is in git.  [Here's a good starting resource](https://git-scm.com/book/en/v1/Git-Branching-What-a-Branch-Is)

<<<<<<< HEAD
Running `git branch` will display all possible branches, with an asterisk next to the one you're currently editing.  You should see two branches, `master` and `test`.  Running `git branch <branch name>` will create a new branch with the given name, but not switch into it.

To switch what branch you're working on, type the command `git checkout <branch name>`.  Checkout the `test` branch, make a change, and commit it.  Then, switch back to the master branch and run `git log`.  Do you see the commit you just made there?

Go back to the `test` branch.  Run git log, and you should see your commit again.

Usually, when you push changes to GitHub, you run `git push origin master` and specify the master branch.  To push this branch, replace the "master" branch name with "test".
=======
Running `git branch` will display all possible branches, with an asterisk next to the one you're currently editing.  You should see two branches, `master` and `test`.  

To switch what branch you're working on, type the command `git checkout <branch name>`.  Checkout the `test` branch, make a change, and commit it.  Then, switch back to the master branch and run `git log`.  Do you see the commit you just made there?

You can also branch off commits.  The command `git checkout <commit checksum>` will revert you back to the state of your code at the time of a commit.
>>>>>>> 59d9a23e632be0a608bb050c083a942c33b3d7f3

## Interactive Adding
Go back to your `master` branch and edit `hello.py`.  Add several lines of code in multiple places - for example, a comment at the top, new lines of code at the bottom.  Have at least 5 or 6 new lines of code.

Say that you want to commit these changes, but not all the changes in the entire file.  You can do this through interactive adding.  Where you usually typed `git add <filename>` to add a file, you can add interactively by typing:
```git add -i```

This will open an in-terminal add program that you can quit at any time by typing "q".  We have a list of several options here, and what we want to do is option 5 - Patch, which will let us create a "patch" of only certain changes.

Type "5" or "p" and press enter.  Git will show you a list of all files with uncommitted changes in them.  One by one, type the number of a file you want to go through and add changes from.  An asterisk will appear when they are selected.  When you've selected all desired files, hit enter with no input.

It goes through each "hunk" of changes in the selected files and prompts you with a series of commands.  You can type "?" at any time to see a description of the commands, but in general you only need to type "y" for "yes, add this hunk", or "n" for do not add the hunk.  When all hunks have been gone through, you'll go back to the main menu.  Typing "1" will let you see the status, and will show numbers of staged hunks based on how many you chose to add.  From there, type "7" or "q" to quit.  When you then run the `git status` command, you'll see your changes are staged for commit.

## To Complete This Toolbox
Read through this README and execute the commands as it suggests.  Commit and push all changes to this repo so that we can see your work.  In addition, choose one of the git commands you practiced and learn more about it in-depth.  Commands like `rebase` and `add -i` and `branch` and `checkout` can do many thing besides what was described here.  Or learn a new command, like `revert`, a "safe" alternative to the `reset` command we learned.  Practice the command, and include a short text file description of what the command does, and what you did to practice it.