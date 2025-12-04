FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install curl -y
RUN apt-get install unzip -y
RUN apt-get install net-tools -y
RUN apt-get autoclean -y
RUN apt-get autoremove -y
RUN useradd -rm -d /home/uxeng -s /bin/bash -g root -G sudo -u 1001 uxeng
COPY run_conda_installer.sh /home/uxeng/
RUN mkdir -p /home/uxeng/apps/uxeng
COPY environment.yml /home/uxeng/apps/uxeng/
COPY nox.py /home/uxeng/
COPY pyproject.toml /home/uxeng/
COPY ./src /home/uxeng/
COPY ./tests /home/uxeng/
RUN chmod +x /home/uxeng/run_conda_installer.sh
WORKDIR /home/uxeng
ENTRYPOINT ["/home/uxeng/run_conda_installer.sh"]
