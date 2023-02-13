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
    prompt_text = "以下は猫耳女の子Nyanatorとの会話です。\n"
    response = openai.Completion.create(
        model=os.environ['modelname'],
        prompt=prompt_text+urllib.parse.unquote(message.content)+" ->",
        temperature=0.27,
        max_tokens=256,
        stop=['end', 'END']
    )

    return {"res": "ok", "ID": message.user_id, "reply": response.choices[0].text.lstrip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
