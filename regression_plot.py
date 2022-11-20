import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
sns.set_style('whitegrid')
sns.set_context('poster', font_scale=0.7)
# non categorical non grid
sns.lmplot(data=iris, y='sepal_length', x='sepal_width', hue='species')

# with grid and categorical
sns.set_style('darkgrid')
sns.set_context('poster', font_scale=0.7)
tips = sns.load_dataset('tips')
sns.lmplot(data=tips, x='total_bill', y='tip', col='day', row='smoker'
           , hue='sex', aspect=0.6)
