package com.example.crypto.dto;

import lombok.Data;

@Data
public class CurrentMarketResponse {
    private String coinId;
    private String symbol;
    private String name;
    private Double currentPrice;
    private Double marketCap;
    private Double totalVolume;
    private Double priceChangePercentage24h;
    private String lastUpdated;
}
