type Props = {
  value: number
  onChange: (value: number) => void
}

export default function TimeRangeSelector({ value, onChange }: Props) {
  return (
    <label className="control-group">
      <span className="muted small">Range</span>
      <select value={value} onChange={(e) => onChange(Number(e.target.value))}>
        <option value={7}>Last 7 days</option>
        <option value={30}>Last 30 days</option>
        <option value={90}>Last 90 days</option>
      </select>
    </label>
  )
}
