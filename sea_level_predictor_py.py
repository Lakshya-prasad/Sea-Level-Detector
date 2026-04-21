import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Import data
    df = pd.read_csv('data/epa-sea-level.csv')

    # 2. Scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, label='Observed Data')

    # 3. Line of best fit — full dataset (1880 to 2050)
    slope1, intercept1, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_full = range(df['Year'].min(), 2051)
    sea_level_full = [slope1 * y + intercept1 for y in years_full]
    ax.plot(years_full, sea_level_full, 'r', label='Best Fit (1880–2050)')

    # 4. Line of best fit — data from 2000 onwards (2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    sea_level_recent = [slope2 * y + intercept2 for y in years_recent]
    ax.plot(years_recent, sea_level_recent, 'g', label='Best Fit (2000–2050)')

    # 5. Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return
    plt.savefig('output/sea_level_plot.png')
    return plt.gca()
