package com.example.crypto.dto;

import lombok.Data;
import java.util.List;
import java.util.Map;

@Data
public class OutlookResponse {

    private String stance;

    private Double confidence;

    private String summary;

    private List<String> signals;

    private List<String> risks;

    private Map<String, Object> indicatorSnapshot;

    private List<AgentContribution> contributors;

    @Data
    public static class AgentContribution {
        private String agent;
        private String summary;
    }
}