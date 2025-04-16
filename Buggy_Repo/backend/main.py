from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(items_router, prefix="/items")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(quiz_router, prefix="/quiz")

@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}