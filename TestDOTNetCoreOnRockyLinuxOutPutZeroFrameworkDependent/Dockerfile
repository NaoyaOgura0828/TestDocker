# RockyLinux 8.5 Install
FROM rockylinux/rockylinux:8.5

# runtime Install
RUN dnf install aspnetcore-runtime-6.0 -y

# WORK_DIR 作成・移動・設定
RUN mkdir WORK_DIR && \
    cd WORK_DIR
WORKDIR /WORK_DIR

# ConsoleApp0 ディレクトリ内全コピー
COPY ConsoleApp0/ /WORK_DIR

# ConsoleApp0 実行
RUN chmod -R +x .
CMD ["bash", "-c", "./ConsoleApp0"]