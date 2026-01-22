from llm.groq_client import call_groq

def generate_summary_tool(state):
    prompt = f"""
Generate a clear and concise CRM visit summary for the following interaction:

{state["user_input"]}
"""

    llm_output = call_groq(prompt)

    return {
        "summary": llm_output
    }