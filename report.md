# 統計分析法　第一回レポート

## 実行環境

python3.9

- pipenv

(これ以降のモジュールは`pipenv update`でダウンロードできます)

- pandas
- matplotlib
- cogapp
- scipy
- scikit-learn

## ファイルのエンコーディングについて

`output/pokemon.txt`,`output/seiseki.txt`については、shift-jisで読み込むことができたが、`output/baseball.txt`については、shift-jisでエンコーディングしても、エラーが出たため、UTF-8でエンコーディングしている。

## 主成分分析の流れについて

主成分分析は`sklearn.decomposition.PCA`を用いて行った。

データについては、比例尺度を取り出した後、標準化して渡している。

また、固有値、寄与率はぞれぞれ、`sklearn.decomposition.PCA.explained_variance`,`sklearn.decomposition.PCA.explained_variance_ratio`を用いて取得し、累積寄与率は、`numpy.cumsum()`を使って、計算した。

## task 1-1

#### 実行結果

#### 実行結果

<!-- [[[cog
import cog
file="output/task1-2.txt"
cog.outl("\n```bash")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]] -->

<!-- [[[end]]] -->