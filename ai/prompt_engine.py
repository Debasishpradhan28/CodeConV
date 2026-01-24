def build_convert_prompt(source, target, code):
    return f"""
You are an expert software engineer.

Convert the following program:

Source Language: {source}
Target Language: {target}

Rules:
- Maintain same logic
- Use best practices
- Add imports if required
- Return ONLY code
- No explanation

Code:
{code}
"""



# def build_explain_prompt(source, code):
#     return f"""
# You are a programming tutor.

# Explain the logic of the following {source} code
# in simple and natural human language.

# Rules:
# - Do NOT use markdown
# - Do NOT use symbols like **, __, ###, ---
# - Do NOT format text
# - Do NOT show code
# - Write like ChatGPT explaining to a student
# - Use short paragraphs
# - Keep explanation clear and friendly

# Code:
# {code}
# """

def build_explain_prompt(source, code):
    return f"""
Explain the logic of the following {source} program in simple English.

Rules:
- Do not show code
- Do not use flowchart syntax
- Do not use symbols like --> or /
- Write in numbered steps
- Explain loops and decisions clearly
- Sound like a teacher

Program:
{code}
"""

