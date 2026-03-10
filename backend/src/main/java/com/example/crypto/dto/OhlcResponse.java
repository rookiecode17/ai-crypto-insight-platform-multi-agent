package com.example.crypto.dto;

import lombok.Data;

import java.util.List;

@Data
public class OhlcResponse {
    private String coinId;
    private Integer days;
    private List<OhlcPoint> points;
}
