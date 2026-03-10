from langgraph.graph import StateGraph, START, END
from app.state import MarketState
from app.skills.market_skill import get_current_market, get_history_market
from app.skills.ohlc_skill import get_ohlc
from app.skills.indicator_skill import calc_indicators
from app.skills.signal_skill import generate_signals
from app.skills.risk_skill import generate_risks
from app.agents.market_agent import analyze_market_context
from app.agents.signal_agent import analyze_signals
from app.agents.risk_agent import analyze_risks
from app.agents.summary_agent import synthesize_outlook


def fetch_current_market_node(state: MarketState):
    result = get_current_market(
        coin_id=state.get("coin_id", "bitcoin"),
        vs_currency=state.get("vs_currency", "usd"),
    )
    return {"current_market": result}


def fetch_history_market_node(state: MarketState):
    result = get_history_market(
        coin_id=state.get("coin_id", "bitcoin"),
        vs_currency=state.get("vs_currency", "usd"),
        days=state.get("days", 30),
    )
    return {"history": result}


def fetch_ohlc_node(state: MarketState):
    result = get_ohlc(
        coin_id=state.get("coin_id", "bitcoin"),
        vs_currency=state.get("vs_currency", "usd"),
        days=state.get("days", 30),
    )
    return {"ohlc": result}


def calc_indicators_node(state: MarketState):
    return {"indicators": calc_indicators(state["history"], state.get("ohlc", []))}


def heuristic_signal_node(state: MarketState):
    return {"signals": generate_signals(state["current_market"], state["indicators"])}


def heuristic_risk_node(state: MarketState):
    return {"risks": generate_risks(state["current_market"], state["indicators"])}


def market_agent_node(state: MarketState):
    return {
        "market_view": analyze_market_context(
            current_market=state["current_market"],
            history=state["history"],
            indicators=state["indicators"],
        )
    }


def signal_agent_node(state: MarketState):
    return {
        "signal_view": analyze_signals(
            current_market=state["current_market"],
            indicators=state["indicators"],
            heuristic_signals=state["signals"],
        )
    }


def risk_agent_node(state: MarketState):
    return {
        "risk_view": analyze_risks(
            current_market=state["current_market"],
            indicators=state["indicators"],
            heuristic_risks=state["risks"],
        )
    }


def supervisor_agent_node(state: MarketState):
    result = synthesize_outlook(
        coin_id=state.get("coin_id", "bitcoin"),
        current_market=state["current_market"],
        indicators=state["indicators"],
        market_view=state["market_view"],
        signal_view=state["signal_view"],
        risk_view=state["risk_view"],
    )
    return {
        "stance": result["stance"],
        "confidence": result["confidence"],
        "summary": result["summary"],
        "outlook": result,
    }


def build_graph():
    graph = StateGraph(MarketState)
    graph.add_node("fetch_current_market", fetch_current_market_node)
    graph.add_node("fetch_history_market", fetch_history_market_node)
    graph.add_node("fetch_ohlc", fetch_ohlc_node)
    graph.add_node("calc_indicators", calc_indicators_node)
    graph.add_node("heuristic_signal", heuristic_signal_node)
    graph.add_node("heuristic_risk", heuristic_risk_node)
    graph.add_node("market_agent", market_agent_node)
    graph.add_node("signal_agent", signal_agent_node)
    graph.add_node("risk_agent", risk_agent_node)
    graph.add_node("supervisor_agent", supervisor_agent_node)

    graph.add_edge(START, "fetch_current_market")
    graph.add_edge("fetch_current_market", "fetch_history_market")
    graph.add_edge("fetch_history_market", "fetch_ohlc")
    graph.add_edge("fetch_ohlc", "calc_indicators")
    graph.add_edge("calc_indicators", "heuristic_signal")
    graph.add_edge("heuristic_signal", "heuristic_risk")
    graph.add_edge("heuristic_risk", "market_agent")
    graph.add_edge("market_agent", "signal_agent")
    graph.add_edge("signal_agent", "risk_agent")
    graph.add_edge("risk_agent", "supervisor_agent")
    graph.add_edge("supervisor_agent", END)
    return graph.compile()
