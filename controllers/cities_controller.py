from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import trip_repository
from repositories import city_repository
from repositories import country_repository
from repositories import continent_repository
from models.trip import Trip
from models.city import City
from models.country import Country

cities_blueprint = Blueprint("cities", __name__)


@cities_blueprint.route("/add_new_city_country")
def add_city_country():
    continents = continent_repository.select_all()
    return render_template("new_city_country.html", continents=continents)


@cities_blueprint.route("/add_new_city_country", methods=["POST"])
def create_new_city():
    new_continent = request.form["new_city_continent"]
    new_country = request.form["new_city_country"]
    new_city = request.form["new_city_name"]
    countries = country_repository.select_all()
    if countries.count(new_country):
        new_city_country = new_country["id"]
    else:
        new_city_country = Country(new_country, new_continent)
    country_repository.save(new_city_country)
    add_new_city = City(new_city, new_continent, new_city_country.id)
    city_repository.save(add_new_city)
    return redirect("/trips/add_trip")
