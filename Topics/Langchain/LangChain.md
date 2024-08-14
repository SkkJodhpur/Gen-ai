# Langchain
LangChain framework, which is designed for building applications using large language models (LLMs). Here's a summarized conceptual guide to these components:

![alt text](image.png)

### 1. **Architecture Overview:**
   - **LangChain as a Framework:** LangChain is composed of several packages that each serve different purposes in the application development process. These packages are categorized based on their functions and the level of integration they offer.

### 2. **Core Packages:**
   - **langchain-core:**
     - **Purpose:** This is the foundational package of LangChain, containing the core abstractions and interfaces for components such as LLMs, vector stores, and retrievers.
     - **Characteristics:** It does not include any third-party integrations and maintains minimal dependencies to remain lightweight and flexible.

   - **langchain:**
     - **Purpose:** The main package where chains, agents, and retrieval strategies are defined.
     - **Characteristics:** These components are generic and not tied to any specific third-party integrations, providing a cognitive architecture for applications.

### 3. **Partner and Community Packages:**
   - **Partner Packages:**
     - **Purpose:** Popular third-party integrations (e.g., OpenAI, Anthropic) are split into their own packages, enhancing support for these integrations.
     - **Characteristics:** These are distinct from community contributions and are critical for working with major partners.

   - **langchain-community:**
     - **Purpose:** This package houses a wide range of third-party integrations contributed by the LangChain community.
     - **Characteristics:** The dependencies here are kept optional to maintain the package's lightweight nature.

### 4. **Extended Capabilities:**
   - **langgraph:**
     - **Purpose:** An extension of LangChain, designed to model and build stateful multi-actor applications using LLMs, organized in a graph structure.
     - **Characteristics:** It provides high-level interfaces for creating agents and a low-level API for custom workflows.

   - **langserve:**
     - **Purpose:** A package focused on deploying LangChain chains as REST APIs, simplifying the process of making production-ready APIs.

   - **LangSmith:**
     - **Purpose:** A developer platform aimed at debugging, testing, evaluating, and monitoring LLM applications.

This guide gives a high-level understanding of the different components in LangChain, which can help you choose the right tools and packages for building and deploying AI applications using LLMs.