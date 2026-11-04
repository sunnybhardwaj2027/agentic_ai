# 8-Week Agentic AI Plan

Goal: go from LLM basics to one deployed multi-agent project, with evaluation to prove it works. LLD/HLD and SQL are tracked separately.

**Rule for the final project:** build the single-agent version first and measure it, then split into multiple agents and compare quality, latency and cost. If multi-agent is not better on some metric, say so.

## Week 1: Python for AI + LLM fundamentals
**Goal:** write production-style Python and talk to an LLM API reliably.
- **Learn:** type hints, dataclasses, venv, error handling; asyncio; Pydantic; FastAPI; pytest; tokens, context windows, temperature; message roles; prompting; structured outputs; function/tool calling; embeddings; Transformers (high level)
- **Build:** app that sends a prompt and returns validated JSON with retry on bad output; add one tool call
- **Done when:** malformed model output is rejected and retried; 3+ pytest tests pass

## Week 2: RAG done properly
**Goal:** PDF Q&A app with measured retrieval quality.
- **Learn:** loading and chunking trade-offs; embeddings and vector DB (Chroma or FAISS); top-k, metadata filtering; hybrid search (BM25 + embeddings) and reranking; short- vs long-term memory; citing sources
- **Build:** PDF Q&A with page citations behind FastAPI; eval set of 20 questions; compare two chunk sizes
- **Done when:** you can show chunk size vs hit-rate on your own eval set

## Week 3: Agents from scratch + tools
**Goal:** understand the agent loop before using a framework.
- **Learn:** agent vs workflow, tool vs agent, LLM call vs agentic system; ReAct and planning; tool schemas and execution; autonomous vs deterministic workflows; web search API; MCP
- **Build:** research agent in plain Python with 3+ tools and a step/cost limit; one small MCP server
- **Done when:** agent finishes a research query end to end and stops safely at its limit

## Week 4: LangGraph + tracing
**Goal:** rebuild the agent as a graph with state, branching and human approval.
- **Learn:** LangChain essentials; LangGraph state, nodes, edges, conditional edges; checkpointing; human-in-the-loop; tracing (LangSmith or Langfuse)
- **Build:** port the Week 3 agent; add a conditional branch; add human approval before a sensitive action; debug one failed run from its trace
- **Done when:** you can explain what LangGraph gave you that your plain loop did not

## Week 5: Evaluation, safety and reliability
**Goal:** make the single agent measurable and safe. This is your baseline.
- **Learn:** eval design; LLM-as-judge and its biases; tool-call correctness; prompt injection and guardrails; cost and token budgets, timeouts, rate limits; retries and fallbacks
- **Build:** eval set of 15-20 queries; baseline for quality, latency and cost; injection test and defence
- **Done when:** you have a saved baseline table to compare against in Week 7

## Week 6: Multi-agent design and build
**Goal:** split into specialist agents only where it plausibly helps.
- **Learn:** supervisor, hierarchical, collaborative, sequential patterns; parallel execution and delegation; shared state vs independent memory; agent communication; when a single agent is enough
- **Build:** supervisor; Research, Analysis and Fact-check agents; report generator; parallel steps where possible
- **Done when:** one query runs through all agents and produces a final report

## Week 7: Harden and compare
**Goal:** make it robust, then prove (or disprove) that multi-agent is worth it.
- **Learn:** failure handling and retries per agent; streaming and status updates; persistent storage and memory
- **Build:** streaming status; tool-call logs and run history; re-run Week 5 evals; write a single vs multi-agent comparison
- **Done when:** a comparison table with an honest conclusion

## Week 8: Ship and interview prep
**Goal:** deployed project, clean repo, clear answers.
- **Learn:** Docker and secrets; cloud basics (Azure or AWS); other frameworks (OpenAI Agents SDK, CrewAI, Claude Agent SDK); Hugging Face Agents Course (skim)
- **Build:** Dockerize and deploy with a live link; README with architecture diagram, sample runs and eval results; 2-minute demo; written answers to the interview questions in `interview-qa.md`
- **Done when:** you can demo the project and defend every design choice in 10 minutes