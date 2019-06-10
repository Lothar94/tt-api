#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    Clase Member: Representa un miembro de una comunidad energética

'''

from models.mySQLHandler import mySql
import json

class Member(object):

    def __init__(self, memberId, name, derLatitude, derLongitude, derName):
        setattr(Member, 'memberId', memberId)
        setattr(Member, 'name', name)
        setattr(Member, 'derCoords', [derLatitude, derLongitude])
        setattr(Member, 'derName', derName)

    def save(self):
        sqlQuery = "INSERT INTO members (memberId, name, derLatitude, derLongitude, derName) VALUES (%s, %s, %s, %s, %s)"
        values = (self.memberId, self.name, self.derLatitude, self.derLongitude, self.derName)
        mySql().query(sqlQuery, values)
        return None

    def update(self):
        sqlQuery = "UPDATE members SET name = %s, derLatitude = %s, derLongitude = %s, derName = %s WHERE memberId = %s"
        values = (self.memberId, self.name, self.derLatitude, self.derLongitude, self.derName, self.memberId)
        mySql().query(sqlQuery, values)
        return None

    def delete(self):
        sqlQuery = "DELETE FROM members WHERE memberId = %s"
        values = (self.memberId)
        mySql().query(sqlQuery, values)
        return None

    def toJson(self):
        response = {}
        attrs = [a for a in dir(Member) if not a.startswith('__') and not callable(getattr(Member,a))]
        for attr in attrs:
            response[attr] = getattr(Member, attr)
        return json.dumps(repsonse)