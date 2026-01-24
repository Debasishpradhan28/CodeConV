import os
import google.generativeai as genai

def init_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def convert_code(prompt):
    try:
        model = genai.GenerativeModel("gemini-3-flash-preview")
        response = model.generate_content(prompt)

        if (
            response.candidates
            and len(response.candidates) > 0
            and response.candidates[0].content
            and response.candidates[0].content.parts
            and len(response.candidates[0].content.parts) > 0
        ):
            return response.candidates[0].content.parts[0].text.strip()

        return "AI returned no output. Please wait 30 seconds and try again."

    except Exception as e:
        return f"AI error: {str(e)}"
