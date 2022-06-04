from fastapi import FastAPI
import chatterbot


app = FastAPI()
chatbot = chatterbot.ChatBot("name", read_only=True)


@app.get("/")
async def root():
    return {"message": "talk to me :("}


@app.get("/{mainInput}")
async def say_hello(mainInput: str):
    response = chatbot.get_response(mainInput)
    print(f"returned '{response}' in response to '{mainInput}'")
    return {"message": f"{response}"}
