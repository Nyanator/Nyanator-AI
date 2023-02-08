from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_id: str
    content: str

@app.post('/')
async def talk(message: Message):
    return {"res": "ok", "ID": message.user_id, "名前": message.content}