package com.example.crypto.dto;

import lombok.Data;

import java.util.List;

@Data
public class HistoryResponse {
    private String coinId;
    private String vsCurrency;
    private Integer days;
    private List<ChartPoint> points;
}
