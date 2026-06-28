<div align="center">
  <img width="415" height="447" alt="output" src="https://github.com/user-attachments/assets/8a8510eb-531d-44c2-bee5-ef2031b98916" />
  <h1>Autonomous Deep Research Agent</h1>
  <p><i>A multi-stage AI research assistant built with LangGraph, RAG, and the Model Context Protocol (MCP).</i></p>
</div>

---

## Overview

This repository contains a production-grade Autonomous AI Research Agent. Given a broad research topic, the agent dynamically plans search queries, orchestrates live web retrieval using a custom MCP server, grounds its knowledge using a vector database (ChromaDB), and synthesizes comprehensive multi-page technical reports in Markdown format.

## Architecture

The system is built on four core technical pillars:

1. **LangGraph (Multi-Agent State Machine)**
   - The agent operates in a cyclical execution graph comprising planning, retrieval, validation, and generation nodes.
   - **Stateful Checkpointing:** Utilizes `MemorySaver` to track `thread_ids`, allowing the agent to maintain long-term memory and conversational context across continuous sessions.

2. **Model Context Protocol (MCP)**
   - Includes a custom-built Python MCP Server (`duckduckgo_mcp_server.py`) that securely exposes web-search tools.
   - Decouples external tool execution from the core reasoning loop, demonstrating modern, scalable tool integration without hardcoded API dependencies.

3. **Retrieval-Augmented Generation (RAG)**
   - Search results are vectorized and stored in **ChromaDB**.
   - The generation node queries the vector store to ground the LLM's final output in verifiable sources, effectively eliminating hallucinations and unsupported claims.

4. **Structured Generation**
   - Forces the LLM to output structured data schemas for predictable pipeline parsing and robust section writing.

## 📁 Repository Structure

- `reports/`: The destination directory where the agent automatically persists finalized Markdown research reports.

* `src/deep_research_advanced.ipynb`: The primary executable graph (includes the injected `%%writefile` block for the MCP server).

- `uv.lock` & `pyproject.toml`: Dependency resolution handled natively by `uv`.

## ⚙️ How to Run

1. Clone this repository.
2. create a .env file and add OPENAI_API_KEY="your-key" to it.
3. Install dependencies using `uv`:

   ```bash
   uv sync
   ```

4. Open `src/deep_research_advanced.ipynb` in a Jupyter environment.
5. Run all cells. The first cell will automatically generate the required MCP Server file, and the execution graph will launch in the background to fulfill your research topic.
