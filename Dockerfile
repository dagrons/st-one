FROM python:3.8

WORKDIR /app

COPY ./st-one /app

RUN pip install -U pip  && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "streamlit", "run", "main.py"]



