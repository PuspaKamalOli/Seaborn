import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
tips.head()
# 1.PairGrid(plot only non-categorical)
# plot all the columns v with each other  in scatter
t = sns.PairGrid(tips)
t.map(plt.scatter, color='#2E4053', s=8)

# plots diff according to diagonal
iris = sns.load_dataset('iris')
i = sns.PairGrid(iris)
# dist plot for diagonal
i.map_diag(sns.distplot, kde=False, color='red')
# scatter plot to above diagonal
i.map_upper(plt.scatter, color='black')
# kde to lower of diagonal
i.map_lower(sns.kdeplot)

# 2.FacetPlot(for categorical plot)
tt = sns.FacetGrid(data=tips, col='sex', row='day', hue='smoker')
tt.map(plt.scatter, 'total_bill', 'tip')
