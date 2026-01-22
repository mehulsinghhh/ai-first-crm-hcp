from typing import TypedDict, Optional, Dict
from pydantic import BaseModel

class AgentState(TypedDict):
    user_input: str
    structured_data: Optional[Dict]

    # Extracted structured fields
    hcp_name: Optional[str] = None
    follow_up_date: Optional[str] = None

    # AI-generated summary
    interaction_summary: Optional[str] = None

    # Final structured CRM record
    structured_data: Optional[Dict] = None