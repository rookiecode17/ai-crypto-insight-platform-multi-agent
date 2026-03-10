import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts'
import type { ChartPoint } from '../types/market'

type Props = { data: ChartPoint[] }

export default function VolumeChart({ data }: Props) {
  return (
    <div className="card chart-card">
      <h3>Trading Volume</h3>
      <ResponsiveContainer width="100%" height={320}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timeLabel" minTickGap={28} />
          <YAxis />
          <Tooltip />
          <Bar dataKey="volume" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
