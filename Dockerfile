FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies from the service directory
COPY rootlender-repayment-service/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual service code
COPY rootlender-repayment-service rootlender-repayment-service

# Run the service
CMD ["python", "-m", "rootlender_repayment_service.main"]
