from fastapi import FastAPI
import openai
import os
from pydantic import BaseModel
import urllib.parse
import uvicorn

app = FastAPI()

openai.api_key = os.environ['apikey']


class Message(BaseModel):
    user_id: str
    content: str


@app.post('/talk/')
async def talk(message: Message):
    prompt_text = "以下AIの女の子Nyanatorとの会話。\n"
    response = openai.Completion.create(
        model=os.environ['modelname'],
        prompt=prompt_text+urllib.parse.unquote(message.content),
        temperature=0.2,
        max_tokens=50,
        frequency_penalty=2.0,
        presence_penalty=2.0,
        stop='.'
    )

    return {"res": "ok", "ID": message.user_id, "reply": response.choices[0].text.lstrip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
