import {
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts'
import type { OhlcPoint } from '../types/market'

type Props = { data: OhlcPoint[] }

export default function OhlcChart({ data }: Props) {
  return (
    <div className="card chart-card full-width">
      <h3>OHLC Snapshot</h3>
      <ResponsiveContainer width="100%" height={320}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timeLabel" minTickGap={28} />
          <YAxis domain={["auto", "auto"]} />
          <Tooltip />
          <Line type="monotone" dataKey="open" dot={false} strokeWidth={1.5} />
          <Line type="monotone" dataKey="high" dot={false} strokeWidth={1.5} />
          <Line type="monotone" dataKey="low" dot={false} strokeWidth={1.5} />
          <Line type="monotone" dataKey="close" dot={false} strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
