# syntax=docker/dockerfile:3

FROM python:3.11 

# Or any preferred Python version.

# Add all required files
ADD Source/* .

# Setup environment
RUN pip install -r requirements.txt

CMD [“python”, “./main.py”] 
# Or enter the name of your unique directory and parameter set.

