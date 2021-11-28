# TestDocker

`TestDocker`は`Docker`による出力テストを実行したい場合に使用する。


# Requirement
# TODO:ここから変更
以下のVersionで検証済みである。
- Python 3.9.7

<br>

`{ソースファイル名}.py`の実行に必要なライブラリなどを列挙する
- 作成時点では必要ライブラリなし

<br>


# Installation

Requirementで列挙したライブラリのインストール方法

```bash
$ pip install -r requirements.txt
```

<br>


# Usage

- test_python.py (Bash実行用)
```bash
$ python test_python.py
```

<br>

- test_python_for_aws_lambda.py (AWS Lambda用)

```
# AWS Lambda へアクセス
# コードソースにtest_python_for_aws_lambda.py内ソースコードをコピペする
# Deployを実行する
```

<br>


# Note

-` buildspec.yml`は`Code Build`で`AWS ECR`へPUSHする為の設定ファイルである。

<br>


# Author
- 作成者 : NaoyaOgura