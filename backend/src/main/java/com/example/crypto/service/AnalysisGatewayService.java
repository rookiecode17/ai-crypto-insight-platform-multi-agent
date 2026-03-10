package com.example.crypto.service;

import com.example.crypto.dto.OutlookResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import java.time.Duration;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class AnalysisGatewayService {

    private final WebClient.Builder webClientBuilder;
    private final CacheService cacheService;

    @Value("${app.agent.base-url}")
    private String agentBaseUrl;

    public OutlookResponse getOutlook(String coinId, int days) {
        String cacheKey = "crypto:outlook:" + coinId + ":" + days;
        String cached = cacheService.get(cacheKey);
        if (cached != null && !cached.isBlank()) {
            try {
                return new com.fasterxml.jackson.databind.ObjectMapper().readValue(cached, OutlookResponse.class);
            } catch (Exception ignored) {
            }
        }

        OutlookResponse response = webClientBuilder.build()
                .post()
                .uri(agentBaseUrl + "/agent/outlook")
                .bodyValue(Map.of(
                        "coin_id", coinId,
                        "vs_currency", "usd",
                        "days", days
                ))
                .retrieve()
                .bodyToMono(new ParameterizedTypeReference<OutlookResponse>() {})
                .block();

        try {
            cacheService.set(cacheKey, new com.fasterxml.jackson.databind.ObjectMapper().writeValueAsString(response), Duration.ofSeconds(60));
        } catch (Exception ignored) {
        }
        return response;
    }
}
