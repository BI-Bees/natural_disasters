import pandas as pd

from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import RangeSlider, Button, DataTable, TableColumn, NumberFormatter
from bokeh.io import curdoc

df = pd.read_csv("natural_disasters/CSV/disasters.csv")

source = ColumnDataSource(data=dict())

def update():
    current = df[(df['year'] >= slider.value[0]) & (df['year'] <= slider.value[1])].dropna()
    source.data = {
        'year'                    : current.year,
        'disaster_type'           : current.disaster_type,
        'occurrences'             : current.occurrence,
        'Injured'                 : current.Injured,
        'Total_deaths'            : current.Total_deaths,
        'Total_damage'            : current["Total_damage ('000 US$)"]
    }

slider = RangeSlider(title="Year", start=1985, end=2017, value=(1985, 2017), step=1, format="0")
slider.on_change('value', lambda attr, old, new: update())

columns = [
    TableColumn(field="year", title="Year"),
    TableColumn(field="disaster_type", title="Disaster type"),
    TableColumn(field="occurrences", title="Occurrence"),
    TableColumn(field="Injured", title="Injured"),
    TableColumn(field="Total_deaths", title="Total deaths"),
    TableColumn(field="Total_damage", title="Total damage ('000 US$)")
]

data_table = DataTable(source=source, columns=columns, width=1000)

controls = widgetbox(slider)
table = widgetbox(data_table)

curdoc().add_root(row(controls, table))
curdoc().title = "Disaster table"

update()