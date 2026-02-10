FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual service package
COPY rootlender-repayment-service rootlender-repayment-service

# Run the service
CMD ["python", "-m", "rootlender-repayment-service.main"]
