from llm.groq_client import call_groq

def edit_interaction_tool(state):
    prompt = f"""
You are editing an existing CRM interaction.

User request:
{state["user_input"]}

Update the interaction details accordingly and return the updated fields.
"""

    llm_output = call_groq(prompt)

    return {
        "tool_result": llm_output
    }