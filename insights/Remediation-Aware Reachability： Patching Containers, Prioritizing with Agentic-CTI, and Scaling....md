# Remediation-Aware Reachability: Patching Containers, Prioritizing with Agentic-CTI, and Scaling Fixes from Code to Cloud

## Executive Summary
Francesco Cipollone (Phoenix Security, GB) argues that traditional vulnerability scanning is too slow and lacks the context necessary for modern threats. He proposes that a mature security program must leverage reachability analysis, precise attribution, and AI-powered intelligence (Agentic-CTI) to distinguish "paper tigers" from genuine production risks. By automating remediation and focusing on vulnerabilities with confirmed evidence of exploitation, organizations can scale their defenses from code to cloud while keeping pace with an accelerating threat landscape.

## Key Points
* **Accelerating Threat Landscape:** Vulnerabilities are increasing at a 25% year-on-year rate, with a projection of reaching 1 million total vulnerabilities well before 2030.
* **The "Vibe-Coded" Attack:** Attackers are using AI to generate malware and chain vulnerabilities in minutes (e.g., JetBrains exploitation took only 3 minutes from declaration).
* **AI-Generated Code:** While GitHub estimates 50% of codebases are AI-generated, the speaker Francesco Cipollone (Phoenix Security, GB).
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
