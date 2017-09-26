#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-26 15:31:43
# @Author  : zhouyiran (719151975@qq.com)
# @Link    : http://www.twinflag.com
# @Version : $Id$

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
