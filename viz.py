import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

wine_colors = ['#efdaa3', '#8c0f0a']
alt_white = '#eccd13'
wine_palette = sns.color_palette(wine_colors)
wine_palette_r = sns.color_palette(list(reversed(wine_colors)))

def abv_boxen_by_quality(df):
    plt.figure(figsize=[10,5])
    sns.boxenplot(data=df, x='quality', y='alcohol')
    plt.title('%ABV is most important variable to consider when making a wine.')
    plt.show()

def not_us_legal(row):
    legal = True
    if row.total_sulfur_dioxide > 350: legal = False
    if row.type == 'red':
        if row.volatile_acidity > 1.4: legal = False
    else:
        if row.volatile_acidity > 1.5: legal = False
    return not legal

def not_eu_legal(row):
    legal = False
    sugar = row.residual_sugar
    so2 = row.total_sulfur_dioxide
    acetic = row.volatile_acidity
    if row.type == 'red':
        if acetic > 1.2: 
            return not legal
        if sugar < 5 and so2 > 150: 
            return not legal
        if 5 < sugar < 35 and so2 > 250: 
            return not legal
    else:
        if acetic > 1.08: 
            return not legal
        if sugar < 5 and so2 > 200: 
            return not legal
        if 5 < sugar < 35 and so2 > 250: 
            return not legal
        if 35 < sugar and so2 > 400: 
            return not legal
    return legal

def regplot_compare(train, x, y):
    fig, axes = plt.subplots(1,2, sharey=True,sharex=True, figsize=[8,4])
    sns.regplot(x=x, y=y, data=train[train.type =='white'],
                x_estimator=np.mean, logx=True,
                color= alt_white, label='White', ax=axes[0],
                )
    sns.regplot(x=x, y=y, data=train[train.type =='red'],
                x_estimator=np.mean, logx=True,
                color= wine_colors[1], label='Red', ax=axes[1]
                )
    fig.legend()
    fig.suptitle(f'{y.capitalize()} / {x.capitalize()} comparison')
    plt.show()