#helps to compare two rows or condition with histogram and scatter plot or othermethods
import seaborn as sns
tips = sns.load_dataset('tips')
sns.jointplot(x='tip', y='size', data=tips,kind='reg')
