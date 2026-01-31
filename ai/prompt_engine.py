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

# explain prompt

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


# logic complexity

def build_complexity_prompt(code):
    return f"""
You are a senior software engineer analyzing program logic.

Return the analysis in clean plain text.

Formatting rules:
- Do NOT use markdown
- Do NOT use bullets like *
- Do NOT use **bold**
- Do NOT use symbols like $ or LaTeX
- Use clear headings and line breaks
- Write like ChatGPT explains concepts to students
- Do NOT use markdown
- Do NOT use symbols like **, ###, or *
- Do NOT use numbered markdown format
- Write in clean plain text
- Separate sections using clear titles
- Sound like ChatGPT explaining professionally

Use this structure exactly:

Program Complexity Analysis

Decision Depth:
<value>

Loop Nesting Depth:
<value>

Time Complexity:
<value>

Space Complexity:
<value>

Logic Risk Level:
<Low / Medium / High>

Explanation:
<short clear explanation>

Program:
{code}
"""


#debug reasoner
def build_debug_prompt(code):
    return f"""
You are a senior software engineer.

Analyze the program logic and identify:

- Possible logical bugs
- Edge cases
- Risky assumptions
- Scenarios where the program may fail

Do NOT rewrite the code.
Do NOT fix the code.
Only explain reasoning.

Formatting rules:
- Do NOT use markdown
- Do NOT use symbols like **, ###, or *
- Do NOT use numbered markdown format
- Write in clean plain text
- Separate sections using clear titles
- Sound like ChatGPT explaining professionally

Program:
{code}
"""

#interview
def build_interview_prompt(code):
    return f"""
You are an interview panel.

Generate:
- 5 interview questions
- 2 follow-up questions
- 1 optimization question

Based only on the program logic.

Formatting rules:
- Do NOT use markdown
- Do NOT use symbols like **, ###, or *
- Do NOT use numbered markdown format
- Write in clean plain text
- Separate sections using clear titles
- Sound like ChatGPT explaining professionally

Use this format exactly:

Interview Questions:
<each question on a new line>

Follow-up Questions:
<each question on a new line>

Optimization Question:
<single clear question>

Do NOT provide answers.
Do NOT show code.

Program:
{code}
"""