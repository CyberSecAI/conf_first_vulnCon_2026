# Diving into the CVSS Base Score Metrics - An Exploratory Analysis Bridging Product Security Assessments and Real-World Attacks
## Executive Summary
Kohei Taguchi (Panasonic Holdings Corporation, JP), Takayuki Uchiyama (Panasonic Holdings Corporation, JP), and Yuichi Kikuchi (Panasonic Holdings Corporation, JP) present a comparative analysis of CVSS "Medium" vulnerabilities in IoT products, illustrating how moderate scores can mask significant risks within attack chains. By combining global honeypot data with internal security testing results, the study identifies high-risk "Medium" vulnerabilities that serve as critical entry points for attackers. The session emphasizes that remediation priorities should be dictated by organizational context and the "attack scenario line"—viewing vulnerabilities as a sequence of events—rather than relying solely on the base score.

## Key Points
- Vulnerabilities rated as "Medium" (CVSS 4.0-6.9) are frequently deprioritized, yet they often provide the "initial access" or "foothold" required for more severe attacks.
- The study analyzed 424 IoT vulnerabilities, focusing on those requiring no privileges and no user interaction but possessing limited individual impact.
- Honeypot data confirms that real-world attackers actively exploit "Medium" information exposure vulnerabilities (CWE-200) to gather intelligence for later stages.
- A gap exists between security testing and honeypot findings: testing uncovers "root cause" design flaws, while honeypots reveal "technical impact" exploitation (e.g., injection, path traversal).
- In OT/factory environments, vulnerabilities affecting Availability (DoS) are as critical as "High" severity bugs because they can directly stop production lines.
- Attackers appear to favor exploiting input processing flaws over direct authentication bypasses, as authentication-related weaknesses only accounted for 12% of observed attacks.
- Effective risk management requires viewing vulnerabilities as a "line" (a sequence of events) rather than a "point" (a single score).
- Remediation should be prioritized based on the benefits an attacker gains, such as using leaked configuration data to facilitate a complete device takeover.

## Notable Quotes
- "Leaving medium-level vulnerabilities unaddressed can create a risk of devices falling under attacker's control."
- "Honeypots show what attackers do, while testing provide data showing how fast those attackers can succeed and what happens."
- "We should view vulnerabilities not as individual points, but as a line in the form of attack scenarios."

## Takeaways
- Re-evaluate "Medium" rated vulnerabilities in your environment to determine if they can serve as a catalyst for chained attacks.
- Adjust remediation priorities based on the product's usage environment (e.g., prioritize Availability in industrial settings vs. Confidentiality in IP cameras).
- Use CWE as a common language to bridge the gap between internal design testing and external threat intelligence.
- Implement strong basic controls, such as password hardening, for vulnerabilities that require general user privileges to mitigate lateral movement.
