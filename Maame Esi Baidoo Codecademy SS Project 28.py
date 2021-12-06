import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
#Inspecting the data
print(healthcare.head())
print(healthcare["DRG Definition"].unique())
#Selecting rows from the dataframe where the diagnosis is for seizures
seizures = healthcare[healthcare["DRG Definition"] == "101 - SEIZURES W/O MCC"]
#Selecting seizure diagnosis that are in Georgia
georgia_seizure = seizures[seizures["Provider State"] == "GA"]
#Selecting the costs for seizure diagnosis in Georgia
costs = georgia_seizure[" Average Covered Charges "].values
#Drawing a boxplot for costs in Georgia
#plt.boxplot(costs)
#plt.show()
#Selecting all the different states in the seizures dataframe
states = seizures["Provider State"].unique()
#print(states)
#Getting the dataset of costs for each state
datasets = []
for state in states:
  datasets.append(seizures[seizures["Provider State"] == state][" Average Covered Charges "].values)
#print(datasets)
#Drawing a histogram for each state
plt.figure(figsize = (20, 6))
plt.boxplot(datasets, labels = states)
plt.show()