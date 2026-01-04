from fastapi import FastAPI
from app.api.v1.routes.repayment_routes import router
from app.core.logging import init_logging

init_logging()

app = FastAPI(title="RootLender Repayment Service")

app.include_router(router, prefix="/api/v1/repayments", tags=["Repayments"])

@app.get("/health")
def health():
    return {"status": "ok"}
