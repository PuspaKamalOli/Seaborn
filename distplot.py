# A distribution plot displays a distribution and range of a set of numeric values plotted against a dimension.
# You can display this chart in three different ways, you can just have the value points displayed showing the
# distribution, or you can display the bounding box which shows the range or use a combination of both.
import seaborn as sns
tips = sns.load_dataset('tips')
# tips is a dataset available already in sea born library
tips.head()
sns.distplot(tips['total_b ill'], bins=5, kde=False)
