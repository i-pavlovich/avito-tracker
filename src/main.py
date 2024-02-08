import uvicorn
from fastapi import FastAPI

from tracker.router import router as tracker_router


app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(tracker_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
