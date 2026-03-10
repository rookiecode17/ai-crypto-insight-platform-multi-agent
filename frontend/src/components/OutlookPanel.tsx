import type { OutlookResponse } from '../types/market'

type Props = {
  data: OutlookResponse | null
}

export default function OutlookPanel({ data }: Props) {
  return (
    <div className="card full-width">
      <h3>Multi-Agent AI Outlook</h3>
      {!data ? (
        <p className="muted">Loading analysis...</p>
      ) : (
        <>
          <div className="pill-row">
            <span className="pill">Stance: {data.stance}</span>
            <span className="pill">Confidence: {(data.confidence * 100).toFixed(0)}%</span>
            <span className="pill">Agents: {data.contributors?.length ?? 0} specialists + supervisor</span>
          </div>
          <p className="summary">{data.summary}</p>

          {data.contributors?.length ? (
            <>
              <h4>Agent Contributions</h4>
              <div className="two-col-text">
                {data.contributors.map((item, idx) => (
                  <div key={`${item.agent}-${idx}`} className="agent-card">
                    <strong>{item.agent}</strong>
                    <p className="muted">{item.summary}</p>
                  </div>
                ))}
              </div>
            </>
          ) : null}

          <div className="two-col-text">
            <div>
              <h4>Signals</h4>
              <ul>
                {data.signals.map((item, idx) => (
                  <li key={idx}>{item}</li>
                ))}
              </ul>
            </div>
            <div>
              <h4>Risks</h4>
              <ul>
                {data.risks.map((item, idx) => (
                  <li key={idx}>{item}</li>
                ))}
              </ul>
            </div>
          </div>
          <h4>Indicator Snapshot</h4>
          <pre className="json-block">{JSON.stringify(data.indicatorSnapshot, null, 2)}</pre>
          <p className="muted small">AI-generated market outlook from a multi-agent workflow. Not financial advice.</p>
        </>
      )}
    </div>
  )
}
