# Ubuntu20.04 Install
FROM ubuntu:20.04

# GNU Wget Install
RUN apt-get update && \
    apt-get install wget -y && \
    rm -rf /var/lib/apt/lists/*

#  Linux Software Repository for Microsoft Products Install
RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb

# ASP.NET Core Runtime Install
RUN apt-get update && \
    apt-get install apt-transport-https -y && \
    apt-get update && \
    apt-get install aspnetcore-runtime-6.0 -y

# WORK_DIR 作成・移動・設定
RUN mkdir WORK_DIR && \
    cd WORK_DIR
WORKDIR /WORK_DIR

# ConsoleApp0 ディレクトリ内全コピー
COPY ConsoleApp0/ /WORK_DIR

# ConsoleApp0 実行
RUN chmod -R +x .
CMD ["bash", "-c", "./ConsoleApp0"]