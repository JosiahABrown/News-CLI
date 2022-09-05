FROM rapidfort/python-chromedriver 

USER root
RUN mkdir -p /home/app

COPY . /home/app

CMD ["python", "main.py"]
