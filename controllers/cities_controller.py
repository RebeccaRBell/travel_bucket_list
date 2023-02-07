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
    countries = country_repository.select_all()
    return render_template(
        "new_city_country.html", continents=continents, countries=countries
    )


@cities_blueprint.route("/add_new_city_country", methods=["POST"])
def create_new_city():
    new_continent = request.form["new_city_continent"]
    new_city = request.form["new_city_name"]
    if request.form["new_city_country"] == "":
        existing_country = request.form["city_country"]
        add_new_city = City(new_city, new_continent, existing_country)
        city_repository.save(add_new_city)
    else:
        new_country = request.form["new_city_country"]
        save_new_country = Country(new_country, new_continent)
        country_repository.save(save_new_country)
        add_new_city_and_country = City(new_city, new_continent, save_new_country.id)
        city_repository.save(add_new_city_and_country)
    return redirect("/add_trip")
