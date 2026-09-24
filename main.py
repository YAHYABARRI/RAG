import logging

from fastapi import FastAPI
import inngest
import inngest.fast_api

from dotenv import load_dotenv

load_dotenv()


# Client Inngest
inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
)


# Fonction Inngest
@inngest_client.create_function(
    fn_id="rag-ingest-pdf",
    trigger=inngest.TriggerEvent(
        event="rag/ingest_pdf",
    ),
)
async def rag_ingest_pdf(ctx: inngest.Context):
    return {"message": "PDF ingestion started"}


# Application FastAPI
app = FastAPI()


# Expose les fonctions Inngest
inngest.fast_api.serve(
    app,
    inngest_client,
    [rag_ingest_pdf],
)