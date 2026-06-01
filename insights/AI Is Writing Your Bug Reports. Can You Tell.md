# AI Is Writing Your Bug Reports. Can You Tell?

## Executive Summary
Khushali Dalal (VulnCheck, US) addresses the surge of AI-generated and AI-assisted vulnerability reports in bug bounty programs and PSIRT queues, highlighting the growing gap between the rapid AI-driven influx of reports and the finite capacity of human triage teams. Rather than advocating for AI bans, she focuses on training triagers to distinguish between "polished writing" and "well-substantiated evidence." The session provides a strategic framework to prioritize signal over noise in an era where some organizations have seen over a 200% increase in report volume.

## Key Points
- The "AI reporting crisis" of late 2025/early 2026 is driven by three factors: massive volume, high linguistic fluency that mimics senior researchers, and a psychological bias where humans mistake confidence for importance.
- A critical operational risk is "wrong triage"—where highly polished, urgent-sounding AI reports distract security teams from real, less-polished vulnerabilities.
- Real-world consequences are already manifesting; notably, the Curl project suspended its public bug bounty program in early 2026 because the signal-to-noise ratio had collapsed.
- Purely AI-generated reports often exhibit "technical hallucinations," such as internal contradictions (e.g., claiming unauthenticated access in the description while the PoC requires admin privileges).
- The most insidious pattern is "human-found, AI-packaged," where a genuine but minor bug is wrapped in an AI-inflated narrative about a catastrophic "full environment takeover" that isn't supported by the evidence.
- High-signal, human-written reports are often "low polish" and may even start tentatively (e.g., "Maybe this is a bug"), but provide specific endpoints, versions, and concrete reproduction steps.
- Security teams should adopt the "PAUSE" mnemonic: Parse the claim, Ask for artifacts, Understand preconditions, Score confirmed impact, and Evolve the workflow.
- One or two domain-specific follow-up questions can effectively expose shallow AI reports, as a model cannot bluff technical depth that an actual researcher would possess after a reproduction.

## Notable Quotes
- "Well written does not mean well substantiated."
- "The risk isn't about slow triage... most of the time it is fast triage, but a wrong triage. That is where we are spending our cycle."
- "Stronger facts is always going to beat the stronger writing these days."
- "A padded report won't survive the follow-up."
- "Score the verified truth and not the imagined worst-case scenario."

## Takeaways
- Update submission templates to mandate specific, non-optional technical preconditions (e.g., exact version, authentication state, and specific environment configurations).
- Transition triage workflows to focus exclusively on "testable statements" rather than the narrative impact claims provided in the report.
- Implement a policy of "delayed trust": do not assign severity or priority until a concrete artifact (PoC, log, or screenshot) has been validated.
- Use targeted, technical follow-up questions as a primary filter to distinguish between automated "padded" reports and genuine researcher findings.
