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
def Emscripten(diname):
    with cd(dirname):
        sudo("git clone https://github.com/kripken/emscripten.git")

# TODO use apt.py
@task
def AptLibrary():
    sudo("apt-get install git openjdk-7-jdk apache2 vim tmux subversion -y")

