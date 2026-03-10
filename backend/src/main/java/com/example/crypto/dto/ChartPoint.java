package com.example.crypto.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ChartPoint {
    private Long timestamp;
    private String timeLabel;
    private Double price;
    private Double volume;
}
