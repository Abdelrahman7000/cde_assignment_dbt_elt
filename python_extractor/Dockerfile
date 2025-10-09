# Use a minimal Python image
FROM python:3.12

WORKDIR /app

# Install dependencies (e.g., pandas and psycopg2-binary for Postgres)
RUN pip install pandas sqlalchemy requests psycopg2-binary

COPY extract_load.py .

# Command to run the script
CMD ["python", "extract_load.py"]