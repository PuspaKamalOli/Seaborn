import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# 1.heatmap
# corr correlates rows and colum and converts into matrix
tip = tips.corr()
sns.heatmap(tip, annot=True)

flights = sns.load_dataset('flights')
flights.head()
# pivot_table re writes table with given arguments and make it easy for matrix plot
flight = flights.pivot_table(values='passengers', index='year', columns='month')
sns.heatmap(flight, annot=True, linewidth=2, linecolor='white', cmap='coolwarm')
# 2.cluster map
# cluster map shows the cluster the most related data as well
sns.clustermap(flight, annot=True, linewidth=2,
               linecolor='white', cmap='magma', standard_scale=1)
