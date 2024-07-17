from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from segmentation import segment_image
import shutil
import os
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/segment")
async def segment(challenge: str = Form(...), file: UploadFile = File(...)):
    if challenge not in ["cv1", "cv2", "cv3", "nlp1", "nlp2", "nlp3", "other"]:
        return JSONResponse(status_code=400, content={"message": "Invalid challenge type"})

    try:
        # Ensure the temp and output directories exist
        os.makedirs("./temp", exist_ok=True)
        os.makedirs("./output", exist_ok=True)

        file_location = f"./temp/{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)

        segmented_image_path = segment_image(file_location)
        if segmented_image_path:
            return {"message": "succeed", "segmented_image_path": segmented_image_path}
        else:
            return {"message": "segmentation failed"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)