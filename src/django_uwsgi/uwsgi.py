from __future__ import absolute_import, print_function

import os
import sys

from django.conf import settings

from django_uwsgi.utils import dict_to_env_vars


class UWSGIServer(object):
    name = 'uwsgi'

    def __init__(self, debug=False, workers=None):
        options = (settings.UWSGI or {}).copy()

        options.setdefault('module', settings.WSGI_APPLICATION)
        options.setdefault('auto-procname', True)
        options.setdefault('workers', 3)
        options.setdefault('threads', 4)
        options.setdefault('vacuum', True)
        options.setdefault('virtualenv', sys.prefix)

        uid = os.getuid()
        if uid > 0:
            options.setdefault('uid', uid)
        gid = os.getgid()
        if gid > 0:
            options.setdefault('gid', gid)

        options['master'] = True

        if workers:
            options['workers'] = workers

        self.options = options

    def prepare_environment(self, env=None):
        if env is None:
            env = os.environ

        for k, v in dict_to_env_vars(self.options):
            env.setdefault(k, v)

        virtualenv_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        current_path = env.get('PATH', '')
        if virtualenv_path not in current_path:
            env['PATH'] = '%s:%s' % (virtualenv_path, current_path)

    def run(self):
        self.prepare_environment()
        os.execvp('uwsgi', ('uwsgi',))
