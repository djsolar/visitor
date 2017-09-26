#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-26 14:34:16
# @Author  : zhouyiran (719151975@qq.com)
# @Link    : http://www.twinflag.com
# @Version : $Id$

import os
from app import create_app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
