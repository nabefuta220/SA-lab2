"""
seiseki.txtを主成分分析する
"""
import pandas as pd

from src.pca import pc_analyze
from src.read_data import read_file

if __name__ == "__main__":
    # ファイルの読み込み
    res = read_file('output/seiseki.txt', 'shift-jis')
    data = pd.DataFrame(res[1:], columns=res[0])
    # 欠損値が含まれる行を削除
    data = data.dropna(axis=0).astype('float64')
    print(f"data:\n{data.head()}")
    # 主成分分析を行う
    pc_analyze(data, 'score')
