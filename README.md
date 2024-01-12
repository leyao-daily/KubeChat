# KubeChat
## Overview:

The KubeChat is designed to provide an efficient, scalable, and secure environment for generating AI-powered content. The system integrates several services and components that work together to process and manage user inputs, contextual embeddings, and AI-generated responses.

## Architecture:

1. **User Interface (UI):** The front-end interface through which users interact with the system. It is responsible for capturing user inputs and displaying the generated content.
2. **Input Handler (IH):** Acts as the central coordinator within the system, processing user inputs, managing data flow between components, and updating contexts based on historical data.
3. **Memory Manager (MM):** Stores and manages user inputs and contexts. It queries the Vector DB to retrieve related historical data to help generate relevant and contextual responses.
4. **Embedding Services:**
   - **Embedding Queue (EQ):** Prioritizes and manages embedding generation requests to ensure efficient processing.
   - **Embedding Service (EM):** Generates embeddings for the input data and retrieves related embeddings from the Vector DB. These embeddings help in understanding and matching the context of the user's input.
5. **Prompt Service (PS):** Manages and retrieves structured prompt templates from the database, which guide the AI in generating coherent and contextually relevant content.
6. **Large Language Model (LLM) Services:**
   - **LLM Queue (LQM):** Manages the processing queue for the LLM service, ensuring that each request is handled efficiently.
   - **LLM Service (LLM):** The core AI component that generates responses based on the given context and prompt templates.
7. **Databases:**
   - **Vector DB (VDB):** A specialized database designed to handle and retrieve vector embeddings. It supports efficient similarity searches to find related historical data.
   - **Database (DB):** A traditional database that stores and manages prompt templates and other necessary data.

## Design Principles:

1. **Scalability:** Designed to handle an increasing load of user inputs and embedding generation requests without degradation in performance. This is achieved through efficient queuing systems and scalable architecture.
2. **Efficiency:** The system ensures prompt processing of inputs through optimized data flow, effective management of queues, and parallel processing where feasible.
3. **Accuracy and Relevance:** By leveraging historical data and contextual embeddings, the system ensures that the AI-generated content is accurate and contextually relevant.
4. **Security and Privacy:** Emphasizes protecting user data and generated content. The system can be integrated with secure storage solutions and encryption mechanisms to ensure data privacy.
5. **Modularity:** The system's architecture is modular, allowing for independent scaling and upgrading of each component as needed. This also facilitates easier maintenance and potential integration with other systems or services.
6. **Performance Monitoring:** Incorporates comprehensive logging and monitoring to track performance metrics, system health, and other critical indicators. This helps in proactive maintenance and performance optimization.

## Deploy

```bash
pip3 -r requirements.txt

python3 src/prompt.py
python3 src/embedding.py
python3 src/llm.py

# Locate the file you want to the root of the project.
python3 src/flow.py

# input pdf filename -> input template2 -> wait for embedding -> input question
```

## Contributor

<!-- readme: contributors -start -->

<!-- readme: contributors -end -->

