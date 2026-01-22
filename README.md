# AI-First CRM HCP Module

An AI-powered Customer Relationship Management (CRM) system designed for Life Science Field Representatives.  
The system uses a LangGraph-based AI agent to convert free-text HCP interactions into structured CRM records, with a React frontend and FastAPI backend.

---

## Objective

Enable field representatives to log Healthcare Professional (HCP) interactions using:
- Natural language (AI Chat)
- Structured CRM form (auto-filled by AI)

The AI agent extracts, validates, and manages interaction data using multiple LangGraph tools.

---

## Core Features

- AI Chat interface for logging HCP interactions
- Automatic extraction of structured CRM fields
- Editable CRM form populated by AI
- Interaction history retrieval
- AI-generated summaries
- AI-suggested follow-up actions
- Side-by-side Chat + Form UI

---

## Tech Stack

### Backend
- Python
- FastAPI
- LangGraph
- Groq LLM
- REST APIs

### Frontend
- React (Create React App)
- JavaScript
- Fetch API

---

## LangGraph Tools Implemented

1. **log_interaction**
   - Extracts structured CRM data from free-text input

2. **edit_interaction**
   - Allows correction of extracted fields

3. **get_history**
   - Retrieves historical interactions (mocked)

4. **generate_summary**
   - Generates concise interaction summaries

5. **suggest_followup**
   - Suggests next best actions for the field representative

Tool routing is handled using an intent-based LangGraph router.

---




