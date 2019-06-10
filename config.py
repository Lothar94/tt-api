#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

dbType = "mysql"    # mysql | test

connection = {
    "host": "localhost",
    "port": 3036,
    "username": "root",
    "password": "",
    "database": "tt-api"
}

error400Message = json.dumps({"code": 400, "error": "Bad Form"})
