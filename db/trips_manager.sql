DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;
CREATE TABLE continents(name VARCHAR(255), id SERIAL PRIMARY KEY);
CREATE TABLE countries (
        name VARCHAR(255),
        continent_id INT NOT NULL REFERENCES continents(id),
        id SERIAL PRIMARY KEY
);
CREATE TABLE cities (
        name VARCHAR(255),
        continent_id INT NOT NULL REFERENCES continents(id),
        country_id INT NOT NULL REFERENCES countries(id),
        id SERIAL PRIMARY KEY
);
CREATE TABLE trips (
        continent_id INT NOT NULL REFERENCES continents(id),
        country_id INT NOT NULL REFERENCES countries(id),
        city_id INT NOT NULL REFERENCES cities(id),
        reason TEXT,
        season VARCHAR(255),
        timeframe VARCHAR(255),
        completed VARCHAR(255),
        id SERIAL PRIMARY KEY
);
