#!/usr/bin/env python3
import configparser
import MySQLdb.cursors

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    return MySQLdb.connect(host = config['mysqlDB']['host'],
           user = config['mysqlDB']['user'],
           passwd = config['mysqlDB']['pass'],
           db = config['mysqlDB']['db'])
