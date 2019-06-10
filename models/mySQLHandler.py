#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from config import connection

class mySql(object):
    
    @staticmethod
    def query(sqlQuery, values):
        result = None
        try:
            conn = mysql.connector.connect(host=connection['host'], user=connection['user'], password=connection['password'], database=connection['database'])
            c = conn.cursor()
            c.execute(sqlQuery, values)
            result = c.fetchone()
            conn.commit()
            conn.close()
        except:
            print("Error executing a query")
            raise
        
        return result