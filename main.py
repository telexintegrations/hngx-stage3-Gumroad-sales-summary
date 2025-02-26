from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.tick import router as tickRouter

app = FastAPI()
app.include_router(tickRouter)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
