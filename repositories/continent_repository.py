from db.run_sql import run_sql
from models.country import Country
from models.city import City
from models.trip import Trip
from models.continent import Continent
from repositories import trip_repository
from repositories import city_repository
from repositories import country_repository


def save(continent):
    sql = "INSERT INTO continents (name) VALUES ( %s) RETURNING id"
    values = [continent.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    continent.id = id
    return continent


def select_all():
    continents = []

    sql = "SELECT * FROM continents"
    results = run_sql(sql)

    for row in results:
        continent = Continent(
            row["name"],
            row["id"],
        )
        continents.append(continent)
    return continents


def select(id):
    continent = None
    sql = "SELECT * FROM continents WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        continent = continent(
            row["name"],
            row["id"],
        )
    return continent


def delete_all():
    sql = "DELETE  FROM continents"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM continents WHERE id = %s"
    values = [id]
    run_sql(sql, values)
