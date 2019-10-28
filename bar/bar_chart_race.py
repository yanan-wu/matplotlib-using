# -*- coding: utf-8 -*

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from matplotlib.font_manager import FontProperties
from IPython.display import HTML

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)


# def get_data():
#     df = pd.read_csv('../data/data.csv')
#     dff = df[df['week'].eq(4)].sort_values(by='value', ascending=True).head(5)
#     matplotlib.rcParams['font.family'] = 'SimHei'
#     fig, ax = plt.subplots(figsize=(15, 8))
#     colors = dict(zip(['A', 'B', 'C'], ['#adb0ff', '#ffb3ff', '#90d595']))
#     groups = df.set_index('name')['group'].to_dict()
#     dff = dff[::-1]
#     ax.barh(dff['name'], dff['value'], color=[colors[groups[x]] for x in dff['name']])
#     # 遍历这些值来绘制标签和值
#     for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
#         ax.text(value, i, name, ha='right')
#         ax.text(value, i-.25, groups[name], ha='right')
#         ax.text(value, i, value, ha='left')
#     ax.text(1, 0.4, 4, transform=ax.transAxes, size=46, ha='right')
#     plt.show()


def get_data2():
    df = pd.read_csv('../data/data.csv')
    matplotlib.rcParams['font.family'] = 'SimHei'
    fig, ax = plt.subplots(figsize=(15, 8))
    draw_barchart(4, df, ax)
    animator = animation.FuncAnimation(fig, draw_barchart, frames=4, fargs=(df, ax))
    HTML(animator.to_jshtml())


def draw_barchart(week, df, ax):
    dff = df[df['week'].eq(week)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    colors = dict(zip(['A', 'B', 'C'], ['#adb0ff', '#ffb3ff', '#90d595']))
    groups = df.set_index('name')['group'].to_dict()
    ax.barh(dff['name'], dff['value'], color=[colors[groups[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, groups[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i, f'{value:,.0f}', ha='left', va='center')
    ax.text(1, 0.4, week, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(1, 1.06, '战斗力', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    plt.box(False)
    plt.show()


get_data2()