#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    Clase Member: Representa un miembro de una comunidad energética

'''

from models.mySQLHandler import mySql
import json

class Member(object):

    def __init__(self, memberId, name, surname, derLatitude, derLongitude, derName, communityName):
        self.memberId = memberId
        self.name = name
        self.surname = surname
        self.derCoords = [derLatitude, derLongitude]
        self.derName = derName
        self.communityName = communityName

    def setName(self, name):
        self.name = name

    def setSurname(self, surname):
        self.surname = surname

    def setCommunityName(self, communityName):
        self.communityName = communityName

    def setDerCoords(self, coords):
        self.derCoords = derCoords

    def setderName(self, derName):
        self.derName = derName

    def toDict(self):
        response = {"memberId": self.memberId, "name": self.name, "surname": self.surname, "derCoords": self.derCoords, "derName": self.derName, "communityName": self.communityName}
        return response

''' MYSQL
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
'''