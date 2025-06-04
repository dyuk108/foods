# -*- coding: utf-8 -*-
#
# Рисует 3D диаграмму БЖУ продуктов.

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('bju/bju.csv', encoding ='utf-8')

fig = go.Figure(data=go.Scatter3d(
    x=df['U'],
    y=df['J'],
    z=df['B'],
    text=df['Food'],
    mode='markers',
    marker=dict(
        sizemode='diameter',
        sizeref=20,
        sizemin = 10,
        size=df['Kkal'],
        color = df['color'],
        line_color='rgb(140, 140, 170)'
    )
))

fig.update_layout(
    #width=1000,
    #height=1500,
    title=dict(text="###"),
    scene=dict(
        xaxis=dict(
            title=dict(
                text="Углеводы",
                font=dict(
                    color="#303030"
                )
            )
        ),
        yaxis=dict(
            title=dict(
                text="Жиры",
                font=dict(
                    color="#303030"
                )
            )
        ),
        zaxis=dict(
            title=dict(
                text="Белки",
                font=dict(
                    color="#303030"
                )
            )
        ),
        # bgcolor="rgb(20, 24, 54)"
    )
)

# Самодельная легенда (здесь не нужен colorbar).
# winds = ['северный', 'восточный', 'южный', 'западный']
# for i in range(len(colors)):
#     htmlText += "<span style='color: " + colors[i] + "; font-size: 20'>\\u25A0</span> " + winds[i] + " &nbsp;"

# config = {'displayModeBar': False}
# s = fig.to_html(config=config, include_plotlyjs = 'cdn', 
#             full_html = False, div_id = 'bl' + str(year))
# s = s.replace('bot-title', htmlText)

fig.show()