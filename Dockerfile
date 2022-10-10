FROM python

USER root
RUN mkdir -p /home/app && \
	pip install -U selenium

COPY . /home/app

CMD ["python", "/home/app/main.py"]
