import { http } from './http'
import type { OutlookResponse } from '../types/market'

export async function fetchOutlook(coinId: string, days: number) {
  const res = await http.post<OutlookResponse>(`/analysis/${coinId}/outlook?days=${days}`)
  return res.data
}
