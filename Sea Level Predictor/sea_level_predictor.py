import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the dataset
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 8))
    df.plot(x="Year", y="CSIRO Adjusted Sea Level", kind="scatter", ax=ax, color="blue", alpha=0.7, s=40)

    # Calculate and plot the first line of best fit
    x_fit_1 = range(df["Year"].iloc[0], 2051, 1)  
    slope_1, intercept_1, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    line_fit_1 = intercept_1 + slope_1 * x_fit_1
    plt.plot(x_fit_1, line_fit_1, color="red", linestyle="--", label="Best Fit Line 1880-2050")

    # Calculate and plot the second line of best fit
    x_fit_2 = range(2000, 2051, 1)  
    slope_2, intercept_2, _, _, _ = linregress(df[df["Year"] >= 2000]["Year"], df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    line_fit_2 = intercept_2 + slope_2 * x_fit_2
    plt.plot(x_fit_2, line_fit_2, color="green", linestyle="--", label="Best Fit Line 2000-2050")

    # Confidence interval shading for the second line of best fit
    ci_upper = line_fit_2 + 0.1
    ci_lower = line_fit_2 - 0.1
    plt.fill_between(x_fit_2, ci_lower, ci_upper, color="lightgreen", alpha=0.3, label="Confidence Interval")

    # Set labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Add legend and grid
    plt.legend()
    plt.grid(True)

    # Save the plot and return the current Axes instance
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to generate the plot
draw_plot()
