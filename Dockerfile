FROM python:3.11-slim
RUN pip install pdm
WORKDIR /app
COPY pdm.lock .
RUN pdm install --prod
COPY src .
CMD pdm start
