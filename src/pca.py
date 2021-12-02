"""
主成分分析を行う
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def pc_analyze(data: pd.DataFrame, title: str):
    """
    主成分分析を行う

    Paramters
    ---------

    data : pandas.DataFrame
        主成分分析を行うデータ
    name : str
        画像に保存に使う名前
    """
    # 標準化
    data_std = data.iloc[:, :].apply(lambda x: (x-x.mean())/x.std(), axis=0)
    # 主成分分析を行う
    pca = PCA()
    pca.fit(data_std)
    feat = pca.transform(data_std)

    # 固有値、寄与率、累積寄与率をまとめる
    state = pd.DataFrame([pca.explained_variance_, pca.explained_variance_ratio_, list(np.cumsum(
        pca.explained_variance_ratio_))],
        columns=[f"PC{i+1}" for i in range(len(data_std.columns))],
        index=['eigenvalue', 'contribution', 'contributioin_sum']).T
    print(f"states:\n{state}")

    # 第一主成分、第二主成分でプロットする
    fig = plt.figure(figsize=(6, 6))
    plt.scatter(feat[:, 0], feat[:, 1], alpha=0.8, c=list(data.iloc[:, 0]))
    plt.grid()
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(f"{title}_distribute")
    plt.show()
    fig.savefig(f"output/{title}_distribute.png")

    # 固有ベクトルの第一主成分、第二主成分の寄与度を見る
    fig = plt.figure(figsize=(6, 6))
    for x_axis, y_axis, name in zip(pca.components_[0], pca.components_[1], data.columns[1:]):
        plt.text(x_axis, y_axis, name)
    plt.scatter(pca.components_[0], pca.components_[1], alpha=0.8)
    plt.grid()
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(f"{title}_heatvector")
    plt.show()
    fig.savefig(f"output/{title}_heatvector.png")
