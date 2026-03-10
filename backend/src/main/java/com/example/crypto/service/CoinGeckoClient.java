package com.example.crypto.service;

import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

@Service
@RequiredArgsConstructor
public class CoinGeckoClient {

    private final WebClient.Builder webClientBuilder;

    @Value("${app.coingecko.base-url}")
    private String baseUrl;

    @Value("${app.coingecko.demo-api-key:}")
    private String demoApiKey;

    public String getCurrentMarket(String coinId) {
        WebClient.RequestHeadersSpec<?> spec = webClientBuilder.build()
                .get()
                .uri(baseUrl + "/coins/markets?vs_currency=usd&ids=" + coinId);
        if (!demoApiKey.isBlank()) {
            spec = spec.header("x-cg-demo-api-key", demoApiKey);
        }
        return spec.retrieve().bodyToMono(String.class).block();
    }

    public String getHistory(String coinId, int days) {
        WebClient.RequestHeadersSpec<?> spec = webClientBuilder.build()
                .get()
                .uri(baseUrl + "/coins/" + coinId + "/market_chart?vs_currency=usd&days=" + days);
        if (!demoApiKey.isBlank()) {
            spec = spec.header("x-cg-demo-api-key", demoApiKey);
        }
        return spec.retrieve().bodyToMono(String.class).block();
    }

    public String getOhlc(String coinId, int days) {
        WebClient.RequestHeadersSpec<?> spec = webClientBuilder.build()
                .get()
                .uri(baseUrl + "/coins/" + coinId + "/ohlc?vs_currency=usd&days=" + days);
        if (!demoApiKey.isBlank()) {
            spec = spec.header("x-cg-demo-api-key", demoApiKey);
        }
        return spec.retrieve().bodyToMono(String.class).block();
    }
}
