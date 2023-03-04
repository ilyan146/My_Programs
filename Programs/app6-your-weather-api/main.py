from flask import Flask, render_template
import pandas as pd

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

if __name__ == "__main__":
    app.run(debug=True)