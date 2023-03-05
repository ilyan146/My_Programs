from flask import Flask, render_template
import pandas as pd
import matplotlib as plot

app = Flask(__name__)

stations_df = pd.read_csv("003 data-small/stations.txt", skiprows=17)
stations_df = stations_df[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations_df.to_html())
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "003 data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"Station": station,
            "Date": date,
            "Temperature": temperature}
@app.route("/api/v1/<station>/")
def one_station_all(station):
    filename = "003 data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result
@app.route("/api/v1/yearly/<station>/<year>/")
def year(station, year):
    filename = "003 data-small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True)