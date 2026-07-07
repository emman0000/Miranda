<div align="center">

# 🧵 Miranda — System Architecture

<p>
  <img src="https://img.shields.io/badge/status-in%20development-2ea44f?style=flat-square" alt="status">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="python">
  <img src="https://img.shields.io/badge/LLM-Google%20Gemini-4285F4?style=flat-square&logo=google&logoColor=white" alt="gemini">
  <img src="https://img.shields.io/badge/framework-Google%20ADK-FF69B4?style=flat-square" alt="adk">
</p>

<sub>An AI-powered conversational fashion assistant — modular by design, stylist by nature.</sub>

</div>

<br>

## 📖 Purpose

This document describes the overall architecture of **Miranda**, an AI-powered conversational fashion assistant. It explains the major software components, how they interact, and how the system is intended to evolve over time.

The goal is to give anyone approaching this codebase a clear mental model **before** diving into implementation details.

<br>

## 🎯 Project Overview

Miranda is designed as a **modular AI agent** capable of understanding user requests, maintaining conversational context, retrieving relevant fashion information, and generating personalized styling recommendations.

Rather than relying solely on a Large Language Model, Miranda combines several specialized components — memory management, retrieval, recommendation logic, and structured fashion data — each with a single, well-defined job.

> The architecture emphasizes **modularity**, **maintainability**, and **future scalability**.

<br>

## 🏗️ High-Level Architecture

```mermaid
flowchart TB
    U([👤 User]) --> UI[💬 Conversational Interface]
    UI --> AGENT{{🧠 Miranda Agent}}

    AGENT --> PE[🎭 Personality Engine]
    AGENT --> MM[(🗂️ Memory Module)]
    AGENT --> RE[✨ Recommendation Engine]

    RE --> RS[🔎 Retrieval System]
    RE --> FD[(👗 Fashion Dataset)]
    RS --> FD

    RS --> RG[📝 Response Generator]
    PE -.-> RG
    MM -.-> RG

    RG --> U

    classDef core fill:#6C5CE7,stroke:#4834d4,color:#fff,font-weight:bold;
    classDef store fill:#00B894,stroke:#00806a,color:#fff;
    classDef io fill:#FDCB6E,stroke:#e0a800,color:#222;

    class AGENT,RE,RS,RG core
    class MM,FD store
    class U,UI io
```

<br>

## 🧩 Core Components

### 1. User Interface

The interface through which users interact with Miranda.

| Status | Interface |
|---|---|
| ✅ Current | Command Line Interface (CLI) |
| 🔜 Planned | Web application |
| 🔜 Planned | Mobile application |
| 🔜 Planned | Voice interface |

---

### 2. Miranda Agent

The **central controller** of the system — the orchestration layer connecting all major components.

Responsibilities:
- Receiving user requests
- Coordinating system modules
- Managing conversation flow
- Constructing prompts
- Returning responses

---

### 3. Personality Engine

Defines Miranda's conversational identity — the difference between *"a chatbot that knows about clothes"* and *"a stylist you'd actually trust."*

Responsibilities:
- Tone of voice
- Styling philosophy
- Prompt templates
- Behavioral rules
- Response consistency

---

### 4. Memory Module

Stores conversational context so Miranda doesn't forget who it's talking to mid-conversation.

| Status | Capability |
|---|---|
| ✅ Current | Session-based memory |
| 🔜 Planned | Long-term memory |
| 🔜 Planned | User preferences |
| 🔜 Planned | Favorite brands |
| 🔜 Planned | Size information |
| 🔜 Planned | Wardrobe history |
| 🔜 Planned | Style evolution |

---

### 5. Recommendation Engine

The component responsible for turning context into concrete styling advice.

**Inputs:** user preferences · occasion · budget · weather · fashion dataset

**Outputs:** outfit recommendations · styling advice · alternative options · explanation of recommendations

---

### 6. Retrieval System

Gives Miranda factual, grounded fashion knowledge rather than relying purely on model recall.

Planned responsibilities:
- Searching product catalogs
- Retrieving clothing information
- Similar-outfit search
- Retrieval-Augmented Generation (RAG)

---

### 7. Fashion Dataset

The structured repository of clothing items that powers recommendations.

Example attributes: `product name` · `category` · `color` · `brand` · `material` · `season` · `style` · `price`

<br>

## 🔄 Data Flow

The sequence below illustrates how a typical interaction is processed, end to end.

```mermaid
sequenceDiagram
    actor User
    participant Agent as Miranda Agent
    participant Memory as Memory Module
    participant Personality as Personality Engine
    participant Recommend as Recommendation Engine
    participant Retrieval as Retrieval System
    participant Gemini as Gemini (LLM)

    User->>Agent: Submits request
    Agent->>Memory: Retrieve conversation history
    Memory-->>Agent: Relevant context
    Agent->>Personality: Prepare system prompt
    Personality-->>Agent: Styled prompt
    Agent->>Recommend: Evaluate request
    Recommend->>Retrieval: Query fashion dataset (if needed)
    Retrieval-->>Recommend: Retrieved fashion knowledge
    Recommend->>Gemini: Context + retrieved data + prompt
    Gemini-->>Agent: Generated response
    Agent-->>User: Final styling recommendation
```

<br>

## 📁 Project Structure

```mermaid
graph LR
    root[miranda/] --> docs[docs/]
    root --> src[src/]
    root --> data[data/]
    root --> tests[tests/]

    src --> agents[agents/]
    src --> prompts[prompts/]
    src --> memory[memory/]
    src --> recommendation[recommendation/]
    src --> retrieval[retrieval/]
    src --> vision[vision/]
    src --> utils[utils/]

    style root fill:#6C5CE7,stroke:#4834d4,color:#fff
    style src fill:#00B894,stroke:#00806a,color:#fff
```

| Path | Responsibility |
|---|---|
| `docs/` | Documentation |
| `src/agents/` | Agent orchestration |
| `src/prompts/` | Prompt templates |
| `src/memory/` | Memory management |
| `src/recommendation/` | Recommendation algorithms |
| `src/retrieval/` | Fashion search and retrieval |
| `src/vision/` | Computer vision modules |
| `src/utils/` | Shared utilities |
| `data/` | Fashion datasets |
| `tests/` | Automated testing |

<br>

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| LLM | Google Gemini |
| Agent Framework | Google ADK |
| Dataset | Kaggle Fashion Product Dataset |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Computer Vision *(future)* | OpenCV |
| Embeddings *(future)* | Sentence Transformers |
| Version Control | Git |

<br>

## 🚧 Future Architecture

The current architecture is intentionally modular to support future extensions **without significant rework**.

```mermaid
mindmap
  root((Miranda))
    Retrieval-Augmented Generation
      Vector database
    Vision-Language Models
      Outfit photo understanding
    User Profile Service
      Preferences
      Sizes
      History
    Recommendation Upgrades
      Outfit ranking algorithms
      Fashion trend analysis
    Multi-Agent Collaboration
```

<br>

## 🧭 Design Principles

| Principle | Meaning |
|---|---|
| **Modularity** | Each component performs a single responsibility |
| **Scalability** | New components integrate without major refactoring |
| **Maintainability** | Code stays organized and easy to understand |
| **Reusability** | Modules are reusable across future projects |
| **Extensibility** | Future AI capabilities are added with minimal disruption |

<br>

<div align="center">
<sub>Miranda — styled by design, engineered for growth. 🧷</sub>
</div>
