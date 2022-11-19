FROM ubuntu
WORKDIR /app
COPY .  .
RUN pip3 install Flask
ENTRYPOINT [ "python" ]
CMD [" app.py" ,"-m","flask","run","--host=0.0.0.0"]