FROM jupyter/base-notebook@sha256:414d9ab1ab928d55c7c841440518315e701775c2670a156e78f97113b1cf9c6a

# Install from requirements.txt file
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --quiet --no-cache-dir --requirement /tmp/requirements.txt && \
    jupyter labextension uninstall jupyterlab-plotly && \
    jupyter labextension install jupyterlab-plotly@5.11.0 @jupyter-widgets/jupyterlab-manager && \
    jupyter lab build && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

