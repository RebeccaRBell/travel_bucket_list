DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
        name VARCHAR(255),
        id SERIAL PRIMARY KEY
);
CREATE TABLE cities (
        name VARCHAR(255),
        country_id INT NOT NULL REFERENCES countries(id),
        id SERIAL PRIMARY KEY
);
CREATE TABLE trips (
        city_id INT NOT NULL REFERENCES cities(id),
        country_id INT NOT NULL REFERENCES countries(id),
        reason TEXT,
        season VARCHAR(255),
        timeframe VARCHAR(255),
        id SERIAL PRIMARY KEY
);