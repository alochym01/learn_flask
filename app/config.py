import os

# This module will contain a Configuration class that instructs Flask


class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
    DEBUG = True
