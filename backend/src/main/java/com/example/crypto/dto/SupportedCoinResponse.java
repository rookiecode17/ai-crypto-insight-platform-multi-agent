package com.example.crypto.dto;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class SupportedCoinResponse {
    private String id;
    private String symbol;
    private String name;
}
