from db.run_sql import run_sql
from models.country import Country
from models.city import City
from models.trip import Trip
from models.continent import Continent
from controllers import trips_controller


def save(trip):
    sql = "INSERT INTO trips ( continent_id, country_id, city_id, reason, season, timeframe, completed) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        trip.continent_id,
        trip.country_id,
        trip.city_id,
        trip.reason,
        trip.season,
        trip.timeframe,
        trip.completed,
    ]
    results = run_sql(sql, values)
    trip.id = results[0]["id"]
    return trip


def select_all():
    trips = []

    sql = "SELECT * FROM trips"
    results = run_sql(sql)

    for result in results:
        trip = Trip(
            result["continent_id"],
            result["country_id"],
            result["city_id"],
            result["reason"],
            result["season"],
            result["timeframe"],
            result["completed"],
            result["id"],
        )
        trips.append(trip)
    return trips


def select(id):
    trip = None
    sql = "SELECT * FROM trips WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        trip = Trip(
            result["continent_id"],
            result["country_id"],
            result["city_id"],
            result["reason"],
            result["season"],
            result["timeframe"],
            result["completed"],
            result["id"],
        )
    return trip


def delete_all():
    sql = "DELETE  FROM trips"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM trips WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(trip):
    sql = "UPDATE trips SET (continent_id, country_id, city_id, reason, season, timeframe, completed) = (%s, %s, %s, %s, %s, %s %s) WHERE id = %s"
    values = [
        trip.continent_id,
        trip.country_id,
        trip.city_id,
        trip.reason,
        trip.season,
        trip.timeframe,
        trip.completed,
    ]
    run_sql(sql, values)


def mark_visited(id):
    trip = None
    sql = "SELECT * FROM trips WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        trip = Trip(
            result["continent_id"],
            result["country_id"],
            result["city_id"],
            result["reason"],
            result["season"],
            result["timeframe"],
            "yes",
            result["id"],
        )
    return trip
