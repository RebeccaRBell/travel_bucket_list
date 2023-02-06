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


@trips_blueprint.route("/add_trip")
def new_trip():
    continents = continent_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template(
        "add_trip.html", continents=continents, countries=countries, cities=cities
    )


@trips_blueprint.route("/add_trip", methods=["POST"])
def create_trip():
    new_continent = request.form["continent"]
    new_country = request.form["country"]
    new_city = request.form["city"]
    new_reason = request.form["reason"]
    new_season = request.form["season"]
    new_timeframe = request.form["timeframe"]
    new_completed = request.form["completed"]
    new_trip = Trip(
        new_continent,
        new_country,
        new_city,
        new_reason,
        new_season,
        new_timeframe,
        new_completed,
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


@trips_blueprint.route("/past")
def past_trips():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template("past.html", trips=trips, countries=countries, cities=cities)


@trips_blueprint.route("/future")
def future_trips():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "future.html", trips=trips, countries=countries, cities=cities
    )


@trips_blueprint.route("/view_by_continent/europe")
def europe_trips():
    continent = 1
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )


@trips_blueprint.route("/view_by_continent/asia")
def asia_trips():
    continent = 2
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )


@trips_blueprint.route("/view_by_continent/africa")
def africa_trips():
    continent = 3
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )


@trips_blueprint.route("/view_by_continent/north_america")
def north_america_trips():
    continent = 4
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )


@trips_blueprint.route("/view_by_continent/south_america")
def south_america_trips():
    continent = 5
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )


@trips_blueprint.route("/view_by_continent/oceania")
def oceania_trips():
    continent = 6
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )


@trips_blueprint.route("/view_by_continent/antarctica")
def antarctica_trips():
    continent = 7
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    trips = trip_repository.select_all()
    return render_template(
        "show_trips_by_continent.html",
        continent=continent,
        countries=countries,
        cities=cities,
        trips=trips,
    )
