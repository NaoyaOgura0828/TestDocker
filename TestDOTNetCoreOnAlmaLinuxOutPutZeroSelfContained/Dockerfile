# AlmaLinux 8.5 Install
FROM almalinux:8.5

# WORK_DIR 作成・移動・設定
RUN mkdir WORK_DIR && \
    cd WORK_DIR
WORKDIR /WORK_DIR

# ConsoleApp0 ディレクトリ内全コピー
COPY ConsoleApp0/ /WORK_DIR

# ConsoleApp0 実行
RUN chmod -R +x .
CMD ["bash", "-c", "./ConsoleApp0"]