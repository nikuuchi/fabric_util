from fabric.api import run, sudo, cd, lcd, env
from fabric.decorators import task

git_url = "git@github.com:nikuuchi/"
git_cmd = "git"

@task
def pull(dirname="/home/uchida", branch="master"):
    with cd(dirname):
        run("{0} fetch origin".format(git_cmd))
        run("{0} merge origin/{1}".format(git_cmd, branch))

