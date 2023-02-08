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

country1 = Country("United Kingdom", continent1.id)
country2 = Country("France", continent1.id)
country3 = Country("Denmark", continent1.id)
country4 = Country("Portugal", continent1.id)
country5 = Country("South Korea", continent2.id)
country6 = Country("Japan", continent2.id)
country7 = Country("Vietnam", continent2.id)
country8 = Country("Morocco", continent3.id)
country9 = Country("South Africa", continent3.id)
country10 = Country("Canada", continent4.id)
country11 = Country("United States of America", continent4.id)
country12 = Country("Mexico", continent4.id)
country13 = Country("Argentina", continent5.id)
country14 = Country("Chile", continent5.id)
country15 = Country("New Zealand", continent6.id)
country16 = Country("Australia", continent6.id)
country_repository.save(country1)
country_repository.save(country2)
country_repository.save(country3)
country_repository.save(country4)
country_repository.save(country5)
country_repository.save(country6)
country_repository.save(country7)
country_repository.save(country8)
country_repository.save(country9)
country_repository.save(country10)
country_repository.save(country11)
country_repository.save(country12)
country_repository.save(country13)
country_repository.save(country14)
country_repository.save(country15)
country_repository.save(country16)

city1 = City("London", continent1.id, country1.id)
city2 = City("Paris", continent1.id, country2.id)
city3 = City("Copenhagen", continent1.id, country3.id)
city4 = City("Lisbon", continent1.id, country4.id)
city5 = City("Seoul", continent2.id, country5.id)
city6 = City("Tokyo", continent2.id, country6.id)
city7 = City("Hanoi", continent2.id, country7.id)
city8 = City("Marrakesh", continent3.id, country8.id)
city9 = City("Cape Town", continent3.id, country9.id)
city10 = City("Toronto", continent4.id, country10.id)
city11 = City("New York City", continent4.id, country11.id)
city12 = City("Oaxaca", continent4.id, country12.id)
city13 = City("Buenos Aires", continent5.id, country13.id)
city14 = City("Santiago", continent5.id, country14.id)
city15 = City("Wellington", continent6.id, country15.id)
city16 = City("Sydney", continent6.id, country16.id)
city_repository.save(city1)
city_repository.save(city2)
city_repository.save(city3)
city_repository.save(city4)
city_repository.save(city5)
city_repository.save(city6)
city_repository.save(city7)
city_repository.save(city8)
city_repository.save(city9)
city_repository.save(city10)
city_repository.save(city11)
city_repository.save(city12)
city_repository.save(city13)
city_repository.save(city14)
city_repository.save(city15)
city_repository.save(city16)

trip1 = Trip(
    continent1.id,
    country3.id,
    city3.id,
    "Sightseeing, Fashion, Culture",
    "Spring",
    "In the Next Year",
    "no",
)
trip2 = Trip(
    continent4.id,
    country11.id,
    city11.id,
    "Broadway, Sightseeing, Markets, Food",
    "Autumn",
    "In the Next 5 Years",
    "no",
)
trip3 = Trip(
    continent1.id,
    country2.id,
    city2.id,
    "Disneyland, Snails, Sightseeing",
    "Spring",
    "In the Next 2 Years",
    "no",
)
trip4 = Trip(
    continent5.id,
    country13.id,
    city13.id,
    "Culture, Art, Food",
    "Spring",
    "In the Next 5 Years",
    "no",
)

trip_repository.save(trip1)
trip_repository.save(trip2)
trip_repository.save(trip3)
trip_repository.save(trip4)
