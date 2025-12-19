FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
# FROM harbor.fa-services.intra.dlr.de/ghcr/astral-sh/uv:python3.12-bookworm-slim

# folder for virtual environment
ENV UV_PROJECT_ENVIRONMENT /python
ENV PATH "${UV_PROJECT_ENVIRONMENT}/bin:$PATH"
ENV PYTHONUNBUFFERED 1
ENV PROJECT_DIR /src
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS False

WORKDIR ${PROJECT_DIR}

# install requirements
# docker run -it --rm -v "$(pwd):/tmp" -w /tmp ghcr.io/astral-sh/uv:python3.12-bookworm-slim bash
COPY uv.lock pyproject.toml ./
RUN uv sync --locked --no-managed-python

# copy source code including common (shared code)
COPY apps ${PROJECT_DIR}/apps/
