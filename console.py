import pdb
from models.country import Country
from models.city import City
from models.trip import Trip

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.trip_repository as trip_repository

country1 = Country("Italy")
country2 = Country("Spain")
country3 = Country("Austria")
country4 = Country("Portugal")
country5 = Country("France")
country_repository.save(country1)
country_repository.save(country2)
country_repository.save(country3)
country_repository.save(country4)
country_repository.save(country5)

city1 = City("Rome", country1.id)
city2 = City("Madrid", country2.id)
city3 = City("Vienna", country3.id)
city4 = City("Lisbon", country4.id)
city5 = City("Paris", country5.id)
city_repository.save(city1)
city_repository.save(city2)
city_repository.save(city3)
city_repository.save(city4)
city_repository.save(city5)

trip1 = Trip(city1.id, city1.country_id, "Food, Culture", "Spring", "In the next year")
trip2 = Trip(
    city2.id, city2.country_id, "Architecture, History", "Autumn", "In the next 2 years"
)
trip3 = Trip(
    city3.id, city3.country_id, "History, Scenery", "Winter", "In the next year"
)
trip_repository.save(trip1)
trip_repository.save(trip2)
trip_repository.save(trip3)
pdb.set_trace()
