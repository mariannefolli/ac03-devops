FROM python:3.7-slim
RUN pip install flask
COPY primos.py primos.py
CMD ["python","primos.py"]