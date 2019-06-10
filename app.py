#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, Response
from models.community import Community
from models.member import Member
from config import dbType

import json
app = Flask(__name__)

communitiesMemory = []                # Test mode
membersMemory = []                    # Test mode

error400Message = json.dumps({"code": 400, "error": "Bad Form"})

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
        if "name" in form:
            if form["name"] != "":
                community = Community(form["name"], form["description"], form["latitude"], form["longitude"], form["gestorId"])
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

        if "name" in form:
            if form["name"] != "":
                for community in communitiesMemory:
                    if community.name == name:
                        community.setCoords([form["latitude"], form["longitude"]])
                        community.setDescription(form["description"]) 
                        community.setGestorId(form["gestorId"])

                        response = Response(json.dumps(community.toDict()), status=200, mimetype='application/json')
            else:
                response = Response(error400Message, status=400, mimetype='application/json')
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

    print(communitiesMemory)
    return response

@app.route("/communities/<communityId>/members", methods=["POST"])
def communitiesInscription(communityId):
    return "Inscripción de miembro en la comunidad " + communityId

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)