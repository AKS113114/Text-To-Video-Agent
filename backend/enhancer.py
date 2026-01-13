# enhancer.py - Simplified with fallbacks
import os
import random
import logging

logger = logging.getLogger(__name__)

# Fallback prompt templates if APIs fail
STYLE_TEMPLATES = {
    "cinematic": [
        "Cinematic shot of {prompt}, 4K resolution, dramatic lighting, film grain, wide angle lens",
        "Epic cinematic scene: {prompt}, masterpiece, photorealistic, cinematic lighting",
        "Film scene: {prompt}, shot on Arri Alexa, anamorphic lens, cinematic color grade"
    ],
    "animation": [
        "Animated style: {prompt}, Pixar style, 3D animation, vibrant colors, cartoon",
        "Anime style: {prompt}, Studio Ghibli, beautiful animation, detailed artwork",
        "Cartoon: {prompt}, Disney style, expressive characters, smooth animation"
    ],
    "realistic": [
        "Photorealistic: {prompt}, detailed, sharp focus, 8K, professional photography",
        "Realistic scene: {prompt}, natural lighting, detailed textures, realistic",
        "Documentary style: {prompt}, realistic lighting, natural colors, authentic"
    ]
}

def enhance_prompt_simple(prompt: str, style: str = "cinematic") -> str:
    """Simple prompt enhancement without external APIs"""
    templates = STYLE_TEMPLATES.get(style, STYLE_TEMPLATES["cinematic"])
    template = random.choice(templates)
    return template.format(prompt=prompt)

def enhance_prompt(prompt: str, style: str = "cinematic") -> str:
    """Enhanced prompt with fallback to simple version"""
    try:
        # Try Gemini first
        from google import genai
        import google.generativeai as genai_legacy
        
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        if not GEMINI_API_KEY:
            logger.warning("GEMINI_API_KEY not found, using simple enhancement")
            return enhance_prompt_simple(prompt, style)
        
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Create prompt for enhancement
        enhancement_text = f"""
        Enhance this video description for AI video generation.
        
        Original prompt: "{prompt}"
        Style: {style}
        
        Make it more visual, descriptive, and suitable for video generation.
        Include details about camera movement, lighting, atmosphere, and composition.
        Keep it concise (1-2 sentences).
        """
        
        # Try with new API
        try:
            client = genai.Client(api_key=GEMINI_API_KEY)
            response = client.models.generate_content(
                model="gemini-1.5-flash",  # Use flash model, it's more available
                contents=enhancement_text
            )
            enhanced = response.text.strip()
        except:
            # Fallback to legacy API
            model = genai_legacy.GenerativeModel('gemini-pro')
            response = model.generate_content(enhancement_text)
            enhanced = response.text.strip()
        
        logger.info(f"Enhanced prompt: {enhanced}")
        return enhanced
        
    except Exception as e:
        logger.error(f"Gemini enhancement failed: {e}, using simple enhancement")
        return enhance_prompt_simple(prompt, style)
