type Props = {
  title: string
  value: string
  subText?: string
}

export default function MetricCard({ title, value, subText }: Props) {
  return (
    <div className="card">
      <div className="muted small">{title}</div>
      <div className="metric-value">{value}</div>
      {subText ? <div className="muted small spaced">{subText}</div> : null}
    </div>
  )
}
