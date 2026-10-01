import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit using all the data, extended to 2050
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(1880, 2051))
    ax.plot(years_all, res_all.intercept + res_all.slope * years_all, 'r')

    # Line of best fit using data from year 2000 onward, extended to 2050
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()