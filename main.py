from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chromegpt.main import run_chromegpt
import time
import uvicorn

# Define the request model
class ChromeGPTRequest(BaseModel):
    task: str  # Only the task/text will be provided by the user

# Create FastAPI app
app = FastAPI()

# Define an endpoint to trigger the ChromeGPT task with default parameters
@app.post("/run_chromegpt")
def run_chromegpt_endpoint(request: ChromeGPTRequest):
    try:
        # Run the ChromeGPT with default parameters and user-provided text
        print("Masuk")
        time.sleep(30)
        result = run_chromegpt(
            task=request.task,
            model="gpt-4",           # Default model
            agent="auto-gpt",        # Default agent
            headless=False,          # Default headless mode
            verbose=True,            # Verbose mode enabled
            continuous=True,         # Continuous mode enabled
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8084, reload=True, workers=5)
