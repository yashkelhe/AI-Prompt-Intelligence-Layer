# AI Prompt Intelligence Layer

An AI-powered Prompt Analysis Engine that helps users understand the complexity, domain, and requirements of a prompt before sending it to an LLM.

The system analyzes a user prompt, estimates its complexity, recommends a suitable AI model, and provides an estimated token usage and cost.

---

## Features

### Prompt Analysis

Analyzes a prompt and extracts:

- Task Type
- Complexity Score
- Coding Score
- Reasoning Score
- Creativity Score
- Domain Detection

### Model Recommendation

Based on the analysis, the system recommends the most suitable model for the task.

Current supported recommendations:

- Claude Sonnet
- DeepSeek V3
- Gemini Flash

### Token Estimation

Estimates the number of tokens required for the prompt.

### Cost Estimation

Calculates an estimated execution cost based on the recommended model and token usage.

### REST API

Built using FastAPI and exposed through a simple API endpoint.

---

## Architecture

```text
User Prompt
     │
     ▼
┌──────────────────┐
│ Prompt Analyzer  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Gemini Analysis  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Structured Data  │
└────────┬─────────┘
         │
         ├────────► Complexity Analysis
         │
         ├────────► Domain Detection
         │
         ├────────► Token Estimation
         │
         └────────► Model Recommendation
                        │
                        ▼
                Final Response
```

---

## Project Structure

```text
AI-Prompt-Intelligence-Layer/

├── analyzers/
│   └── prompt_analyzer.py
│
├── estimators/
│   ├── token_estimator.py
│   └── cost_estimator.py
│
├── registry/
│   └── models.py
│
├── routers/
│   └── model_router.py
│
├── schemas/
│   └── response.py
│
├── services/
│   └── gemini_service.py
│
├── app.py
├── requirements.txt
└── .env
```

---

## Tech Stack

### Backend

- Python
- FastAPI
- Pydantic

### AI

- Google Gemini API

### Utilities

- python-dotenv
- tiktoken

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/AI-Prompt-Intelligence-Layer.git
cd AI-Prompt-Intelligence-Layer
```

### Create Virtual Environment

```bash
conda create -n ai-rag python=3.12
conda activate ai-rag
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Project

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Analyze Prompt

**POST** `/analyze`

### Request

```json
{
  "prompt": "Build a production ready RAG system using LangGraph"
}
```

### Sample Response

```json
{
  "analysis": {
    "task_type": ["system_design", "code_generation", "architectural_planning"],
    "complexity": 9,
    "coding_score": 95,
    "reasoning_score": 90,
    "creativity_score": 40,
    "domain": [
      "Large Language Models",
      "Natural Language Processing",
      "AI Frameworks",
      "System Architecture",
      "Software Engineering",
      "DevOps"
    ]
  },
  "recommended_model": "claude-sonnet",
  "estimated_tokens": 10,
  "estimated_cost": 0.00003
}
```

---

## Recommendation Logic

Current routing rules:

```text
Coding Score > 85
    → Claude Sonnet

Reasoning Score > 80
    → Claude Sonnet

Coding Score > 60
    → DeepSeek V3

Else
    → Gemini Flash
```

---

## Example Workflow

```text
User enters prompt
        │
        ▼
Prompt sent to Gemini
        │
        ▼
Prompt analyzed
        │
        ▼
Complexity calculated
        │
        ▼
Token estimate generated
        │
        ▼
Model recommendation generated
        │
        ▼
Cost estimate calculated
        │
        ▼
Response returned to user
```

---

## Example Use Cases

- Selecting the right LLM for a task
- Understanding prompt complexity
- Estimating AI execution costs
- Analyzing coding and reasoning requirements
- Evaluating software architecture prompts
- AI project planning and assessment

---

## Future Improvements

- Improved token estimation
- Multi-model comparison
- Prompt quality scoring
- Prompt optimization
- Task decomposition
- Advanced routing engine
- Real-time pricing integration

---

## Author

**Yash Kelhe**

Software Engineer | Full Stack Developer | AI Enthusiast

GitHub: https://github.com/yashkelhe
LinkedIn: https://linkedin.com/in/yashkelhe

---

⭐ If you found this project useful, consider giving it a star.
