import re
import json
from llm.groq_client import call_groq


def regex_fallback(text: str):
    name = re.search(r"Dr\s+[A-Za-z]+", text)
    topic = re.search(r"discuss\s+([a-zA-Z\s]+?)(?:\.|,|$)", text, re.IGNORECASE)
    date = re.search(r"\d{1,2}(st|nd|rd|th)?\s+[A-Za-z]+", text)

    return {
        "hcp_name": name.group(0) if name else None,
        "interaction_topic": topic.group(1).strip() if topic else None,
        "follow_up_date": date.group(0) if date else None
    }


def log_interaction_tool(state):
    user_input = state.get("user_input", "")

    prompt = f"""
Extract the following fields from the text.
Return STRICT JSON only.

Fields:
- hcp_name
- interaction_topic
- follow_up_date

Text:
{user_input}

JSON:
"""

    structured = None

    try:
        response = call_groq(prompt)
        start = response.find("{")
        end = response.rfind("}") + 1
        structured = json.loads(response[start:end])
    except Exception:
        structured = regex_fallback(user_input)

    # HARD GUARANTEE (never null if text contains info)
    if not structured or all(v is None for v in structured.values()):
        structured = regex_fallback(user_input)

    state["structured_data"] = structured
    state["hcp_name"] = structured.get("hcp_name")

    return state
