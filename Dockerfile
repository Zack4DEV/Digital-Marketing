FROM python:3.11-slim

COPY requirements.txt /app

COPY streamlit_app.py components screens utils /app

COPY pyproject.toml /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENV STREAMLIT_PORT=8501
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
