# orthogonal-table-mit

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


直交表（Orthogonal Array）を簡単に作成し、コンジョイント分析や実験計画法で使える形式に変換する Python パッケージです。

---

## 概要

- `levels.csv` から因子ごとの水準リストを取得
- L9直交表に基づき、各組み合わせを水準値に変換
- 直交表の順番を安定させて DataFrame 化
- コンジョイント分析用に行列を転置して保存
- Windows / Mac / Linux で出力フォルダを自動で開く

---

# フォルダ構成
```
├─ 1_flow/
│   └─ orthogonal-table.py       # R 実行スクリプト
├─ 2_data/
│   └─ levels.csv                # 水準表　サンプル
├─ 3_output/                     # 決定木出力画像用（自動作成）
```


# 入力データフォーマット例
2_data/sample.csv を参照ください。


# インストール

```bash
pip install orthogonal-table-mit
```


# 使い方
## 1. データ準備

2_data/levels.csv に因子と水準を記載します。

## 2. 実行例
```bash
from orthogonal_table_mit import create_orthogonal_table

create_orthogonal_table(
    input_csv="2_data/levels.csv",
    output_folder="3_output"
)
```
実行すると、3_output/直交表.csv が生成され、行列はコンジョイント分析用に転置されています。

## ステップ解説

### 1. データ読み込み

- UTF-8 で読み込み、文字化けする場合は cp932 に自動切り替え
- OS に依存せず安定して読み込めます

### 2. 因子ごとのユニークな水準リスト作成

- 欠損値を除外してユニーク値を抽出
- `factor_levels` に辞書形式で格納
- 各因子の水準リストとして扱えます

### 3. L9直交表の水準番号

- 0始まりのインデックスで、因子ごとの水準に対応
- 各行は 1 回の実験条件の組み合わせ

### 4. 直交表作成と転置

- L9インデックスを水準値に変換して DataFrame 化
- 転置してコンジョイント分析で扱いやすい形式に

### 5. 直交表を作る順番を決める

- 因子順を安定させることで、水準との対応関係を崩さない

### 6. 水準リストも順番を合わせる

- 選択した因子に対応する水準リストを因子順に揃える
- 実験条件の組み合わせを正確に作成可能

### 7. L9のインデックスを水準値に変換しながら直交表を作成

- 数値インデックスを実際の水準名に置き換え、直交表として完成

### 8. コンジョイント分析用に行列入れ替え

- 作成した直交表を転置し、分析で扱いやすく整形
- CSV に保存して再利用可能



## まとめ
- 「どんな調査をしたいのか」「何を目的に分析するのか」を明確にしてから直交表を作成
- 目的が不明確だと水準表がブレてしまい、調査や分析の意味が薄れる
- 直交表作成前に 目的をクリアにする ことが重要


## 今後の拡張予定

`orthogonal-table-mit` は現在、L9直交表を使った基本的な実験計画表の作成とコンジョイント分析用の転置に対応しています。  
今後は、より使いやすく、幅広い用途に対応できるよう進化予定です。

### 精度・機能の向上
- 自動直交表生成アルゴリズムの追加
- CSVやExcelなど多様な入力形式への対応
- 転置や保存形式の柔軟化

### 分析対象の拡張
- 3因子以上の直交表自動生成
- 実験計画法の他の標準直交表への対応
- 将来的にはコンジョイント分析以外の実験計画への応用も検討

---

## 貢献方法

プロジェクトへの貢献は以下の方法で歓迎します：

- バグ報告や機能追加の提案は [Issues](https://github.com/ユーザー名/orthogonal-table-mit/issues) から
- コード改善や新機能追加は Pull Request を作成
- ドキュメントの改善やサンプル追加も歓迎


## LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)
<img width="254" height="101" alt="image" src="https://github.com/user-attachments/assets/810c9630-5927-4e3f-b064-61c546dedb07" />




