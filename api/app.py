from fastapi import FastAPI

from router.credit_cards import router as credit_cards_router

#from router.credit_cards import router as credit_cards_router
from api.subscriptions import router as subscriptions_router
from api.financial_reports import router as financial_reports_router
from api.integrations import router as integrations_router

#from api import credit_cards, subscriptions, financial_reports, integrations

app = FastAPI()

# Aggiungi i router degli endpoint specifici
app.include_router(credit_cards.router)
app.include_router(subscriptions.router)
app.include_router(financial_reports.router)
app.include_router(integrations.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app', host="0.0.0.0", port=8000)

