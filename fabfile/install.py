# -*- coding: utf-8 -*-
from fabric.api import run, sudo, cd, lcd, env
from fabric.decorators import task

@task
def LLVM(dirname):
    with cd(dirname):
        run("wget http://llvm.org/releases/3.2/clang+llvm-3.2-x86_64-linux-ubuntu-12.04.tar.gz")
        run("tar xf clang+llvm-3.2-x86_64-linux-ubuntu-12.04.tar.gz")
    with cd(dirname + "/clang+llvm-3.2-x86_64-linux-ubuntu-12.04"):
        sudo("cp -R * /usr/local")

@task
def Nodejs(dirname):
    with cd(dirname):
        run("wget http://nodejs.org/dist/v0.10.19/node-v0.10.19-linux-x64.tar.gz")
        run("tar xf node-v0.10.19-linux-x64.tar.gz")
    with cd(dirname + "/node-v0.10.19-linux-x64"):
        sudo("cp -R * /usr/local")

@task
def Emscripten(dirname):
    with cd(dirname):
        sudo("git clone https://github.com/kripken/emscripten.git")

# TODO use apt.py
@task
def AptLibrary():
    sudo("apt-get install git openjdk-7-jdk apache2 vim tmux subversion -y")

@task
def C2js(dirname, homedir):
    with cd(dirname):
        run("git clone https://github.com/nikuuchi/c2js.git")
    with cd("/var/www"):
        sudo("ln -s " + dirname +"/c2js ./c2js")
        sudo("cp " + homedir + ".emscripten /var/www"

@task WriteApachConf():
    text = '''
        <Directory /var/www/c2js/>
             Options ExecCGI FollowSymLinks MultiViews
             AllowOverride None
             Order allow,deny
             allow from all
        </Directory>
        '''
    
