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

## 1

### task 1-1

##### 実行結果

##### 実行結果

<!-- [[[cog
import cog
file="output/task1-2.txt"
cog.outl("\n```bash")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]] -->

<!-- [[[end]]] -->