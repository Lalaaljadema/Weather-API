from flask import Flask, render_template
import pandas

app= Flask("__name__")

@app.route("/") # a decorator that decorates function below
def home():
    return render_template("home.html")  # automatically find the file in templates file

@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    temperature= 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__= "__main__":
    app.run(debug=True, port= 5001) # port so we can run multiple app