import pandas as pd # Pandas
from sklearn.datasets import fetch_california_housing

# Populationの値によって3種類のカテゴリに区分する関数
def category(df):
  if df < 600: return 'few' # 600以下はfew
  elif df > 3000: return 'many' # 3000以上はmany
  else: return 'usually' # 中間の値はusually

housing = fetch_california_housing() # データセットを取得
# dataキーで8項目のデータを抽出
# feature_namesキーで項目名を抽出してデータフレームに格納
df_housing = pd.DataFrame(
  housing.data, columns=housing.feature_names
)
#　Populationの統計量を出力
p_describe = df_housing['Population'].describe()
# print(p_describe)

# Populationのデータをカテゴリ化
p_category = df_housing['Population'].apply(category)
# print(df_housing['Population'].apply(category))

# Pandasのget_dummies関数でカテゴリデータに対応したダミー変数を作成
p_dummy = pd.get_dummies(p_category, drop_first=True, dtype=int)
# print(p_dummy)

# 作成したダミー変数を元のデータに追加し、Populationの列を削除
X = pd.concat([df_housing,p_dummy], axis=1)
X = X.drop(['Population'], axis=1)
print(X)
