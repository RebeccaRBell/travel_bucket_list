from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import trip_repository
from repositories import city_repository
from repositories import country_repository
from repositories import continent_repository
from models.trip import Trip
from models.city import City
from models.country import Country

trips_blueprint = Blueprint("users", __name__)


@trips_blueprint.route("/trips")
def trips():
    continents = continent_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "trips.html",
        trips=trips,
        countries=countries,
        cities=cities,
        continents=continents,
    )


@trips_blueprint.route("/trips/add_trip")
def new_trip():
    continents = continent_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template(
        "add_trip.html", continents=continents, countries=countries, cities=cities
    )


@trips_blueprint.route("/trips/add_trip", methods=["POST"])
def create_trip():
    new_continent = request.form["continent"]
    new_country = request.form["country"]
    new_city = request.form["city"]
    new_reason = request.form["reason"]
    new_season = request.form["season"]
    new_timeframe = request.form["timeframe"]
    new_trip = Trip(
        new_continent, new_country, new_city, new_reason, new_season, new_timeframe
    )
    trip_repository.save(new_trip)
    return redirect("/trips")


@trips_blueprint.route("/trips/<id>/delete")
def delete_trip(id):
    trip_repository.delete(id)
    return redirect("/trips")


@trips_blueprint.route("/add_new_city_country", methods=["POST"])
def create_new_city():
    new_continent = request.form["new_city_continent"]
    new_country = request.form["new_city_country"]
    new_city = request.form["new_city_name"]
    new_city_country = Country(new_country, new_continent)
    country_repository.save(new_city_country)
    add_new_city = City(new_city, new_continent, new_city_country.id)
    city_repository.save(add_new_city)
    return redirect("/trips")
