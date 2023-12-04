**Using Rebase**

First, fix your name in `git-config`:

``` bash
git config --global user.name "New Author Name"
git config --global user.email "<email@address.example>"
```

Optional, but it makes sure to reset the committer name, too.

To rewrite metadata for a range of commits using a rebase, do
``` bash
git rebase -r <some commit before all of your bad commits> \
    --exec 'git commit --amend --no-edit --reset-author'
```

`--exec` will run the git commit step after each commit is rewritten (as if you ran git commit && git rebase --continue repeatedly).


If you also want to change your first (root) commit, you will have to add `--root` to the rebase call.

This will change both the committer and the author to your user.name/user.email configuration. If you did not want to change that config, you can use --author "New Author Name <email@address.example>" instead of --reset-author. Note that doing so will not update the committer -- just the author.

**Single Commit**

If you just want to change the most recent commit, a rebase is not necessary. Just amend the commit:

```bash
git commit --amend --no-edit --reset-author
```

**Entire project history**
```bash
git rebase -r --root --exec "git commit --amend --no-edit --reset-author"
```

```bash
git config --global user.name "Sumeet Shukla"
git config --global user.username "sumeetshk"
git config --global user.email "<sumeet.k.shukla@gmail.com>"

git rebase -r --root --exec "git commit --amend --no-edit --reset-author"
```