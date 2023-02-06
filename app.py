from flask import Flask, render_template
from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.trips_controller import trips_blueprint

app = Flask(__name__)


app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(trips_blueprint)


@app.route("/")
def opening():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("base.html")


@app.route("/add_trip")
def add_trip_page():
    return render_template("add_trip.html")


@app.route("/past")
def past_trips():
    return render_template("past.html")


@app.route("/future")
def future_trips():
    return render_template("future.html")


@app.route("/view_by_continent")
def trips_by_continent():
    return render_template(
        "continent_trips.html",
    )


if __name__ == "__main__":
    app.run(debug=True)
