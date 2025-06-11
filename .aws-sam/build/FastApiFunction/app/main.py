from fastapi import FastAPI
from mangum import Mangum
from app.routers.flights import router as flight_router
from app.routers.analyze import router as analyze_router 
from app.routers.logs import router as logs_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://flight-schedule-frontend-hlc9.vercel.app",
                   "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flight_router, prefix="/api")
app.include_router(analyze_router, prefix="/api")
app.include_router(logs_router, prefix="/api")


handler = Mangum(app, lifespan="off")