FROM ubuntu:22.04
USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install curl -y
RUN apt-get install unzip -y
RUN apt-get install net-tools -y
RUN apt-get autoclean -y
RUN apt-get autoremove -y
RUN apt-get install git -y
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install ntp -y
RUN apt-get install vim -y
RUN useradd -rm -d /home/uxeng -s /bin/bash -g root -G sudo -u 1001 uxeng
USER uxeng
COPY --chown=uxeng:root run_conda_installer.sh /home/uxeng/
RUN mkdir -p /home/uxeng/apps/uxeng
RUN mkdir -p /home/uxeng/dev
COPY --chown=uxeng:root environment.yml /home/uxeng/apps/uxeng/
COPY --chown=uxeng:root noxfile.py /home/uxeng/dev/
COPY --chown=uxeng:root pyproject.toml /home/uxeng/dev/
COPY --chown=uxeng:root LICENSE.txt /home/uxeng/dev/
COPY --chown=uxeng:root README.md /home/uxeng/dev/
COPY --chown=uxeng:root MANIFEST.in /home/uxeng/dev/
COPY --chown=uxeng:root .coveragerc /home/uxeng/dev/
COPY --chown=uxeng:root ./src /home/uxeng/dev/src/
COPY --chown=uxeng:root ./tests /home/uxeng/dev/tests/
COPY --chown=uxeng:root build_test_lint.sh /home/uxeng/dev/
RUN chmod +x /home/uxeng/run_conda_installer.sh
RUN chmod +x /home/uxeng/dev/build_test_lint.sh
WORKDIR /home/uxeng
ENTRYPOINT ["/home/uxeng/run_conda_installer.sh"]


# FROM python:3.12
# RUN apt-get update && apt-get upgrade -y
# RUN apt-get autoclean -y
# RUN apt-get autoremove -y
# RUN useradd -rm -d /home/gridx -s /bin/bash -g root -G sudo -u 1001 gridx
# COPY requirements.txt /home/gridx/
# WORKDIR /home/gridx
# RUN pip install -r ./requirements.txt
# ENTRYPOINT ["python3"]
# CMD ["-m", "http.server","3000"]
