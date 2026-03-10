package com.example.crypto.controller;

import com.example.crypto.dto.CurrentMarketResponse;
import com.example.crypto.dto.HistoryResponse;
import com.example.crypto.dto.OhlcResponse;
import com.example.crypto.dto.SupportedCoinResponse;
import com.example.crypto.service.CoinMarketService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/coins")
@RequiredArgsConstructor
public class CoinController {

    private final CoinMarketService coinMarketService;

    @GetMapping("/supported")
    public List<SupportedCoinResponse> supported() {
        return coinMarketService.getSupportedCoins();
    }

    @GetMapping("/{id}/current")
    public CurrentMarketResponse current(@PathVariable String id) {
        return coinMarketService.getCurrentMarket(id);
    }

    @GetMapping("/{id}/history")
    public HistoryResponse history(@PathVariable String id,
                                   @RequestParam(defaultValue = "30") int days) {
        return coinMarketService.getHistory(id, days);
    }

    @GetMapping("/{id}/ohlc")
    public OhlcResponse ohlc(@PathVariable String id,
                             @RequestParam(defaultValue = "30") int days) {
        return coinMarketService.getOhlc(id, days);
    }
}
