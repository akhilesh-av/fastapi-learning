from  fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class AnalyzePRRequest(BaseModel):
    repo_url : str
    pr_number : int
    github_token : Optional['str'] = None


@app.post("/start_task", status_code=status.HTTP_200_OK)
async def start_task_endpoint(task_request: AnalyzePRRequest):
    data = {
        "repo_url": task_request.repo_url,
        "pr_number": task_request.pr_number,
        "github_token": task_request.github_token
    }
    print(f"Received data: {data}")
    return {"task_id": "123", "status": "Task started"}