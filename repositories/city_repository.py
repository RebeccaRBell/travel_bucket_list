from db.run_sql import run_sql
from models.trip import Trip
from models.country import Country
from models.city import City


def save(city):
    sql = "INSERT INTO cities(name, country_id) VALUES ( %s, %s) RETURNING id"
    values = [city.name, city.country_id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row["name"], row["country_id"], row["id"])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(row["name"], row["country_id"], row["id"])
    return city


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)
