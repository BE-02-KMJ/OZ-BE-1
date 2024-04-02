from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
from predict import predict

app = FastAPI()


@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(BytesIO(await file.read()))
    result = predict(image)
    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
