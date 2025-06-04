# -*- coding: utf-8 -*-
#
# Рисует тернарную диаграмму БЖУ продуктов.

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('bju/bju.csv', encoding ='utf-8')

rawData = [
    {'journalist':75,'developer':25,'designer':0,'label':'point 1'},
    {'journalist':70,'developer':10,'designer':20,'label':'point 2'},
    {'journalist':75,'developer':20,'designer':5,'label':'point 3'},
    {'journalist':5,'developer':60,'designer':35,'label':'point 4'},
    {'journalist':10,'developer':80,'designer':10,'label':'point 5'},
    {'journalist':10,'developer':90,'designer':0,'label':'point 6'},
    {'journalist':20,'developer':70,'designer':10,'label':'point 7'},
    {'journalist':10,'developer':20,'designer':70,'label':'point 8'},
    {'journalist':15,'developer':5,'designer':80,'label':'point 9'},
    {'journalist':10,'developer':10,'designer':80,'label':'point 10'},
    {'journalist':20,'developer':10,'designer':70,'label':'point 11'},
];

def makeAxis(title, tickangle):
    return {
      'title': {'text': title, 'font': { 'size': 20}},
      'tickangle': tickangle,
      'tickfont': { 'size': 15 },
      'tickcolor': 'rgba(0,0,0,0)',
      'ticklen': 5,
      'showline': True,
      'showgrid': True
    }

fig = go.Figure(go.Scatterternary({
    'mode': 'markers',
    'a': df['B'],
    'b': df['J'],
    'c': df['U'],
    'text': df['Food'],
    'marker': {
        #'symbol': 100,
        'sizemode': 'diameter',
        'sizeref': 20,
        'sizemin': 3,
        'color': df['color'],
        'size': df['Kkal']
    }
}))

fig.update_layout({
    'ternary': {
        'sum': 100,
        'aaxis': makeAxis('Белки', 0),
        'baxis': makeAxis('Жиры', 45),
        'caxis': makeAxis('Углеводы', -45)
    }
})

fig.show()