# Travel Bucket List App

This was a solo project whilst studying with CodeClan with the brief of creating an app to track someone's travel adventures.

### Project Brief

The requirements for the project were to build an app allowing a user to:

- track cities and countries they want to visit and those they have visited
- create and edit countries
- each country should have one or more city
- create and delete entries
- mark destinations as visited or still to see

### Application Features:

- Create, track and log travel bucket list destinations
- Edit trips once they have been created
- Ability to create new cities and countries for a new trip
- Ability to mark destinations as visited
- Filter trips by viewing as past or future trips
- Filters trips by continent
- Delete trips

### Languages & Tools used:

- Python
- Flask (Jinja2)
- SQL
- HTML5
- CSS

### Running The App

##### Ensure Python and Flask are installed

- $ brew install python
- $ pip install Flask

##### Get the code

- $ git clone https://github.com/https://github.com/RebeccaRBell/travel_bucket_list

##### Create Database

- $ 'createdb' + 'database_name' in the terminal (original was named 'trips_manager')
- $ 'psql -d database_name -f trips_manager.sql'
- $ run python3 console.py in the terminal to add inbuilt trips

##### Run Flask

- $ in terminal, 'flask run' and command + click link in terminal to take to local server

### Wireframes

| Add Trip Page Wireframe                               |                  Trips Page Wireframe                   |
| ----------------------------------------------------- | :-----------------------------------------------------: |
| ![Add-Trip-Wireframe](/static/new_trip_wireframe.png) | ![All-Trips-Wireframe](/static/trip_page_wireframe.png) |

### Screenshots

| Add Trip Page                                   |                  Trips Page                   |
| ----------------------------------------------- | :-------------------------------------------: |
| ![Add-Trip-Page](/static/add_trip.png?raw=true) | ![All-Trips-Page](/static/trips.png?raw=true) |
