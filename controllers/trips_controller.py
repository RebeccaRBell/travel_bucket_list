from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import trip_repository
from repositories import city_repository
from repositories import country_repository

trips_blueprint = Blueprint("users", __name__)


@trips_blueprint.route("/trips")
def trips():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "trips.html", trips=trips, countries=countries, cities=cities
    )


@trips_blueprint.route("/trips/add_trip")
def new_trip():
    countries = country_repository.select_all()
    cities = city_repository.select_all()

    return render_template("add_trip.html", countries=countries, cities=cities)
