import pdb
from models.country import Country
from models.city import City
from models.trip import Trip

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.trip_repository as trip_repository

country1 = Country("Italy")
country_repository.save(country1)
country2 = Country("Spain")
country_repository.save(country2)

city1 = City("Rome", country1.id)
city_repository.save(city1)
city2 = City("Madrid", country2.id)
city_repository.save(city2)

trip1 = Trip(city1.id, city1.country_id, "Food, Culture", "Spring", "In the next year")
trip_repository.save(trip1)
