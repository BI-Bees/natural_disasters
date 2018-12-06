from flask import Flask, request, render_template, session, redirect, send_file
import app.pygal_graph as pg
import app.natural_disasters_graph as ndg

app = Flask(__name__)

# Used as main page
@app.route('/')
def home_page():
    return render_template("main_page.html")

# Route that shows all bar graphs we have
@app.route('/bokeh_bar')
def bokeh_bar_page():
    bars = ndg.createBar()
    return render_template("bars.html", script=bars[0], div=bars[1])

@app.route('/pygal_bar')
def pygal_bar_page():
    bar = pg.render_chart()
    return render_template("pygal_bar.html", data=bar.render_data_uri())

if __name__ == "__main__":
    app.run(host='0.0.0.0')