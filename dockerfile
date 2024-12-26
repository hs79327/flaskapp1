FROM python
RUN pip install flask
RUN mkdir /app1
COPY hello.py /app1/
EXPOSE 7000
CMD [ "python","/app1/hello.py" ]
