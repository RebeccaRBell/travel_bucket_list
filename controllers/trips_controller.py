from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import trip_repository

trips_blueprint = Blueprint("users", __name__)


@trips_blueprint.route("/trips")
def trips():
    trips = trip_repository.select_all()
    return render_template("trips.html", trips=trips)
