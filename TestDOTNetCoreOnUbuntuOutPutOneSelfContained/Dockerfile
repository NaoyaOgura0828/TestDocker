# Ubuntu20.04 Install
FROM ubuntu:20.04

# WORK_DIR 作成・移動・設定
RUN mkdir WORK_DIR && \
    cd WORK_DIR
WORKDIR /WORK_DIR

# ConsoleApp1 ディレクトリ内全コピー
COPY ConsoleApp1/ /WORK_DIR

# ConsoleApp1 実行
RUN chmod -R +x .
CMD ["bash", "-c", "./ConsoleApp1"]