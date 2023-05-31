FROM python:3.10
WORKDIR /usr/src/app

COPY . .
RUN pip install flask python-dotenv translate requests requests-html Unidecode

EXPOSE 5000

CMD ["python3", "index.py"]