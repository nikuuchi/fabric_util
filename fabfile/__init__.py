# -*- coding: utf-8 -*-
from fabric.api import run, sudo, cd, lcd, env
from fabric.decorators import task
import apt
import install
from shellutil import *

def set_env():
    pass

@task
def start():
    dirname = "/home/tsunade"
    apt.upgrade()
    install.AptLibrary()
    install.LLVM()
    install.Nodejs()
    install.Emscripten()
