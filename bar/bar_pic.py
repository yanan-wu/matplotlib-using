# -*- coding: utf-8 -*

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)


def per_share():
    """
    每股收益-年份柱状图
    :return:
    """
    csv_data = pd.read_csv('../data/000988_data.csv', index_col=0, names=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    x = csv_data.iloc[:1].values.tolist()[0][::-1]
    y = csv_data.iloc[1:2].values.tolist()[0][::-1]
    print(x)
    plt.bar(range(9), y, width=0.5)
    plt.plot(range(9), y, color='red')
    plt.xticks(range(9), x, rotation=20)

    plt.title('华工科技历年每股收益变化图', fontproperties=font_set)
    plt.legend()
    plt.xlabel('年份', fontproperties=font_set)
    plt.ylabel('基本每股收益(元)', fontproperties=font_set)
    plt.savefig('D:/share.png', dpi=200, bbox_inches='tight')
    plt.show()


def roe_pic():
    """
    净资产收益率-年份柱状图
    :return:
    """
    csv_data = pd.read_csv('../data/300414_data.csv', index_col=0, names=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    x = csv_data.iloc[:1].values.tolist()[0][::-1]
    y = csv_data.iloc[1:2].values.tolist()[0][::-1]
    plt.bar(range(8), y, width=0.5, color='green')
    plt.plot(range(8), y, color='red')
    plt.xticks(range(8), x, rotation=20)

    plt.title('中光防雷历年 ROE 变化图', fontproperties=font_set)
    plt.legend()
    plt.xlabel('年份', fontproperties=font_set)
    plt.ylabel('ROE(%)', fontproperties=font_set)
    plt.savefig('D:/roe.png', dpi=200, bbox_inches='tight')
    plt.show()

roe_pic()
