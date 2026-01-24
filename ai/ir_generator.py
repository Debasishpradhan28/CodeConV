def build_ir_prompt(source, code):
    return f"""
You are a compiler control-flow analyzer.

Convert the following {source} program into
a CONTROL FLOW GRAPH suitable for a flowchart.

Rules:
- Identify start and end
- Identify input/output
- Identify processes
- Identify decisions
- Identify loops with back edges
- Output ONLY Mermaid flowchart syntax
- Use flowchart TD
- Do NOT explain anything
- Do NOT use markdown fences

Program:
{code}
"""
