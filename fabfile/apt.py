from fabric.api import run, sudo, cd, lcd, env
from fabric.decorators import task

cmd_name = 'apt-get'

@task
def upgrade():
    sudo("{0} update".format(cmd_name))
    sudo("{3} upgrade -y".format(cmd_name))

def install(package):
    sudo("{0} install {1} -y".format(cmd_name, package))

def remove(package):
    sudo("{0} remove {1} -y".format(cmd_name, package))

@task
def installDevelopmentEssential():
    install('git subversion build-essential tig vim zsh python-setuptools tmux screen cmake cmake-curses-gui')
