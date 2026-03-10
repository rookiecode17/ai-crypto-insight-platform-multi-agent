# AI Crypto Insight Platform (Multi Agent Edition)

A full-stack crypto market analysis project built with React, Spring Boot, Redis, FastAPI, and LangGraph.

## What changed in this version

This edition upgrades the AI layer from a single-agent workflow to a **multi agent system**:

- **Market Agent**: interprets current and historical market context
- **Signal Agent**: refines bullish/bearish/neutral signals
- **Risk Agent**: analyzes downside and reversal risks
- **Supervisor Agent**: synthesizes specialist outputs into the final structured outlook

The LangGraph workflow still fetches market data and computes indicators first, then routes that state through multiple specialized agents.

## Stack

- Frontend: React + Vite + Recharts
- Backend: Spring Boot 3 + WebClient + Redis
- AI Service: FastAPI + LangGraph + LangChain OpenAI
- Data: CoinGecko Demo API

## Features

- Multi-coin support: BTC, ETH, SOL
- Current market metrics
- Historical price/volume charts (7/30/90 days)
- OHLC visualization
- Multi-agent AI outlook with:
  - stance
  - confidence
  - signals
  - risks
  - indicator snapshot
  - specialist agent contributions
- Redis caching for market data and AI outputs

## Project structure

```text
ai-crypto-insight-platform/
├── frontend/
├── backend/
├── agent-service/
└── docker-compose.yml
```

## Environment variables

### agent-service/.env

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4.1-mini
COINGECKO_DEMO_API_KEY=your_coingecko_demo_key
```

### backend

The backend reads these from your shell:

```env
COINGECKO_DEMO_API_KEY=your_coingecko_demo_key
AGENT_BASE_URL=http://localhost:8001
REDIS_HOST=localhost
REDIS_PORT=6379
```

## Run locally

### 1. Start Redis

```bash
docker compose up -d
```

### 2. Start the AI service

```bash
cd agent-service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8001
```

### 3. Start the Spring Boot backend

```bash
cd backend
./mvnw spring-boot:run
```

If you do not have the wrapper:

```bash
mvn spring-boot:run
```

### 4. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

## Multi agent workflow

```text
START
  -> fetch_current_market
  -> fetch_history_market
  -> fetch_ohlc
  -> calc_indicators
  -> heuristic_signal
  -> heuristic_risk
  -> market_agent
  -> signal_agent
  -> risk_agent
  -> supervisor_agent
  -> END
```

## Key Features

- Built a **multi agent crypto market analysis platform** using LangGraph to orchestrate specialized Market, Signal, Risk, and Supervisor agents for structured reasoning over market data.

- Implemented a **FastAPI based AI service** to expose reusable agent workflows and structured LLM outputs including stance, confidence scores, signals, and risk factors.

- Introduced **Redis caching** for market datasets and AI outputs to reduce repeated third-party API calls and improve response latency.
