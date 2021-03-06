import math
import pandas as pd
import app.visualizer as visual 
from bokeh.io import show, output_file, curdoc
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure
from bokeh.palettes import inferno
from bokeh.embed import components

def createBar():
    temp_dict = visual.read_csv('natural_disasters/CSV/disasters.csv')
    df = pd.DataFrame(temp_dict)
    df_sumed = df.groupby(['year']).sum()

    result = list(zip(df_sumed.index, df_sumed.occurrence))

    years = list([str(val[0]) for val in result])
    occurrences = list([val[1] for val in result])

    source = ColumnDataSource(data=dict(years=years, occurrences=occurrences, color=inferno(97)))

    p = figure(x_range=years, y_range=(0,40), plot_height=500, plot_width=1000, title="Natural Disasters", toolbar_location=None, tools="")

    p.vbar(x='years', top='occurrences', width=0.5, color='color', source=source)
    p.xaxis.major_label_orientation = math.pi/2

    label = LabelSet(x='years', y='occurrences', text='occurrences', level='glyph', text_font_size='0.8em', text_align='center', source=source, render_mode='canvas')

    p.xgrid.grid_line_color = None
    p.add_layout(label)
    script, div = components(p)
    return (script, div)