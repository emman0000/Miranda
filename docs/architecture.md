# Miranda Architecture

## Purpose

This document describes the overall architecture of Miranda, an AI-powered conversational fashion assistant. It explains the major software components, how they interact, and how the system is intended to evolve over time.

The goal of this document is to provide a high-level understanding of the project before diving into implementation details.

---

# Project Overview

Miranda is designed as a modular AI agent capable of understanding user requests, maintaining conversational context, retrieving relevant fashion information, and generating personalized styling recommendations.

Rather than relying solely on a Large Language Model (LLM), Miranda combines multiple specialized components including memory management, retrieval, recommendation logic, and structured fashion data.

The architecture emphasizes modularity, maintainability, and future scalability.

---

# High-Level Architecture

                    User
                      │
                      ▼
           Conversational Interface
                      │
                      ▼
                Miranda Agent
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Personality      Memory Module   Recommendation
    Engine                              Engine
                                         │
                           ┌─────────────┴─────────────┐
                           ▼                           ▼
                   Retrieval System          Fashion Dataset
                           │
                           ▼
                     Response Generator
                           │
                           ▼
                         User

---

# Core Components

## 1. User Interface

The interface through which users interact with Miranda.

Current implementation:

- Command Line Interface (CLI)

Future implementations:

- Web application
- Mobile application
- Voice interface

---

## 2. Miranda Agent

The Miranda Agent serves as the central controller of the system.

Responsibilities include:

- Receiving user requests
- Coordinating system modules
- Managing conversation flow
- Constructing prompts
- Returning responses

The agent acts as the orchestration layer connecting all major components.

---

## 3. Personality Engine

Defines Miranda's conversational identity.

Responsibilities:

- Tone of voice
- Styling philosophy
- Prompt templates
- Behavioral rules
- Response consistency

This component ensures Miranda behaves like a fashion stylist rather than a generic chatbot.

---

## 4. Memory Module

Stores conversational context.

Current capabilities:

- Session-based memory

Future capabilities:

- Long-term memory
- User preferences
- Favorite brands
- Size information
- Wardrobe history
- Style evolution

---

## 5. Recommendation Engine

Responsible for generating fashion recommendations.

Inputs include:

- User preferences
- Occasion
- Budget
- Weather
- Fashion dataset

Outputs:

- Outfit recommendations
- Styling advice
- Alternative options
- Explanation of recommendations

---

## 6. Retrieval System

Provides Miranda with factual fashion knowledge.

Future responsibilities include:

- Searching product catalogs
- Retrieving clothing information
- Similar outfit search
- RAG (Retrieval-Augmented Generation)

---

## 7. Fashion Dataset

Structured repository of clothing items.

Example attributes:

- Product name
- Category
- Color
- Brand
- Material
- Season
- Style
- Price

This dataset serves as the primary knowledge source for recommendations.

---

# Data Flow

The following sequence illustrates how a typical interaction is processed.

1. User submits a request.

2. Miranda Agent receives the request.

3. Memory Module retrieves relevant conversation history.

4. Personality Engine prepares the system prompt.

5. Recommendation Engine determines whether external fashion knowledge is required.

6. Retrieval System searches the fashion dataset.

7. Retrieved information is combined with conversation context.

8. Gemini generates a response.

9. Miranda returns the final response to the user.

---

# Project Structure Responsibilities

docs/
: Documentation

src/agents/
: Agent orchestration

src/prompts/
: Prompt templates

src/memory/
: Memory management

src/recommendation/
: Recommendation algorithms

src/retrieval/
: Fashion search and retrieval

src/vision/
: Computer vision modules

src/utils/
: Shared utilities

data/
: Fashion datasets

tests/
: Automated testing

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Programming Language | Python |
| LLM | Google Gemini |
| Agent Framework | Google ADK |
| Dataset | Kaggle Fashion Product Dataset |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Computer Vision (Future) | OpenCV |
| Embeddings (Future) | Sentence Transformers |
| Version Control | Git |

---

# Future Architecture

The current architecture is intentionally modular to support future extensions.

Planned additions include:

- Retrieval-Augmented Generation (RAG)
- Vector database
- Vision-language models
- User profile service
- Outfit ranking algorithms
- Fashion trend analysis
- Multi-agent collaboration

These additions can be integrated without significant modifications to the existing architecture.

---

# Design Principles

The architecture follows several guiding principles.

### Modularity

Each component performs a single responsibility.

### Scalability

New components should be integrated without major refactoring.

### Maintainability

Code should remain organized and easy to understand.

### Reusability

Modules should be reusable across future projects.

### Extensibility

Future AI capabilities should be added with minimal disruption to existing functionality.
