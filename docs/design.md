<div align="center">

# 🧵 Miranda — Design Document

<p>
  <img src="https://img.shields.io/badge/status-living%20document-2ea44f?style=flat-square" alt="status">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="python">
  <img src="https://img.shields.io/badge/LLM-Google%20Gemini-4285F4?style=flat-square&logo=google&logoColor=white" alt="gemini">
  <img src="https://img.shields.io/badge/type-blueprint-8A2BE2?style=flat-square" alt="blueprint">
</p>

<sub>The implementation blueprint for Miranda — updated as the system grows.</sub>

</div>

<br>

> 📌 **This is a living document.** Unlike `ARCHITECTURE.md`, which describes the overall system shape, this file is the working blueprint — the one to update every time a module's responsibilities, data, or pipeline changes.

<br>

## 📖 Purpose

This document defines the **detailed software design** for Miranda, an AI-powered conversational fashion assistant.

It describes:
- the responsibilities of each software module
- the flow of data between components
- the implementation decisions guiding development

Where the Architecture Document answers *"what does the system look like?"*, this document answers **"how exactly is it built?"**

<br>

## 🎯 Design Goals

Miranda's design is guided by six principles:

| Goal | What it means in practice |
|---|---|
| 🧩 **Modular development** | Each module can be built, tested, and replaced independently |
| 🎯 **Separation of responsibilities** | No module does more than one job |
| 🧪 **Easy testing** | Modules are small enough to unit test in isolation |
| 📈 **Future scalability** | New capabilities slot in without rewrites |
| 📖 **Readable code** | Anyone should be able to follow the logic without a walkthrough |
| 🔌 **Extensible AI capabilities** | New models, tools, or data sources can be swapped in |

<br>

---

## 🧩 Module Design

Each module below has a single job. This section is the first place to update whenever a responsibility shifts.

### 🧠 Agent — `src/agents/`

**Purpose:** Acts as the central controller.

| | |
|---|---|
| **Receives** | User input |
| **Builds** | Prompts |
| **Coordinates** | All other modules |
| **Returns** | Final responses |

---

### 🎭 Personality — `src/prompts/`

**Purpose:** Defines Miranda's behavior and voice.

Responsibilities:
- Tone
- Writing style
- Fashion expertise
- Response formatting

---

### 🗂️ Memory — `src/memory/`

**Purpose:** Maintains conversation context.

**Stores:**
- Conversation history
- User preferences
- Style preferences
- Favorite colors
- Budget
- Occasion history

| Status | Implementation |
|---|---|
| ✅ Current | Session memory |
| 🔜 Future | Persistent user memory |

---

### 🔎 Retrieval — `src/retrieval/`

**Purpose:** Searches the fashion dataset.

Future features:
- Similar products
- Semantic search
- Vector retrieval
- Metadata filtering

---

### 👁️ Vision — `src/vision/`

**Purpose:** Analyzes clothing images.

Future tasks:
- Clothing classification
- Color extraction
- Style recognition
- Similar outfit search

<br>

---

## 🗃️ Data Models

Two core entities anchor Miranda's data layer today. This section grows as new models are introduced.

```mermaid
erDiagram
    USER_PROFILE {
        string name
        list favorite_colors
        list favorite_brands
        float budget
        string gender
        list sizes
        list preferred_styles
        list purchase_history
    }

    FASHION_ITEM {
        string id
        string title
        string brand
        string category
        string color
        float price
        string season
        string style
        string image
        string description
    }

    USER_PROFILE ||--o{ FASHION_ITEM : "receives recommendations from"
```

<br>

---

## 🔄 System Data Flow

How a single request travels through Miranda end-to-end.

