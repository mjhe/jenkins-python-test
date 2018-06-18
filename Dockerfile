from python

COPY . .

RUN pip3 install hvac boto3
CMD python3 testing.py
