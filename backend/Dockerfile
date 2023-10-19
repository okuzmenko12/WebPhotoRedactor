FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /apps/backend
COPY . .

RUN pip install "poetry"

RUN apt-get update && apt-get install -y python3-opencv

COPY poetry.lock /portfolio/backend
COPY start.sh /apps/backend/start.sh

RUN poetry config virtualenvs.create true && poetry install --no-interaction --no-ansi
RUN chmod +x /apps/backend/start.sh

CMD ["/apps/backend/start.sh"]