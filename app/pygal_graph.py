import pygal
import pandas as pd
import visualizer as visual 
from pygal.style import Style

temp_dict = visual.read_csv('../CSV/disasters.csv')
df = pd.DataFrame(temp_dict)
list_year = df['year'].tolist()
list_injured = df['Injured'].tolist()
list_deaths = df['Total_deaths'].tolist()


custom_style = Style(
  colors=('#E80080', '#404040', '#9BC850'))

b_chart = pygal.Line(style=custom_style, width=1500)
b_chart.title = "Disasters"
b_chart.x_labels = list_year
b_chart.add("Injured", list_injured)
b_chart.add("Total deaths", list_deaths)
b_chart.render_in_browser()