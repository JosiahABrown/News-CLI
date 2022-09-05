FROM selenium/standalone-chrome

USER root
RUN mkdir -p /home/app

COPY . /home/app

CMD ["python", "main.py"]
