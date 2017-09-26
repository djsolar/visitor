#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-26 15:26:37
# @Author  : zhouyiran (719151975@qq.com)
# @Link    : http://www.twinflag.com
# @Version : $Id$

from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')
