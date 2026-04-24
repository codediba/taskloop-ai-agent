# taskloop-ai-agent
Autonomous AI agent with tool use and execution-evaluation loop built using LangGraph

## Overview

TaskLoop is an AI system that can plan, execute, and evaluate its own work.

Instead of returning a single response, it follows an iterative process to improve results until the task is completed or clarification is needed.

**Core loop:**

Task → Execute → Evaluate → Improve → Final Output

---

## Demo

### Task Execution
![UI Demo](demo.png)

### Generated Output File
![Output](output.png)

### Web Search (Tool Usage)
![Browser](browser.png)

### Push Notification
![Notification](notification.png)

---

## Features

- Tool-based reasoning using LangChain  
- Execution–evaluation loop powered by LangGraph  
- Web browsing with Playwright  
- Web search using Google Serper API  
- Python execution tool  
- File system interaction (read/write outputs)  
- Push notifications via Pushover  
- Self-evaluation loop using LLMs  
- Interactive UI with Gradio  

---

## Architecture

The agent is built around a two-stage loop:

- **Worker**  
  Executes tasks using available tools (search, browser, Python, file system)

- **Evaluator**  
  Assesses whether the success criteria are met and provides feedback

This loop is orchestrated using **LangGraph** and continues until:
- the task is completed, or  
- additional user input is required  

State is managed using **LangGraph’s in-memory checkpointing (MemorySaver)**.

---

## Example Task

**Input:**

Find a great restaurant in Fredericton and generate a report. Send a push notification with the name and phone number.

**What the agent does:**

- Searches the web  
- Opens and reads relevant pages  
- Extracts and summarizes information  
- Writes a structured report to file  
- Sends a notification  
- Evaluates its own result and iterates if needed  

---

## Tech Stack

- Python  
- LangChain (tool integration)  
- LangGraph (agent orchestration and loop)  
- OpenAI API (LLM)  
- Playwright (web browsing)  
- Google Serper API (search)  
- Wikipedia API  
- Python REPL tool  
- FileManagementToolkit (file operations)  
- Gradio (UI)  
- Pushover API (notifications)  

---

## Installation

```bash
pip install -r requirements.txt
playwright install
