package com.example.crypto.service;

import com.example.crypto.dto.*;
import com.example.crypto.util.TimeFormatUtil;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class CoinMarketService {

    private final CoinGeckoClient coinGeckoClient;
    private final CacheService cacheService;
    private final ObjectMapper objectMapper = new ObjectMapper();

    public List<SupportedCoinResponse> getSupportedCoins() {
        return List.of(
                new SupportedCoinResponse("bitcoin", "BTC", "Bitcoin"),
                new SupportedCoinResponse("ethereum", "ETH", "Ethereum"),
                new SupportedCoinResponse("solana", "SOL", "Solana")
        );
    }

    public CurrentMarketResponse getCurrentMarket(String coinId) {
        String cacheKey = "crypto:current:" + coinId;
        String json = getOrLoad(cacheKey, Duration.ofSeconds(30), () -> coinGeckoClient.getCurrentMarket(coinId));
        try {
            JsonNode root = objectMapper.readTree(json);
            JsonNode node = root.get(0);
            CurrentMarketResponse response = new CurrentMarketResponse();
            response.setCoinId(node.path("id").asText());
            response.setSymbol(node.path("symbol").asText().toUpperCase());
            response.setName(node.path("name").asText());
            response.setCurrentPrice(node.path("current_price").asDouble());
            response.setMarketCap(node.path("market_cap").asDouble());
            response.setTotalVolume(node.path("total_volume").asDouble());
            response.setPriceChangePercentage24h(node.path("price_change_percentage_24h").asDouble());
            response.setLastUpdated(node.path("last_updated").asText());
            return response;
        } catch (Exception e) {
            throw new RuntimeException("Failed to parse current market response", e);
        }
    }

    public HistoryResponse getHistory(String coinId, int days) {
        String cacheKey = "crypto:history:" + coinId + ":" + days;
        String json = getOrLoad(cacheKey, Duration.ofMinutes(5), () -> coinGeckoClient.getHistory(coinId, days));
        try {
            JsonNode root = objectMapper.readTree(json);
            JsonNode prices = root.path("prices");
            JsonNode volumes = root.path("total_volumes");
            int size = Math.min(prices.size(), volumes.size());
            List<ChartPoint> points = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                long ts = prices.get(i).get(0).asLong();
                double price = prices.get(i).get(1).asDouble();
                double volume = volumes.get(i).get(1).asDouble();
                points.add(new ChartPoint(ts, TimeFormatUtil.formatMillis(ts), price, volume));
            }
            HistoryResponse response = new HistoryResponse();
            response.setCoinId(coinId);
            response.setVsCurrency("usd");
            response.setDays(days);
            response.setPoints(points);
            return response;
        } catch (Exception e) {
            throw new RuntimeException("Failed to parse history response", e);
        }
    }

    public OhlcResponse getOhlc(String coinId, int days) {
        String cacheKey = "crypto:ohlc:" + coinId + ":" + days;
        String json = getOrLoad(cacheKey, Duration.ofMinutes(5), () -> coinGeckoClient.getOhlc(coinId, days));
        try {
            JsonNode root = objectMapper.readTree(json);
            List<OhlcPoint> points = new ArrayList<>();
            for (JsonNode item : root) {
                long ts = item.get(0).asLong();
                points.add(new OhlcPoint(
                        ts,
                        TimeFormatUtil.formatMillis(ts),
                        item.get(1).asDouble(),
                        item.get(2).asDouble(),
                        item.get(3).asDouble(),
                        item.get(4).asDouble()
                ));
            }
            OhlcResponse response = new OhlcResponse();
            response.setCoinId(coinId);
            response.setDays(days);
            response.setPoints(points);
            return response;
        } catch (Exception e) {
            throw new RuntimeException("Failed to parse OHLC response", e);
        }
    }

    private String getOrLoad(String key, Duration ttl, Loader loader) {
        String cached = cacheService.get(key);
        if (cached != null && !cached.isBlank()) {
            return cached;
        }
        String value = loader.load();
        cacheService.set(key, value, ttl);
        return value;
    }

    @FunctionalInterface
    private interface Loader {
        String load();
    }
}
