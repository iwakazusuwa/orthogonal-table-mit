# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import os
import sys
import pandas as pd
import numpy as np

# =========================
# ディレクトリ・ファイル設定
# =========================
INPUT_FOLDER = '2_data'
OUTPUT_FOLDER = '3_output'

parent_path = os.path.dirname(os.getcwd())
input_path = os.path.join(parent_path, INPUT_FOLDER, 'levels.csv')
output_path = os.path.join(parent_path, OUTPUT_FOLDER)
os.makedirs(output_path, exist_ok=True)

save_name = os.path.join(output_path, "orthogonal_table.csv")


# =========================
# データ読み込み
# =========================
try:
    levels_df = pd.read_csv(input_path, encoding="utf-8")
except UnicodeDecodeError:
    levels_df = pd.read_csv(input_path, encoding="cp932")

# %%
#=============================================
# 各列ごとにユニーク値（非NA）を水準として抽出
#=============================================
factor_levels = {}
for col in levels_df.columns:
    unique_levels = levels_df[col].dropna().unique().tolist()
    factor_levels[col] = unique_levels

#=============================================
# 因子ごとにユニークな水準リストを作る
#=============================================
factor_levels = {}
for col in levels_df.columns:
    factor_levels[col] = levels_df[col].dropna().unique().tolist()
    print(factor_levels[col])

#=============================================
# L9直交表の水準番号（0始まり）
#=============================================
orthogonal_index = [
    [0, 0, 0, 0], 
    [0, 1, 1, 1], 
    [0, 2, 2, 2], 
    [1, 0, 1, 2], 
    [1, 1, 2, 0], 
    [1, 2, 0, 1], 
    [2, 0, 2, 1], 
    [2, 1, 0, 2], 
    [2, 2, 1, 0],
]
##=============================================
# 直交表を作る順番を決める
#=============================================
# 必ず factor_levels の全列を使う
selected_factors = list(factor_levels.keys()) 

#=============================================
# 水準リストも順番を合わせる
#=============================================
selected_levels = [factor_levels[f] for f in selected_factors]
#=============================================
# L9のインデックスを水準値に変換しながら直交表を作成
#=============================================
data_OA = []
for row in orthogonal_index:
    entry = [selected_levels[i][row[i]] for i in range(len(selected_factors))]
    data_OA.append(entry)

# DataFrame化（列名も元の因子名のまま）
df_OA = pd.DataFrame(data_OA, columns=selected_factors)

#=============================================
# コンジョイント分析用に行列入れ替えます
#=============================================
df_OA = df_OA.T
#=============================================
#保存
#=============================================
df_OA.to_csv(save_name, index=True, encoding="utf-8-sig")


# %%
# =============================================
# 出力フォルダを開く
# =============================================
if sys.platform.startswith('win'):
    os.startfile(output_path)
elif sys.platform.startswith('darwin'):
    subprocess.run(['open', output_path])
else:
    subprocess.run(['xdg-open', output_path])

print("完了")

# %%

# %%
