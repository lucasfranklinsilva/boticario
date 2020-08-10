FROM python:3.7

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY __init__.py /app
CMD python __init__.py
