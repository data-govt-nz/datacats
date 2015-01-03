# Copyright 2014-2015 Boxkite Inc.

# This file is part of the DataCats package and is released under
# the terms of the GNU Affero General Public License version 3.0.
# See LICENSE.txt or http://www.fsf.org/licensing/licenses/agpl-3.0.html

import sys
from os import listdir
from os.path import isdir, exists

from datacats.cli import manage

def write(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def install(project, opts):
    """
    Install all packages found in the project src directory
    and their requirements.txt files
    """
    srcdirs = set()
    for d in listdir(project.target):
        fulld = project.target + '/' + d
        if not isdir(fulld):
            continue
        if not exists(fulld + '/setup.py'):
            continue
        srcdirs.add(d)
    try:
        srcdirs.remove('ckan')
    except KeyError:
        print 'ckan not found in project src directory'
        return

    write('Installing all packages in src')

    srcdirs = ['ckan'] + sorted(srcdirs)
    for s in srcdirs:
        project.install_package_requirements(s)
        write('.')
    for s in srcdirs:
        project.install_package_develop(s)
        write('.')
    write('\n')

    address = project.web_address()
    if address is not None:
        # FIXME: reload without changing debug setting?
        manage.reload(project, {'--production': False})
