#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    Clase Community: Representa una comunidad energética

'''

from models.mySQLHandler import mySql
import json

class Community(object):

    def __init__(self, name, description, latitude, longitude, gestorId):
        setattr(Community, 'name', name)
        setattr(Community, 'coords', [latitude, longitude])
        setattr(Community, 'gestorId', gestorId)
        setattr(Community, 'description', description)

    def setCoords(self, coords):
        setattr(Community, 'coords', coords)

    def setDescription(self, description):
        setattr(Community, 'description', description)

    def setGestorId(self, gestorId):
        setattr(Community, 'gestorId', gestorId)

    def toDict(self):
        response = {}
        attrs = [a for a in dir(Community) if not a.startswith('__') and not callable(getattr(Community,a))]
        for attr in attrs:
            response[attr] = getattr(Community, attr)
        return response

''' MYSQL
    def save(self):
        sqlQuery = "INSERT INTO communities (name, description, latitude, longitude, gestorId) VALUES (%s, %s, %s, %s, %s)"
        values = (self.name, self.description, self.latitude, self.longitude, self.gestorId)
        mySql().query(sqlQuery, values)

    def update(self):
        sqlQuery = "UPDATE communities SET description = %s, latitude = %s, longitude = %s, gestorId = %s WHERE name = %s"
        values = (self.name, self.description, self.latitude, self.longitude, self.gestorId, self.name)
        mySql().query(sqlQuery, values)

    def delete(self):
        sqlQuery = "DELETE FROM communities WHERE name = %s"
        values = (self.name)
        mySql().query(sqlQuery, values)
'''