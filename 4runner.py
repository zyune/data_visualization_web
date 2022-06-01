import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
fourrunner = pd.read_csv(
    'scrapy_ spider/tutorial/tutorial/spiders/Fourrunner.csv')
fourrunner_trim = fourrunner.groupby(by='name').median()
sns.scatterplot(data=fourrunner_trim, x='millage', y='price', hue='name')
plt.legend(bbox_to_anchor=(1.02, 1), loc='best')
plt.savefig('img/median_price_trim')
plt.close()

sns.scatterplot(data=fourrunner, x='millage', y='price', hue='name')
plt.legend(bbox_to_anchor=(1.02, 1), loc='best')
plt.savefig('img/4runner_2018')
plt.close()
