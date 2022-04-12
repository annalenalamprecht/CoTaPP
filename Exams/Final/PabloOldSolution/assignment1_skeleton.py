import pandas as pd
import matplotlib.pyplot as plt
import time

def get_number_of_runs(dataframe):
    return len(dataframe)

def get_number_of_marathons_and_ultras(dataframe):
    n_mar, n_ult = 0, 0
    d_mar = 42.195
    for d in dataframe['Distance']:
        if d == d_mar:
            n_mar += 1
        elif d > d_mar:
            n_ult += 1
        else:
            print('WARNING: short race')
    return n_mar, n_ult

def get_longest_distance(dataframe):
    return dataframe['Distance'].max()

def get_total_distance(dataframe):
    return dataframe['Distance'].sum()

def draw_barchart_of_km_per_year(dataframe):
    years = []
    for date in dataframe['Date']:
        year = date.split('/')[2]
        years.append(year)
    dataframe['Year'] = years
    dataframe.groupby('Year')['Distance'].sum().plot(kind='bar')
    plt.show()

def get_three_fastest_marathons(dataframe):
    return dataframe[dataframe['Distance'] == 42.195].sort_values(
        'Time', ascending=True
    ).head(3)

def draw_histogram_of_times(dataframe):
    dataframe['Time'] = pd.to_timedelta(dataframe['Time'])
    entire_time_span = dataframe['Time'].max() - dataframe['Time'].min()
    n_bins = int(entire_time_span / pd.Timedelta(minutes=15) + 0.5)
    #print('bins:', n_bins)
    #print(type(dataframe['Time'].tolist()[0]))
    (dataframe['Time'].astype('timedelta64[s]') / 60).hist(bins=n_bins)
    plt.show()

def get_number_of_countries(dataframe):
    return dataframe['Country'].nunique()

def draw_piechart_of_countries(dataframe):
    dataframe.groupby('Country').count().plot.pie(y='Distance')
    plt.show()

#################################
# MAIN PROGRAM (do not change!) #
#################################

if __name__ == "__main__":
    
    # read the date from the file into a dataframe
    df = pd.read_csv("run_statistics.csv")
   
    # number of runs
    n_runs = get_number_of_runs(df)
    print(f"This runner has completed {n_runs} long-distance runs.")
    
    # number normal marathons and ultras
    n_marathons, n_ultras = get_number_of_marathons_and_ultras(df)
    print(f"{n_marathons} marathons and {n_ultras} ultra-marathons, to be precise.")
        
    # longest
    d_longest = get_longest_distance(df)
    print(f"The longest run was {d_longest} km.")
    
    # total km
    d_total = get_total_distance(df)
    print(f"The total distance run is {d_total:.3f} km.")
    print()
    
    # three fastest marathons
    three_fastest = get_three_fastest_marathons(df)
    print("The fastest three marathons were:")
    print(three_fastest)
    print()
    
    # histogram of marathon times
    draw_histogram_of_times(df)
    
    # bar chart of km/year
    draw_barchart_of_km_per_year(df)
        
    # number of countries
    n_countries = get_number_of_countries(df)
    print(f"The runner has completed runs in {n_countries} countries.")
    
    # pie chart of countries
    draw_piechart_of_countries(df)
    