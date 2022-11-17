#compare all the columns of dataset in histogram and scatter plot
import seaborn as sns
tips = sns.load_dataset('tips')
sns.pairplot(tips,hue='sex',palette='coolwarm')