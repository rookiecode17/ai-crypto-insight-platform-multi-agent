package com.example.crypto.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class OhlcPoint {
    private Long timestamp;
    private String timeLabel;
    private Double open;
    private Double high;
    private Double low;
    private Double close;
}
