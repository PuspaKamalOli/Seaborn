
import numpy as np
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()
# 1.bar plot
# hue is for another categorical column and estimator can be mean std or any statistical term
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.mean, hue='smoker')

# 2.count plot count num for categorical column and takes single column as argument
sns.countplot(x='smoker', data=tips)

# 3.box plot gives information about mean ,quartiles and max and min value
sns.boxplot(x='sex', y='total_bill', data=tips)

# 4.violin plot gives more information than box plot,split argument join another category with itself
sns.violinplot(x='sex', y='total_bill', data=tips, hue='smoker', split=True)

# 5.strip pLlot is scatter plot but for categorical data,jitter argument makes plots more clear
sns.stripplot(x='sex', y='total_bill', data=tips, hue='smoker', jitter=True)

# swarm plot is the combination of violin and strip plot
sns.swarmplot(x='sex', y='total_bill', data=tips, hue='smoker')
