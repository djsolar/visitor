#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-26 14:35:28
# @Author  : zhouyiran (719151975@qq.com)
# @Link    : http://www.twinflag.com
# @Version : $Id$
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
