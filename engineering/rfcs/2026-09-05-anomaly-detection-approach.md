# RFC - Anomaly detection approach (2026-09-05)
**Author:** Robin Park (AI). **Status:** accepted.
**Problem:** threshold alerts miss slow drifts and seasonal spikes.
**Approach:** per-metric baseline (rolling median + MAD) with a seasonality adjustment; start simple, no heavy ML.
**Why not ML v1:** cost + explainability; a transparent statistical baseline is defensible to customers.
**Risks:** noisy metrics -> alert fatigue; mitigate with a per-alert sensitivity setting.
**Owner:** Robin; feeds smart-alerts (TL-008).
