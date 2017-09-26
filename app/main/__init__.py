#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-26 15:26:23
# @Author  : zhouyiran (719151975@qq.com)
# @Link    : http://www.twinflag.com
# @Version : $Id$

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
