from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from model import VoiceModel, create_features


router = APIRouter(prefix='/gender')
model = VoiceModel()

class Response(BaseModel):
    class_value: int
    class_name: str

@router.post("/", response_model=Response)
async def gender(file: UploadFile = File(...)):
    features = create_features(file.filename)
    class_value = model.predict(features)
    class_name = model.get_target_name(class_value)
    return {"class_value": class_value, "class_name": class_name}