RUN pip3 install -r requirements.txt

EXPOSE 4800

ENTRYPOINT  ["python"]

CMD ["app.py"]
