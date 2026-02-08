from fastapi import FastAPI
from src.adapters.api.magic_link_routes import router as magic_link_router

app = FastAPI(title="AI Agent Project", version="0.1.0")

app.include_router(magic_link_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
