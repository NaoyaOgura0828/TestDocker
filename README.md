# TestDocker

`TestDocker`は`Docker`による出力テストを実行したい場合に使用する。


# Requirement

以下のVersionで検証済みである。
- AmazonLinux2 (AWS EC2)
- Ubuntu20.04 (WSL2)

<br>


# Installation

- `AWS CodeBuild`を使用する場合は、`buildspec.yml`へ`Docker Hub` の`USER_ID`, `USER_PASS`をそれぞれ入力する。
    <br>
    **但しMFAを有効化している場合は`Docker Hub`で`AccessToken`を発行し`DOCKERHUB_PASS`へ入力する。**
    <br>
    参考URL:
    <br>
    https://dev.classmethod.jp/articles/codebuild-has-to-use-dockerhub-login-to-avoid-ip-gacha/

```yml
phases:
  pre_build:
    commands:
      # ECR へのログイン
      - echo Logging in to Amazon ECR...
      - aws ecr get-login --region ${AWS_DEFAULT_REGION}
      - aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
      # Docker Hub へのログイン
      - echo Logging in to Docker Hub...
      - echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin # DOCKERHUB_PASS, DOCKERHUB_USER をそれぞれ入力する
```

<br>


# Usage

以下のコマンドは`Test{テスト対象リソース}`ディレクトリ内で実行する。

```bash
# イメージ構築
$ docker build -t ${イメージ名} .

# イメージ確認
$ docker images

# イメージ削除
$ docker rmi ${IMAGE_ID}


# コンテナ起動
$ docker run ${イメージ名}

# すべてのコンテナ情報出力
$ docker ps -a

# コンテナを停止
$ docker stop ${イメージ名}

# 停止したコンテナを起動
$ docker start ${イメージ名}

# コンテナ削除
$ docker rm ${CONTAINER_ID}
```

<br>


# Note

- `buildspec.yml`は`Code Build`で`AWS ECR`へPUSHする為の設定ファイルである。

<br>


# Author
- 作成者 : NaoyaOgura