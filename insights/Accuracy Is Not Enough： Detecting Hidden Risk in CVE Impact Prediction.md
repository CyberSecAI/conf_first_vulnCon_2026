# Accuracy Is Not Enough: Detecting Hidden Risk in CVE Impact Prediction

## Executive Summary
Keerthana Purushotham (IEEE, US) argues that in vulnerability management, false negatives carry significantly higher risk than false positives, yet standard accuracy metrics often mask these critical failures. By introducing data science concepts like confusion matrices and the Matthews Correlation Coefficient (MCC), she proposes a more nuanced way to measure and visualize "trust" in security automations and AI models over time. This session explores how a deeper understanding of risk-weighted metrics can prevent undetected vulnerabilities from leaving organizations exposed.

## Key Points
- Vulnerability assessment is a dynamic process where a CVE's severity and impact can change as more information or exploitability data becomes available.
- Standard "accuracy" is a misleading metric in security; a system can maintain high accuracy while missing a single critical vulnerability that results in total compromise.
- False negatives represent undetected risks that leave customers exposed, whereas false positives lead to "erosion of trust" and unnecessary operational costs like forced system reboots and downtime.
- Organizations should utilize a "Confusion Matrix" (True Positives, True Negatives, False Positives, False Negatives) to evaluate the performance of their security models and triaging systems.
- The "Matthews Correlation Coefficient (MCC)" is recommended as a robust metric for building a "Trust Score" dashboard that handles imbalanced datasets common in vulnerability management.
- A "drift zone" is identified as the period between a CVE's initial announcement and the point where contradictory evidence (e.g., from ADPs or exploitation reports) reveals an assessment error.
- Modern vulnerability management should automate the monitoring of "disputed" statuses and conflicting reports between CNAs and ADPs to trigger immediate reconciliation.
- These predictive metrics are applicable to both data producers (CNAs) and consumers (security practitioners) to quantify and communicate the reliability of their security assessments.

## Notable Quotes
- "All of security that we have today is some form of prediction because security changes with day-to-day... a single CVE ID... could have a specific severity score XYZ and with time it could change."
- "In vulnerability management, you can say that false negatives have a higher risk impact than false positives... false negatives is like the missed vulnerabilities where you're blind to something you should be able to see."
- "You can have the same accuracy but your impact can be one and zero—very different."
- "Every time you reboot a system, that's an actual loss. So you do not want to announce too many false positives."
- "This [MCC] is going to essentially be your trust score. Every week you can evaluate trust... and see whether your trust score is improving or decreasing."

## Takeaways
- Shift performance metrics for vulnerability management from simple "accuracy" to risk-weighted metrics that penalize false negatives more heavily.
- Implement a rolling "Trust Score" using the Matthews Correlation Coefficient to monitor the reliability of automated triaging or AI-driven impact assessments.
- Monitor "ADP" (Authorized Data Provider) fields and "disputed" statuses in CVE records as high-priority triggers for re-evaluating internal vulnerability impact assessments.
- Visualize and measure the "drift zone"—the time between initial assessment and correction—to identify systematic weaknesses in the triage process.
