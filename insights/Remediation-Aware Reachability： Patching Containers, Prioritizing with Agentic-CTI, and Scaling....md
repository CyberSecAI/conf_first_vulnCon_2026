# Remediation-Aware Reachability： Patching Containers, Prioritizing with Agentic-CTI, and Scaling...

## Executive Summary
Francesco Beltramini (Phoenix Security) addresses the "AI apocalypse" in vulnerability management, emphasizing that defenders must move at the speed of attackers who are already using AI for "one-shot" exploits and malware generation. He argues that traditional scanning is too slow and lacks context. Instead, a mature program must leverage reachability analysis, attribution, and AI-powered intelligence (Agentic-CTI) to distinguish "paper tigers" from real production risks and automate remediation.

## Key Points
* **Accelerating Threat Landscape:** Vulnerabilities are increasing at a 25% year-on-year rate, with a projection of reaching 1 million total vulnerabilities well before 2030.
* **The "Vibe-Coded" Attack:** Attackers are using AI to generate malware and chain vulnerabilities in minutes (e.g., JetBrains exploitation took only 3 minutes from declaration).
* **AI-Generated Code:** While GitHub estimates 50% of codebases are AI-generated, the speaker believes it is closer to 80-90%, leading to a massive surge in potential software weaknesses.
* **Four Essential Questions:** A functional VM program must know: Who owns the asset? Where does the problem come from? Is it in a running container/system? Is it reachable?
* **Paper Tigers vs. Tier 1:** Many "Critical" vulnerabilities are "paper tigers" (no evidence of exploitation, unreachable). Tier 1 threats are those with confirmed evidence, acceleration, or ransomware usage.
* **The NVD Enrichment Gap:** Approximately 50% of key tactics and techniques used in real-world exploitations are absent from the National Vulnerability Database (NVD).
* **Package Manager Fragility:** The ecosystem is "on fire" with malware in NPM and other package managers (e.g., Shai-Hulud, Axios) that often never receive a traditional CVE.
* **Phoenix Blue Release:** An open-source threat intelligence platform designed to help defenders fight AI with AI by processing 2 million advisories hourly with "judge" LLMs.
* **Human-First AI:** AI should not replace humans but empower "human with AI" to replace "human without AI." Remediation should be automated via one-shot patching while humans focus on context.

## Notable Quotes
* "Finding problems is cheap. Finding more problems is cheaper."
* "AI is just a tool. Use a tool as a tool. Otherwise, you become the tool."
* "Human with AI will replace human without AI."
* "Only a percentage of [vulnerability data] is exploitable... what's important is the end part, the critical vulnerability in system that are running."

## Takeaways
* Implement reachability analysis to reduce noise and focus remediation efforts on vulnerabilities that are active and accessible in production.
* Integrate malware and package intelligence into your security program, as traditional CVE/NVD data is no longer sufficient for modern supply chain risks.
* Shift from reactive scanning to proactive prevention by using AI agents to block vulnerable packages from entering the pipeline and to automate the remediation of existing flaws.
