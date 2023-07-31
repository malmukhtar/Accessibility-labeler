from fastapi import Depends, FastAPI
from .classifier.model import Model, get_model

app = FastAPI()


@app.post("/predict")
async def predict(issue: str, model: Model = Depends(get_model)):
    accessibility_confidence, nonaccessibility_confidence = model.predict(issue)
    return {"Accessibility": str(accessibility_confidence),
            "Non-accessibility": str(nonaccessibility_confidence)}
