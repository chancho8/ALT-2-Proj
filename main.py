import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt

def plot_ages_vs_rates(make, df, color, fig, ax, show_scatter):
    vehicleMakesUnedited = df['Vehicle Make'].tolist()


    indexStart = 0      #Start of the group in which selected vehicle make is
    indexStop = 0       #End of the group in which selected vehicle make is
    makes = []          #List of the selected Make
    failRates = []      #List of the failrates of the selected make
    totals = []         #List of the totals of the cars tested
    ages = []           #list of the ages of the makes

    for i in range(len(vehicleMakesUnedited)):
        # Initialize indexStart at the first instance of the selected make
        if vehicleMakesUnedited[i] == make and vehicleMakesUnedited[i - 1] != make:
            indexStart = i
        # Initialize indexStop at the last continuous instance of the selected make
        elif vehicleMakesUnedited[i] == make and vehicleMakesUnedited[i + 1] != make:
            indexStop = i
            #append the values under the selected make onto our lists
            for j in range(indexStart, indexStop):
                ages.append(2020 - df['Year Of Birth'].tolist()[j])
                makes.append(df['Vehicle Make'].tolist()[j])
                failRates.append(df['FAIL %'].tolist()[j])
                totals.append(df['Total'].tolist()[j])

    i = 0
    while True:
        if i + 1 == len(totals):
            break
        if totals[i] <= 20:     #Remove all instances of models with less than 20 total tests
            del totals[i]
            del makes[i]
            del failRates[i]
            del ages[i]
        else:
            i += 1

    #Create a linear regression based off of the given data
    failRates_model = numpy.poly1d(numpy.polyfit(ages, failRates, 1))
    failRates_line = numpy.linspace(0, 35, 100)

    plt.plot(failRates_line, failRates_model(failRates_line), color=color,label=make)

    if show_scatter == True:
        ax.scatter(ages, failRates, color=color)

def compare(make1, make2, df , show_scatter):       #Compares the fail rate vs age of two makes of car
    fig, ax = plt.subplots()

    plot_ages_vs_rates(make1, df, 'blue', fig, ax, show_scatter)
    plot_ages_vs_rates(make2, df, 'red', fig, ax, show_scatter)

    plt.title(make1 + " vs " + make2)
    plt.xlabel("Age in years")
    plt.ylabel("Percent Fail rate")
    plt.ylim([0,100])
    plt.legend()
    plt.show()


df2020 = pd.read_excel('2020-Make-and-model-data-(xls).xlsx')
df2019 = pd.read_csv('Excel and csv files/2019-Make-Model-Data-(xls).csv')
df2018 = pd.read_csv('Excel and csv files/2018-Make-Model-Data-(csv).csv')
df2017 = pd.read_excel('2017-Make-Model-Data-(xls).xlsx')
df2015 = pd.read_excel('2015-Make-Model-Data-(xls).xlsx')

frames = [df2020, df2019, df2018, df2017, df2015]
total = pd.concat(frames, ignore_index=True)
compare("FORD","TOYOTA", total, show_scatter=False)
