export interface SupportedCoinResponse {
  id: string
  symbol: string
  name: string
}

export interface CurrentMarketResponse {
  coinId: string
  symbol: string
  name: string
  currentPrice: number
  marketCap: number
  totalVolume: number
  priceChangePercentage24h: number
  lastUpdated: string
}

export interface ChartPoint {
  timestamp: number
  timeLabel: string
  price: number
  volume: number
}

export interface HistoryResponse {
  coinId: string
  vsCurrency: string
  days: number
  points: ChartPoint[]
}

export interface OhlcPoint {
  timestamp: number
  timeLabel: string
  open: number
  high: number
  low: number
  close: number
}

export interface OhlcResponse {
  coinId: string
  days: number
  points: OhlcPoint[]
}

export interface AgentContribution {
  agent: string
  summary: string
}

export interface OutlookResponse {
  stance: string
  confidence: number
  summary: string
  signals: string[]
  risks: string[]
  indicatorSnapshot: Record<string, number | string>
  contributors: AgentContribution[]
}
