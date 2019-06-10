#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    Clase Community: Representa una comunidad energética

'''

from models.mySQLHandler import mySql
import json

class Community(object):

    def __init__(self, name, description, latitude, longitude, gestorId):
        self.name = name
        self.coords = [latitude, longitude]
        self.gestorId = gestorId
        self.description = description

    def setCoords(self, coords):
        self.coords = coords

    def setDescription(self, description):
        self.description = description

    def setGestorId(self, gestorId):
        self.gestorId = gestorId

    def toDict(self):
        response = {"name": self.name, "coords": self.coords, "gestorId": self.gestorId, "description": self.description}

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