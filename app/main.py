import pandas as pd # Pandas
from sklearn.datasets import fetch_california_housing

# Populationの値によって3種類のカテゴリに区分する関数
def category(df):
  if df < 600: return 'few'
  elif df > 3000: return 'many'
  else: return 'usually'

housing = fetch_california_housing() # データセットを取得
# dataキーで8項目のデータを抽出
# feature_namesキーで項目名を抽出してデータフレームに格納
df_housing = pd.DataFrame(
  housing.data, columns=housing.feature_names
)
#　Populationの統計量を出力
p_describe = df_housing['Population'].describe()
# print(p_describe)

p_category = df_housing['Population'].apply(category)
# print(df_housing['Population'].apply(category))

p_dummy = pd.get_dummies(p_category, drop_first=True, dtype=int)
# print(p_dummy)

X = pd.concat([df_housing,p_dummy], axis=1) # many、usuallyを追加
X = X.drop(['Population'], axis=1) # Populationの列を削除
X.head() # 冒頭5件を出力
# print(X)
