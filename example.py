#!/usr/bin/env python3.3
# -*- coding:utf-8 -*-

import sys
from pynt import task, build

@task()
def clean():
    '''Clean build directory.'''
    print('Cleaning build directory...')

@task(clean)
def html(target='.'):
    '''Generate HTML.'''
    print('Generating HTML in directory {target}'.format(target = target))


@task(clean, ignore=True)
def images():
    '''Prepare images.'''
    print('Preparing images...')

@task(html,images)
def start_server(server='localhost', port = '80'):
    '''Start the server'''
    print('Starting server at {server}:{port}'.format(server = server, port = port))

@task(start_server) #Depends on task with all optional params
def stop_server():
    print('Stopping server....')

@task()
def copy_file(src, dest):
    print('Copying from {src} to {dest}'.format(src = src, dest = dest))

@task()
def echo(*args,**kwargs):
    print(args)
    print(kwargs)

if __name__ == '__main__':
    build(sys.modules[__name__],sys.argv[1:])
