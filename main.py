from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_id: str
    content: str

@app.post('/')
async def talk(message: Message):
    return {"res":"okok","ID":message.user_id,"name":message.content}