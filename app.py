#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, Response
from models.community import Community
from models.member import Member
from config import error400Message

import json
import math

app = Flask(__name__)

communitiesMemory = []                # Test mode
membersMemory = []                    # Test mode

def isInCommunitiesMemory(communityName):
    result = False
    for community in communitiesMemory:
        if community.name == communityName:
            result = True
    return result

def isInMembersMemory(memberId):
    result = False
    for member in membersMemory:
        if member.memberId == memberId:
            result = True
    return result

def haversineMeasure(lat1, lon1, lat2, lon2):
    R = 6378.137
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c

    return d * 1000

def validateFloat(value):
    result = True
    try:
        float(value)
    except:
        result = False
    return result


@app.route("/communities", methods=["GET", "POST"])
def communitiesCreation():
    response = Response("", status=204, mimetype='application/json')

    if request.method == "GET":
        communities = []
        for community in communitiesMemory:
            communities.append(community.toDict())

        response = Response(json.dumps(communities), status=200, mimetype='application/json')            

    elif request.method == "POST":

        form = request.get_json()
        if "name" in form and "description" in form and "latitude" in form and "longitude" in form and "gestorId" in form:
            if form["name"] != "":
                community = Community(form["name"], form["description"], form["latitude"], form["longitude"], form["gestorId"])
                if not isInCommunitiesMemory(form["name"]):
                    communitiesMemory.append(community)
                    response = Response(json.dumps(community.toDict()), status=200, mimetype='application/json')
            else:
                response = Response(error400Message, status=400, mimetype='application/json')
        else:
            response = Response(error400Message, status=400, mimetype='application/json')

    print(communitiesMemory)
    return response

@app.route("/communities/<name>", methods=["GET", "POST", "PUT", "DELETE"])
def communitiesModification(name):
    response = Response("", status=204, mimetype='application/json')

    if request.method == "GET":

        for community in communitiesMemory:
            if community.name == name:
                response = Response(json.dumps(community.toDict()), status=200, mimetype='application/json')

    elif request.method == "PUT":

        form = request.get_json()

        if name != "" and "latitude" in form and "longitude" in form and "gestorId" in form and "description" in form:
            for community in communitiesMemory:
                print(community.name)
                if community.name == name:
                    community.coords = [form["latitude"], form["longitude"]]
                    community.description = form["description"] 
                    community.gestorId = form["gestorId"]

                    response = Response(json.dumps(community.toDict()), status=200, mimetype='application/json')
        else:
            response = Response(error400Message, status=400, mimetype='application/json')


    elif request.method == "DELETE":

        index = -1
        for community in communitiesMemory:
            if community.name == name:
                index = communitiesMemory.index(community)

        if index != -1: 
            del communitiesMemory[index]

    else:
        return "default"

    return response

@app.route("/members", methods=["GET", "POST"])
def communitiesInscription():
    response = Response("", status=204, mimetype='application/json')

    if request.method == "GET":
        members = []
        for member in membersMemory:
            members.append(member.toDict())

        response = Response(json.dumps(members), status=200, mimetype='application/json')       
    
    elif request.method == "POST":

        form = request.get_json()

        if "memberId" in form and "derLatitude" in form and "derLongitude" in form and "surname" in form and "name" in form and "derName" in form:
            if form["memberId"] != "":

                if validateFloat(form["derLatitude"]):
                    derLatitude = float(form["derLatitude"])

                if validateFloat(form["derLongitude"]):
                    derLongitude = float(form["derLongitude"])

                for community in communitiesMemory:
                    if haversineMeasure(community.coords[0], community.coords[1], derLatitude, derLongitude) <= 500:                        
                        member = Member(form["memberId"], form["name"], form["surname"], form["derLatitude"], form["derLongitude"], form["derName"], community.name)
                        print(isInMembersMemory(member))
                        if not isInMembersMemory(member):
                            membersMemory.append(member)
                            response = Response(json.dumps(member.toDict()), status=200, mimetype='application/json')
            else:
                response = Response(error400Message, status=400, mimetype='application/json')
        else:
            response = Response(error400Message, status=400, mimetype='application/json')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)