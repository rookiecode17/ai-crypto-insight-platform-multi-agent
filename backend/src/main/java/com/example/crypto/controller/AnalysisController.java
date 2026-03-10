package com.example.crypto.controller;

import com.example.crypto.dto.OutlookResponse;
import com.example.crypto.service.AnalysisGatewayService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/analysis")
@RequiredArgsConstructor
public class AnalysisController {

    private final AnalysisGatewayService analysisGatewayService;

    @PostMapping("/{id}/outlook")
    public OutlookResponse outlook(@PathVariable String id,
                                   @RequestParam(defaultValue = "30") int days) {
        return analysisGatewayService.getOutlook(id, days);
    }
}
