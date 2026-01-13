from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time
import uuid
import random

class SimpleHandler(BaseHTTPRequestHandler):
    # Sample videos for responses
    SAMPLE_VIDEOS = [
    # Animals/Pets
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
    # Cars/Vehicles
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4",
    # Office/Work
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4",
    # Nature/Wildlife
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
    # Beach/Ocean
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4",
    # General
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4"
    ]
    
    def do_GET(self):
        print(f"📥 GET: {self.path}")
        
        if self.path == '/health' or self.path == '/health/':
            self.send_success({
                "status": "healthy",
                "timestamp": time.time(),
                "service": "text-to-video-api"
            })
            
        elif self.path.startswith('/status/'):
            job_id = self.path.split('/')[-1]
            self.send_success({
                "status": "completed",
                "job_id": job_id,
                "video_url": random.choice(self.SAMPLE_VIDEOS)
            })
            
        elif self.path == '/' or self.path == '':
            self.send_success({
                "message": "Text to Video API",
                "endpoints": [
                    "GET  /health",
                    "POST /generate",
                    "GET  /status/{id}"
                ]
            })
            
        else:
            self.send_error(404, {"error": "Not found"})
    
    # def do_POST(self):
    #     print(f"📥 POST: {self.path}")
        
    #     if self.path == '/generate' or self.path == '/generate/':
    #         try:
    #             content_length = int(self.headers['Content-Length'])
    #             body = self.rfile.read(content_length)
    #             data = json.loads(body)
                
    #             job_id = f"vid_{uuid.uuid4().hex[:8]}"
    #             video_url = random.choice(self.SAMPLE_VIDEOS)
                
    #             self.send_success({
    #                 "status": "completed",
    #                 "job_id": job_id,
    #                 "video_url": video_url,
    #                 "message": f"Video generated for: {data.get('prompt', 'unknown')}",
    #                 "enhanced_prompt": f"Cinematic shot of {data.get('prompt', 'unknown')}, 4K resolution",
    #                 "prompt": data.get('prompt', ''),
    #                 "style": data.get('style', 'cinematic'),
    #                 "duration": data.get('duration', 4)
    #             })
                
    #         except Exception as e:
    #             self.send_error(500, {"error": str(e)})
    #     else:
    #         self.send_error(404, {"error": "Not found"})

    # In simple_server.py, modify the do_POST method:

# Replace the do_POST method with this:
# Replace the do_POST method with this:
def do_POST(self):
    print(f"📥 POST: {self.path}")
    
    if self.path == '/generate' or self.path == '/generate/':
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)
            
            prompt = data.get('prompt', '').lower()
            job_id = f"vid_{uuid.uuid4().hex[:8]}"
            
            # SMART VIDEO MATCHING BASED ON KEYWORDS
            if any(word in prompt for word in ['dog', 'cat', 'pet', 'animal', 'puppy', 'kitten', 'walking', 'running']):
                video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
                enhanced_prompt = f"Adorable {data.get('prompt', 'pet')}, happy animals, cute, heartwarming"
                matched_type = "animal"
                
            elif any(word in prompt for word in ['car', 'vehicle', 'drive', 'racing', 'drift', 'speed', 'drifting']):
                video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4"
                enhanced_prompt = f"Exciting {data.get('prompt', 'car')} action, fast-paced, dynamic, thrilling"
                matched_type = "car"
                
            elif any(word in prompt for word in ['office', 'work', 'computer', 'desk', 'meeting', 'business']):
                video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4"
                enhanced_prompt = f"Professional {data.get('prompt', 'work')} scene, office environment"
                matched_type = "office"
                
            elif any(word in prompt for word in ['elephant', 'nature', 'wildlife', 'jungle', 'forest']):
                video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"
                enhanced_prompt = f"Beautiful {data.get('prompt', 'nature')} scene, wildlife documentary"
                matched_type = "nature"
                
            elif any(word in prompt for word in ['beach', 'ocean', 'surf', 'wave', 'water', 'sea']):
                video_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4"
                enhanced_prompt = f"Scenic {data.get('prompt', 'beach')} view, ocean waves"
                matched_type = "beach"
                
            else:
                # Default random video
                import random
                videos = [
                    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
                    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4",
                    "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4",
                ]
                video_url = random.choice(videos)
                enhanced_prompt = f"Cinematic shot of {data.get('prompt', 'scene')}"
                matched_type = "random"
            
            self.send_success({
                "status": "completed",
                "job_id": job_id,
                "video_url": video_url,
                "message": f"Video generated for: {data.get('prompt', 'unknown')}",
                "enhanced_prompt": enhanced_prompt,
                "prompt": data.get('prompt', ''),
                "style": data.get('style', 'cinematic'),
                "duration": data.get('duration', 4),
                "matched_type": matched_type  # Added this
            })
            
        except Exception as e:
            self.send_error(500, {"error": str(e)})
    else:
        self.send_error(404, {"error": "Not found"})
    
    # ... rest of the code ...
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def send_success(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def send_error(self, code, data):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

def run():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    
    print('🚀' * 40)
    print('TEXT TO VIDEO BACKEND SERVER')
    print('Address: http://127.0.0.1:8000')
    print('')
    print('Endpoints:')
    print('  GET  /                - API information')
    print('  GET  /health          - Health check')
    print('  POST /generate        - Generate video from text')
    print('  GET  /status/{id}     - Check video status')
    print('')
    print('Sample request:')
    print('  curl -X POST http://127.0.0.1:8000/generate \\')
    print('    -H "Content-Type: application/json" \\')
    print('    -d \'{"prompt":"dog surfing","style":"cinematic"}\'')
    print('🚀' * 40)
    print('')
    print('Press Ctrl+C to stop the server')
    
    httpd.serve_forever()

if __name__ == '__main__':
    run()