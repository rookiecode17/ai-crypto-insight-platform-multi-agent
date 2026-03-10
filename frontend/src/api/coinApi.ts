import { http } from './http'
import type {
  CurrentMarketResponse,
  HistoryResponse,
  OhlcResponse,
  SupportedCoinResponse,
} from '../types/market'

export async function fetchSupportedCoins() {
  const res = await http.get<SupportedCoinResponse[]>('/coins/supported')
  return res.data
}

export async function fetchCurrentMarket(coinId: string) {
  const res = await http.get<CurrentMarketResponse>(`/coins/${coinId}/current`)
  return res.data
}

export async function fetchHistory(coinId: string, days: number) {
  const res = await http.get<HistoryResponse>(`/coins/${coinId}/history?days=${days}`)
  return res.data
}

export async function fetchOhlc(coinId: string, days: number) {
  const res = await http.get<OhlcResponse>(`/coins/${coinId}/ohlc?days=${days}`)
  return res.data
}
