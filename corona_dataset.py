
# Import Libraries and Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset1 = pd.read_csv("2019_nC0v_20200121_20200126 - SUMMARY.csv")
dataset2 = pd.read_csv("2019_nC0v_20200121_20200126_cleaned.csv")
dataset3 = pd.read_csv("2019_nCoV_20200121_20200127.csv")
dataset4 = pd.read_csv("2019_nCoV_20200121_20200128.csv")
dataset5 = pd.read_csv("2019_nCoV_20200121_20200130.csv")
dataset6 = pd.read_csv("2019_nCoV_20200121_20200131.csv")
dataset7 = pd.read_csv("2019_nCoV_20200121_20200201.csv")
dataset8 = pd.read_csv("2019_nCoV_20200121_20200205.csv")
dataset9 = pd.read_csv("2019_nCoV_20200121_20200206.csv")


dataset2 = dataset2.iloc[:,1:7]
# Create a new Dataset
New_Dataset = pd.concat([dataset2, dataset3, dataset4, dataset5, dataset6, dataset7, dataset8, dataset9])
New_Dataset.shape

# Take out the missing values
nullseries = New_Dataset.isnull().sum()
New_Dataset = New_Dataset[New_Dataset["Province/State"].notnull()]
New_Dataset = New_Dataset[New_Dataset["Suspected"].notnull()]
New_Dataset = New_Dataset[New_Dataset["Recovered"].notnull()]
New_Dataset = New_Dataset[New_Dataset["Province/State"]!= "0"]

# Visualization Dataset
Sorting = New_Dataset.sort_values("Province/State")
Break = pd.pivot_table(data = Sorting, index = ["Province/State"],values = ["Recovered","Suspected"], aggfunc = "max")
Break = Break.reset_index(level = "Province/State")

# The Visualization of the Dataset obtained in here. 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xlabel = Break["Province/State"]
ax.plot(xlabel, Break["Suspected"], "r-", label = "Suspected")
ax.legend(loc = 0)
ax.set_xlabel('Province / State')
ax.set_xticklabels(xlabel, rotation = 90)
ax.set_ylabel('Number of Suspected')
ax.set_title("Province / State vs Number of Suspected")
ax.grid(True)
ax2 = ax.twinx()
ax2.plot(xlabel, Break["Recovered"], "b-", label = "Recovered")
ax2.set_ylabel('Number of Recovered')
ax2.legend(loc =1)

# Showing the Table
Break.sort_values(["Suspected","Recovered"])
