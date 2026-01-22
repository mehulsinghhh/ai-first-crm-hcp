from llm.groq_client import call_groq

def suggest_followup_tool(state):
    prompt = f"""
You are a CRM AI assistant.

Based on the interaction below, suggest next best follow-up actions
for a life science field representative.

Interaction:
{state["user_input"]}
"""

    llm_output = call_groq(prompt)

    return {
        "tool_result": llm_output
    }