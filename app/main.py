from fastapi import FastAPI,status

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/health")
async def root():
    return {"status":"ok"}

