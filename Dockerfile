FROM mcr.microsoft.com/devcontainers/miniconda:0-3

RUN conda install -n base -c conda-forge mamba

COPY environment.yml* /tmp/conda-tmp/
COPY requirements.txt* /tmp/conda-tmp/

# Use root to change permissions
USER root

# Give full permissions to the user
RUN chown -R vscode:vscode /tmp/conda-tmp/
# RUN chmod -R 777 /tmp/conda-tmp/

# Switch to the normal user
USER vscode

RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then /opt/conda/bin/mamba env update -n base -f /tmp/conda-tmp/environment.yml; fi

RUN conda init bash

# RUN echo "conda activate base" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
