#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify


hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}

@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    numClass = len(hbnbText)
    for key, value in hbnbText:
        jsonify("{}{}".format(key, storage.count(value)))

if __name__ == "__main__":
    pass
