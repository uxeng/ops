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
RUN mkdir -p /home/uxeng/dev
COPY environment.yml /home/uxeng/apps/uxeng/
COPY noxfile.py /home/uxeng/dev/
COPY pyproject.toml /home/uxeng/dev/
COPY LICENSE.txt /home/uxeng/dev/
COPY README.md /home/uxeng/dev/
COPY MANIFEST.in /home/uxeng/dev/
COPY ./src /home/uxeng/dev/src/dev
COPY ./tests /home/uxeng/dev/tests/
RUN chmod +x /home/uxeng/run_conda_installer.sh
WORKDIR /home/uxeng
ENTRYPOINT ["/home/uxeng/run_conda_installer.sh"]