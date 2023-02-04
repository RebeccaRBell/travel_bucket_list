import pdb
from models.country import Country
from models.city import City
from models.trip import Trip
from models.continent import Continent

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.trip_repository as trip_repository
import repositories.continent_repository as continent_repository

continent1 = Continent("Europe")
continent2 = Continent("Asia")
continent3 = Continent("Africa")
continent4 = Continent("North America")
continent5 = Continent("South America")
continent6 = Continent("Oceania")
continent7 = Continent("Antarctica")
continent_repository.save(continent1)
continent_repository.save(continent2)
continent_repository.save(continent3)
continent_repository.save(continent4)
continent_repository.save(continent5)
continent_repository.save(continent6)
continent_repository.save(continent7)


country1 = Country("Italy", continent1.id)
country2 = Country("Spain", continent1.id)
country3 = Country("Austria", continent1.id)
country4 = Country("Portugal", continent1.id)
country5 = Country("France", continent1.id)
country_repository.save(country1)
country_repository.save(country2)
country_repository.save(country3)
country_repository.save(country4)
country_repository.save(country5)

city1 = City("Rome", continent1.id, country1.id)
city2 = City("Madrid", continent1.id, country2.id)
city3 = City("Vienna", continent1.id, country3.id)
city4 = City("Lisbon", continent1.id, country4.id)
city5 = City("Paris", continent1.id, country5.id)
city_repository.save(city1)
city_repository.save(city2)
city_repository.save(city3)
city_repository.save(city4)
city_repository.save(city5)

trip1 = Trip(
    continent1.id,
    city1.id,
    city1.country_id,
    "Food, Culture",
    "Spring",
    "In the next year",
)
trip2 = Trip(
    continent1.id,
    city2.id,
    city2.country_id,
    "Architecture, History",
    "Autumn",
    "In the next 2 years",
)
trip3 = Trip(
    continent1.id,
    city3.id,
    city3.country_id,
    "History, Scenery",
    "Winter",
    "In the next year",
)
trip_repository.save(trip1)
trip_repository.save(trip2)
trip_repository.save(trip3)
