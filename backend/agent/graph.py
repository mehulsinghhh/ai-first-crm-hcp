from langgraph.graph import StateGraph, END

from agent.state import AgentState
from agent.router import route_intent

from agent.tools.log_interaction import log_interaction_tool
from agent.tools.edit_interaction import edit_interaction_tool
from agent.tools.get_history import get_interaction_history_tool
from agent.tools.generate_summary import generate_summary_tool
from agent.tools.suggest_followup import suggest_followup_tool


graph = StateGraph(AgentState)

graph.add_node("log_interaction", log_interaction_tool)
graph.add_node("edit_interaction", edit_interaction_tool)
graph.add_node("get_history", get_interaction_history_tool)
graph.add_node("generate_summary", generate_summary_tool)
graph.add_node("suggest_followup", suggest_followup_tool)

graph.set_conditional_entry_point(route_intent)

graph.add_edge("log_interaction", END)
graph.add_edge("edit_interaction", END)
graph.add_edge("get_history", END)
graph.add_edge("generate_summary", END)
graph.add_edge("suggest_followup", END)

agent_app = graph.compile()
# Compile the graph
agent_app = graph.compile()