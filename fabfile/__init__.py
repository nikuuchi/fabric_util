from fabric.api import run, sudo, cd, lcd, env
from fabric.decorators import task
import apt

def set_env():
    pass

@task
def make_workdir(user="uchida"):
    run("mkdir -p /home/"+user+"/dev")
    run("mkdir -p /home/"+user+"/dev/conf")
    run("mkdir -p /home/"+user+"/dev/konoha")
    run("mkdir -p /home/"+user+"/dev/paper")

@task
def clone_config(user="uchida"):
    with cd("/home/"+user+"/dev/conf"):
        run("git clone https://github.com/nikuuchi/dotfiles.git")

@task
def init_config(user="uchida"):
    with cd("/home/"+user+"/dev/conf/dotfiles"):
        run ("git submodule init")
        run ("git submodule update")
        run ("./setup.sh")

@task
def start(user="uchida"):
    apt.upgrade()
    apt.installDevelopmentEssentials()
    make_workdir(user)
    clone_config(user)
    init_config(user)
