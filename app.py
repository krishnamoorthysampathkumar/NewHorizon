import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from similarity import most_similar_row

app = FastAPI()

class Item(BaseModel):
    incident_title: str
    
    
@app.post("/get_runbooks")
async def reminder(request: Item):
    incident_title = request.incident_title
    runbook_title, runbook_link = most_similar_row(incident_title)
    response = {
        "runbook_title": runbook_title,
        "runbook_link": runbook_link
    }
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)