# Quantifying Swiss Cheese, the Bayesian Way

## Executive Summary
Steven (from Moderna and EPSS SIG) discusses a quantified vulnerability risk model based on Bayesian updating. He argues that traditional qualitative risk assessments lack defensibility and that we need to measure control effectiveness empirically—through breach and attack simulations—to understand if security actions actually make the organization safer. The talk moves from the base layer of vulnerability exploitation to material incident likelihood, providing an economically defensible framework for prioritization.

## Key Points
* **Systemic Failure:** Cybersecurity lacks strong economic incentives for safety; technology is used to enable business outcomes, but its inherent safety is often unmeasured.
* **The Denominator Problem:** Organizations often count "successes" (e.g., blocked exploits) but lack a denominator for "failures" (undetected exploits), leading to the "Missing Not At Random" (MNAR) problem in statistics.
* **Qualitative vs. Quantitative:** The "Swiss Cheese" model of defense-in-depth is often used qualitatively without knowing the actual "size of the holes" in each layer of control.
* **Bayesian Updating:** Control effectiveness can be quantified using beta distributions. Starting with a "prior" (expert opinion), the model is updated with "posteriors" from empirical tests like Breach and Attack Simulation (BAS).
* **Subject Matter Expert Calibration:** Since expert opinions are biased, the model uses P50 (median) and P90 (high confidence) guesses to reverse-engineer beta distributions and quantify uncertainty.
* **Group EPSS at Asset Layer:** By taking the complement product of EPSS scores for all CVEs on an asset, organizations can calculate the probability that at least one vulnerability on that asset will be exploited within 30 days.
* **EVIL Model:** The "Exploit Vector Incident Loss" model maps components and vectors to control failure rates, bridging technical vulnerability data to material business risk exposure.
* **Patch Cadence Value:** Simulations demonstrate that broad, automated patch cadence is often significantly more valuable in reducing aggregate risk than focusing on a few high-EPSS one-off vulnerabilities.
* **Aggregate Hazard:** Moderate per-asset risk multiplied across thousands of assets often dominates the total risk profile of an environment more than a single critical outlier.

## Notable Quotes
* "I have no idea if that's actually making us safer. Can we validate that?"
* "Just because those assumptions have to be made and they're hard to quantify or hard to measure doesn't mean we shouldn't try."
* "All models are wrong, but some are useful. The question actually is: is this model less wrong than what you're doing right now?"
* "Moderate per asset risk multiplied across thousands of assets dominates the aggregate hazard of your environment."

## Takeaways
* Move from qualitative "High/Medium/Low" labels to quantitative risk models using Bayesian methods to provide a more defensible security posture.
* Prioritize automated, broad patch cadence as it provides a higher economic return on risk reduction compared to manual triaging of individual vulnerabilities.
* Use Breach and Attack Simulation (BAS) or red teaming to create a "denominator" for control effectiveness, allowing for empirical measurement of security tools.
