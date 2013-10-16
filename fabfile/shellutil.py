from fabric.api import run, sudo, cd, lcd, env
from fabric.decorators import task

@task
def mkDir(dirname):
    run("mkdir -p " + dirname)

