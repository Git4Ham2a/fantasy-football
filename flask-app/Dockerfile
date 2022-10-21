FROM python:3.8
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
RUN python3
ENTRYPOINT ["python3", "app.py"]
