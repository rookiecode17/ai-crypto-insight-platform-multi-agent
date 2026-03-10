package com.example.crypto.util;

import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

public class TimeFormatUtil {

    private static final DateTimeFormatter FORMATTER =
            DateTimeFormatter.ofPattern("MM-dd HH:mm").withZone(ZoneId.systemDefault());

    private TimeFormatUtil() {
    }

    public static String formatMillis(Long millis) {
        return FORMATTER.format(Instant.ofEpochMilli(millis));
    }
}
