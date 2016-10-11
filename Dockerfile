FROM python:3-alpine
MAINTAINER Ioannis Skoulis "ioannis.skoulis@sesam.io"
EXPOSE 5000/tcp
COPY ./service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./service /service
WORKDIR /service
ENTRYPOINT ["python"]
CMD ["datasink-service.py"]
