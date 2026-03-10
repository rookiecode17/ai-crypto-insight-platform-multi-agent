import type { SupportedCoinResponse } from '../types/market'

type Props = {
  options: SupportedCoinResponse[]
  value: string
  onChange: (value: string) => void
}

export default function CoinSelector({ options, value, onChange }: Props) {
  return (
    <label className="control-group">
      <span className="muted small">Coin</span>
      <select value={value} onChange={(e) => onChange(e.target.value)}>
        {options.map((coin) => (
          <option key={coin.id} value={coin.id}>
            {coin.name} ({coin.symbol})
          </option>
        ))}
      </select>
    </label>
  )
}