```mermaid
flowchart TB
    A([👤 User]) --> B[✅ Input Validation]
    B --> C[(🗂️ Memory Retrieval)]
    C --> D[📝 Prompt Construction]
    D --> E[(👗 Dataset Retrieval)]
    E --> F[✨ Recommendation Engine]
    F --> G[🤖 Gemini]
    G --> H[🎨 Response Formatting]
    H --> I([📤 Output])

    classDef core fill:#6C5CE7,stroke:#4834d4,color:#fff,font-weight:bold;
    classDef store fill:#00B894,stroke:#00806a,color:#fff;
    classDef io fill:#FDCB6E,stroke:#e0a800,color:#222;

    class D,F,H core
    class C,E store
    class A,B,G,I io
```

### Prompt Composition

What actually gets assembled and sent to Gemini:

```mermaid
flowchart LR
    SP[🎭 System Prompt] --> GM[🤖 Gemini]
    CH[🗂️ Conversation History] --> GM
    RC[👗 Retrieved Fashion Context] --> GM
    UM[💬 User Message] --> GM

    style GM fill:#4285F4,stroke:#2b5fb0,color:#fff,font-weight:bold
```

<br>

---

## 🧠 Memory Design

What Miranda should remember — split by how long it should stick around.

| Term | Contents |
|---|---|
| **Short-term** | Current conversation |
| **Long-term** | Favorite brands · clothing sizes · favorite colors · fashion goals · budget · preferred stores · seasonal preferences |

> 💡 You don't have to implement all of this yet — the point of this section is to **define the target shape** of memory so future work has a clear destination.

<br>

---

## 🚀 Recommendation Pipeline

The heart of Miranda, shown at two stages of maturity.

**Today:**

```mermaid
flowchart LR
    A[💬 User asks for outfit] --> B[🤖 Gemini] --> C[📤 Response]

    style B fill:#4285F4,stroke:#2b5fb0,color:#fff
```

**Where it's heading:**

```mermaid
flowchart LR
    A[💬 User Request] --> B[🎯 Extract Intent]
    B --> C[(🔎 Retrieve Products)]
    C --> D[🧹 Filter Products]
    D --> E[📊 Rank Products]
    E --> F[✍️ Generate Explanation]
    F --> G[📤 Return Recommendation]

    classDef core fill:#6C5CE7,stroke:#4834d4,color:#fff,font-weight:bold;
    class B,D,E,F core
```

The gap between these two diagrams **is the roadmap** — each new box is a future unit of work.

<br>

---

## 📊 Dataset Design

Core attributes the fashion dataset should expose, to make preprocessing straightforward later.

| Attribute | Notes |
|---|---|
| Product ID | Unique identifier |
| Category | Top-level grouping (e.g. tops, shoes) |
| Subcategory | Finer grouping (e.g. sneakers, boots) |
| Brand | — |
| Color | — |
| Season | Spring / Summer / Fall / Winter |
| Material | — |
| Gender | Target demographic |
| Usage | Casual / Formal / Sports / etc. |
| Price | — |
| Image Path | Local or remote reference |

<br>

---

## 🗺️ Future Modules

A living roadmap — check items off as they land, add new ones as they emerge.

- [ ] Wardrobe Manager
- [ ] Trend Analysis
- [ ] Weather API
- [ ] Shopping APIs
- [ ] Virtual Try-On
- [ ] Outfit Rating
- [ ] Multi-Agent Collaboration

<br>

---

## 🧾 Coding Standards

Boring until you're debugging at 2 a.m. — worth defining now.

- One responsibility per module
- Type hints where practical
- Meaningful function names
- Keep modules focused
- Write docstrings for public functions
- Avoid hard-coded values — use configuration files where appropriate

<br>

---

## ⚠️ Known Limitations

Transparency about what isn't built yet, so nobody (including future-you) assumes otherwise.

- No persistent memory *(yet)*
- Recommendations are not yet ranked using machine learning
- Computer vision is planned but not implemented
- Fashion knowledge currently depends on the integrated dataset and LLM reasoning

<br>

---

<div align="center">
<sub>This document evolves with Miranda — update it before the code drifts from the plan. 🧷</sub>
</div>
