import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) &
        (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw a distinctive line plot
    plt.figure(figsize=(18, 6))
    plt.plot(df, color='mediumseagreen')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()

    # Save and return the plot
    plt.savefig('line_plot.png')
    return plt.gcf()

def draw_bar_plot():
    # Create a bar chart with vibrant visuals
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar.index.year
    months_order = ["January", "February", "March", "April", "May", "June", "July", "August",
                    "September", "October", "November", "December"]
    df_bar['month'] = df_bar.index.strftime('%B')
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months_order)
    df_bar_pivot = df_bar.pivot_table(
        values='value',
        index='year',
        columns='month',
        aggfunc=np.mean
    )

    plt.figure(figsize=(12, 7))
    df_bar_pivot.plot(kind='bar', colormap='copper')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Year-wise Page Views Trends')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Save and return the plot
    plt.savefig('yearly_page_views.png')
    return plt.gcf()

def draw_box_plot():
    # Discover insights through elegant box plots
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                    "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months_order)

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(ax=axes[0], x='year', y='value', data=df_box, palette='Set2')
    sns.boxplot(ax=axes[1], x='month', y='value', data=df_box, order=months_order, palette='Set2')

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.tight_layout()

    # Save and return the plot
    plt.savefig('page_views_insights_boxplot.png')
    return plt.gcf()
