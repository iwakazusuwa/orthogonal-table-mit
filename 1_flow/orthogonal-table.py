import os
import sys
import subprocess
import pandas as pd

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

# =========================
# 各列ごとにユニーク値（非NA）を水準として抽出
# =========================
factor_levels = {col: levels_df[col].dropna().unique().tolist() for col in levels_df.columns}
for col, lv in factor_levels.items():
    print(f"{col}: {lv}")

# =========================
# 因子数に応じて直交表インデックスを選択
# =========================
num_factors = len(factor_levels)

if num_factors == 3:
    orthogonal_index = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 2, 2],
        [1, 0, 1],
        [1, 1, 2],
        [1, 2, 0],
        [2, 0, 2],
        [2, 1, 0],
        [2, 2, 1],
    ]
elif num_factors == 4:
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
else:
    raise ValueError(f"L9直交表は3因子または4因子のみ対応しています。入力因子数: {num_factors}")

# =========================
# L9のインデックスを水準値に変換して直交表作成
# =========================
selected_factors = list(factor_levels.keys())
selected_levels = [factor_levels[f] for f in selected_factors]

data_OA = []
for row in orthogonal_index:
    entry = [selected_levels[i][row[i]] for i in range(num_factors)]
    data_OA.append(entry)

df_OA = pd.DataFrame(data_OA, columns=selected_factors)

# =========================
# コンジョイント分析用に行列入れ替え
# =========================
df_OA = df_OA.T

# =========================
# 保存
# =========================
df_OA.to_csv(save_name, index=True, encoding="utf-8-sig")

# =========================
# 出力フォルダを開く
# =========================
if sys.platform.startswith('win'):
    os.startfile(output_path)
elif sys.platform.startswith('darwin'):
    subprocess.run(['open', output_path])
else:
    subprocess.run(['xdg-open', output_path])

print("完了")
