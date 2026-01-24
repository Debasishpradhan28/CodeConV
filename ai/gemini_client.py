import google.generativeai as genai
import os

def init_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def convert_code(prompt):
    model = genai.GenerativeModel("gemini-3-flash-preview")
    response = model.generate_content(prompt)

    try:
        if response.candidates and len(response.candidates) > 0:
            parts = response.candidates[0].content.parts
            if parts and len(parts) > 0:
                return parts[0].text
    except:
        pass

    return "Error: AI returned empty response. Please retry after a few seconds."
