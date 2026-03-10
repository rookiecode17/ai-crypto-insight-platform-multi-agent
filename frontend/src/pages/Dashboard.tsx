import { useEffect, useState } from 'react'
import { fetchSupportedCoins, fetchCurrentMarket, fetchHistory, fetchOhlc } from '../api/coinApi'
import { fetchOutlook } from '../api/analysisApi'
import MetricCard from '../components/MetricCard'
import CoinSelector from '../components/CoinSelector'
import TimeRangeSelector from '../components/TimeRangeSelector'
import PriceChart from '../components/PriceChart'
import VolumeChart from '../components/VolumeChart'
import OhlcChart from '../components/OhlcChart'
import OutlookPanel from '../components/OutlookPanel'
import type {
  CurrentMarketResponse,
  HistoryResponse,
  OhlcResponse,
  OutlookResponse,
  SupportedCoinResponse,
} from '../types/market'

export default function Dashboard() {
  const [coins, setCoins] = useState<SupportedCoinResponse[]>([])
  const [coinId, setCoinId] = useState('bitcoin')
  const [days, setDays] = useState(30)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [current, setCurrent] = useState<CurrentMarketResponse | null>(null)
  const [history, setHistory] = useState<HistoryResponse | null>(null)
  const [ohlc, setOhlc] = useState<OhlcResponse | null>(null)
  const [outlook, setOutlook] = useState<OutlookResponse | null>(null)

  useEffect(() => {
    void fetchSupportedCoins().then(setCoins).catch(() => undefined)
  }, [])

  useEffect(() => {
    void loadAll(coinId, days)
  }, [coinId, days])

  async function loadAll(selectedCoin: string, selectedDays: number) {
    setLoading(true)
    setError(null)
    try {
      const [currentRes, historyRes, ohlcRes, outlookRes] = await Promise.all([
        fetchCurrentMarket(selectedCoin),
        fetchHistory(selectedCoin, selectedDays),
        fetchOhlc(selectedCoin, selectedDays),
        fetchOutlook(selectedCoin, selectedDays),
      ])
      setCurrent(currentRes)
      setHistory(historyRes)
      setOhlc(ohlcRes)
      setOutlook(outlookRes)
    } catch (e) {
      console.error(e)
      setError('Failed to load market data. Check backend, agent service, Redis, and API key configuration.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <div className="container">
        <div className="header-row">
          <div>
            <h1>AI Crypto Insight Platform</h1>
            <p className="muted">React + Spring Boot + LangGraph + Redis + CoinGecko Demo API</p>
          </div>
          <div className="controls">
            <CoinSelector options={coins} value={coinId} onChange={setCoinId} />
            <TimeRangeSelector value={days} onChange={setDays} />
            <button onClick={() => void loadAll(coinId, days)}>Refresh Analysis</button>
          </div>
        </div>

        {loading ? <p className="muted">Loading...</p> : null}
        {error ? <div className="error-box">{error}</div> : null}

        <div className="grid metrics-grid">
          <MetricCard title="Current Price" value={current ? `$${current.currentPrice.toLocaleString()}` : '-'} />
          <MetricCard title="24h Volume" value={current ? `$${Math.round(current.totalVolume).toLocaleString()}` : '-'} />
          <MetricCard title="Market Cap" value={current ? `$${Math.round(current.marketCap).toLocaleString()}` : '-'} />
          <MetricCard
            title="24h Change"
            value={current ? `${current.priceChangePercentage24h.toFixed(2)}%` : '-'}
            subText={current?.lastUpdated}
          />
        </div>

        <div className="grid charts-grid">
          <PriceChart data={history?.points ?? []} />
          <VolumeChart data={history?.points ?? []} />
        </div>

        <div className="grid single-grid">
          <OhlcChart data={ohlc?.points ?? []} />
        </div>

        <div className="grid single-grid">
          <OutlookPanel data={outlook} />
        </div>
      </div>
    </div>
  )
}
