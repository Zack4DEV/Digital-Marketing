FROM python:3.11-slim

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN /opt/venv/bin/pip3 install --no-cache-dir -r "requirements.txt"

COPY . ./app

WORKDIR /app/

EXPOSE 8501

ENV STREAMLIT_PORT=8501
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
