"""
    Database Specific Configuration File
"""
""" Put Generic Database Configurations here """
import os

class DBConfig(object):
    """ DB_ON must be True to use the DB! """
    DB_ON = True
    DB_DRIVER = 'mysql'
    DB_ORM = False

""" Put Development Specific Configurations here """
class DevelopmentDBConfig(DBConfig):
    DB_USERNAME = 'oogiceqcdnhmeb'
    DB_PASSWORD = 'Vg0WqHkpjAZ2IJJyuJSiVyYRGn'
    DB_DATABASE_NAME = 'd37p7vn71e7beh'
    DB_HOST = 'ec2-50-19-117-114.compute-1.amazonaws.com'
    DB_PORT = 5432
    # """ unix_socket is used for connecting with MAMP. Take this out if you aren't using MAMP """
    DB_OPTIONS = {
    #     'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock'
    }

""" Put Staging Specific Configurations here """
class StagingDBConfig(DBConfig):
    DB_USERNAME = 'oogiceqcdnhmeb'
    DB_PASSWORD = 'Vg0WqHkpjAZ2IJJyuJSiVyYRGn'
    DB_DATABASE_NAME = 'd37p7vn71e7beh'
    DB_HOST = 'ec2-50-19-117-114.compute-1.amazonaws.com'

""" Put Production Specific Configurations here """
class ProductionDBConfig(DBConfig):
    DB_USERNAME = 'oogiceqcdnhmeb'
    DB_PASSWORD = 'Vg0WqHkpjAZ2IJJyuJSiVyYRGn'
    DB_DATABASE_NAME = 'd37p7vn71e7beh'
    DB_HOST = 'ec2-50-19-117-114.compute-1.amazonaws.com'
