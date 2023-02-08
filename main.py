import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    user_id: str
    content: str


@app.post('/talk/')
async def talk(message: Message):
    return {"res": "okokok", "ID": message.user_id, "name": message.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)