# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.192.0/containers/python-3/.devcontainer/base.Dockerfile


ARG VARIANT="3.10"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends bash-completion \
    default-libmysqlclient-dev default-mysql-client default-mysql-server \
    vim

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
#COPY requirements.txt /tmp/pip-tmp/
#RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#   && rm -rf /tmp/pip-tmp

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/home/vscode/.poetry python3 -
ENV PATH="/home/vscode/.poetry/bin:${PATH}"
