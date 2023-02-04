from db.run_sql import run_sql
from models.country import Country
from models.city import City
from models.trip import Trip
from repositories import trip_repository
from repositories import city_repository
from repositories import country_repository


def save(trip):
    sql = "INSERT INTO trips(continent_id, country_id, city_id, reason, season, timeframe) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        trip.continent_id,
        trip.country_id,
        trip.city_id,
        trip.reason,
        trip.season,
        trip.timeframe,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    trip.id = id
    return trip


def select_all():
    trips = []

    sql = "SELECT * FROM trips"
    results = run_sql(sql)

    for row in results:
        trip = Trip(
            row["continent_id"],
            row["country_id"],
            row["city_id"],
            row["reason"],
            row["season"],
            row["timeframe"],
            row["id"],
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
            row["continent_id"],
            row["country_id"],
            row["city_id"],
            row["reason"],
            row["season"],
            row["timeframe"],
            row["id"],
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
    sql = "UPDATE trips SET (continent_id, country_id, city_id, reason, season, timeframe) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        trip.continent_id,
        trip.country_id,
        trip.city_id,
        trip.reason,
        trip.season,
        trip.timeframe,
    ]
    run_sql(sql, values)
