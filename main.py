import openai
import urllib.parse
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

openai.api_key = ""

class Message(BaseModel):
    user_id: str
    content: str


@app.post('/talk/')
async def talk(message: Message):
    prompt_text = "\n";
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_text+urllib.parse.unquote(message.content),
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    return {"res": "okokok", "ID": message.user_id, "reply": response.choices[0].text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)