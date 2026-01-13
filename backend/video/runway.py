import os
import time
import runwayml

client = runwayml.RunwayML(api_key=os.getenv("RUNWAYML_API_SECRET"))

def generate_runway_video(prompt, style="cinematic"):
    print(f"✨ Runway generating for: {prompt}")

    job = client.video.create(
        model="gen3-alpha",
        prompt=prompt,
        size="1280x720",
        duration=6,
        fps=24,
        seed=42
    )

    # Poll until finished
    while True:
        status = client.video.get(job.id)
        print("Status:", status.status)

        if status.status == "succeeded":
            return status.output[0].url
        
        if status.status == "failed":
            raise Exception("Runway failed!")
        
        time.sleep(2)




