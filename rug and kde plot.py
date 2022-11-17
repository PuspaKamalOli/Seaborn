import seaborn as sns
tips = sns.load_dataset('tips')
# rugplot
sns.rugplot(tips['total_bill'])
# kernel density estimation plot
sns.kdeplot(tips['total_bill'])
