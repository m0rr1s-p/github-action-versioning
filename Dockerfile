FROM python:3.13.5-alpine3.22

COPY requirements.txt /action/requirements.txt
RUN pip install --upgrade --force --no-cache-dir pip && \
    pip install --upgrade --force --no-cache-dir -r /action/requirements.txt

COPY versioning.py /action/versioning.py

ENTRYPOINT ["python", "/action/versioning.py"]