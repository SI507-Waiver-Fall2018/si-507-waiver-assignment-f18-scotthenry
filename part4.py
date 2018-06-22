
# coding: utf-8

# In[ ]:

#Stanley Scott Henry (schenry) 81390908

# Imports -- you may add others but do not need to
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

plotly.tools.set_credentials_file(username='sscotthenry', api_key='6IcW55SU1oaLaxoiHMk5')
# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

df = pd.read_csv('noun_data.csv')
df.head()

data = [
    go.Bar(
        x=df['Noun'],
        y=df['Number']
    )
]

fig = go.Figure(data = data)
py.image.save_as(fig, filename = "part4_viz_image.png")

