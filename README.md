# SA-lab1

統計分析法 第2回演習

## 使用方法

- `pip instlla pipenv`でpipenv をインストールする
- `pipenv update`でパッケージをインストールする
- `pipenv run (コマンド)`でコマンドを実行する

## ファイル・フォルダーについての説明

- output
  
  標本データや出力ファイルなどがあるフォルダーです。
- src
  
  各演習を実行するためのメソッドを定義したフォルダーです。
- Pipfile
  
  インポートするモジュールが書かれたファイルです。

- issuer.py
  
  outputに標準出力を保存するときに使うファイルでる。
  `python3 issuer.py python3 (ファイル名)`で実行できます。
- ?_analize.py
  
  各演習のプログラムです。
  `pipenv run python3 (ファイル名)`で実行できます。
