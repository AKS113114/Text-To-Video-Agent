# # main.py - Updated version
# import os
# import asyncio
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import Optional, Dict, Any
# import json
# import logging
# import traceback
# from video.runway import generate_runway_video

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# app = FastAPI()

# # CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "*"],  # Add your frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class VideoRequest(BaseModel):
#     prompt: str
#     style: str = "cinematic"
#     duration: int = 4
#     model: str = "stable-video-diffusion"

# # Simple in-memory storage for demo
# video_storage = {}

# @app.get("/")
# async def root():
#     return {"status": "online", "message": "Text-to-Video API"}

# @app.post("/generate")
# async def generate_video(request: VideoRequest):
#     try:
#         logger.info(f"Received request: {request.prompt} [{request.style}]")
        
#         # Simple response for testing - remove this when models work
#         video_storage["test"] = {
#             "status": "completed",
#             "video_url": "https://example.com/test.mp4",
#             "message": "Video generation in progress - using test mode",
#             "prompt": request.prompt,
#             "enhanced_prompt": f"Cinematic shot of {request.prompt}, 4K resolution, dramatic lighting"
#         }


        
#         return {
#             "status": "processing",
#             "message": "Video generation started",
#             "job_id": "test_123",
#             "estimated_time": 30,
#             "test_mode": True  # Indicate this is test mode
#         }
        
#     except Exception as e:
#         logger.error(f"Error in generate_video: {str(e)}")
#         logger.error(traceback.format_exc())
#         raise HTTPException(
#             status_code=500,
#             detail=f"Internal server error: {str(e)}"
#         )

# @app.get("/status/{job_id}")
# async def get_status(job_id: str):
#     if job_id in video_storage:
#         return video_storage[job_id]
#     return {"status": "unknown", "message": "Job not found"}

# # Health check endpoint
# @app.get("/health")
# async def health_check():
#     return {"status": "healthy", "timestamp": "2025-01-11T12:00:00Z"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)           


# new main.py - Current version

import os
import logging
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from enhancer import enhance_prompt
from video.runway import generate_runway_video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    prompt: str
    style: str = "cinematic"

@app.get("/")
async def root():
    return {"status": "online", "service": "text-to-video"}

@app.post("/generate")
async def generate_video(request: GenerateRequest):
    try:
        logger.info(f"🎬 GENERATE: {request.prompt} [{request.style}]")

        enhanced = enhance_prompt(request.prompt, request.style)
        video_url = generate_runway_video(enhanced, request.style)

        return {
            "status": "completed",
            "prompt": request.prompt,
            "enhanced_prompt": enhanced,
            "video_url": video_url
        }

    except Exception as e:
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
