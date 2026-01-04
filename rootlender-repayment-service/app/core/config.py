import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_NAME = "rootlender-repayment-service"

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
