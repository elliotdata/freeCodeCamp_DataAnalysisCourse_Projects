import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set figure autolayout to False to prevent the tight layout warning
plt.rcParams["figure.autolayout"] = False

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
BMI = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (BMI > 25).astype(int)

# Normalize data
df['cholesterol'] = df['cholesterol'].replace([1, 2, 3], [0, 1, 1])
df['gluc'] = df['gluc'].replace([1, 2, 3], [0, 1, 1])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # Save and return the figure
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                 & (df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975)))
                 & (df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975)))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap
    ax = sns.heatmap(corr, linewidths=.5, annot=True, fmt='.1f', mask=mask, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': .45, 'format': '%.2f'})

    # Save and return the figure
    fig.savefig('heatmap.png')
    return fig
