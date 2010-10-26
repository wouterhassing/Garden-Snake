"""
    config
    ~~~~~~

    Configration file for Garden Snake.

    :copyright: Copyright 2010 by Wouter Hassing.
    :license: see LINCENSE for more details.
"""

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = "testkey"
DATABASE_URI = ""
USERNAME = "admin"
PASSWORD = "test"
