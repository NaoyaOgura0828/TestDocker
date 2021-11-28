# BaseImage Python3
FROM python:3

# WorkingDirectory 作成・設定・移動
RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO
WORKDIR  /WORK_REPO

# main.py 作成・実行
ADD main.py .
CMD ["python", "-u", "main.py"]