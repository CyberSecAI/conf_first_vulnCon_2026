# The Myth of the Meteoric Rise in Vulnerabilities
## Executive Summary
Scott Moore, a veteran vulnerability data collector and creator of the X-Force database, challenges the narrative that the current explosion in CVE numbers represents a genuine surge in critical software risk. Instead, he identifies a "CVE factory" phenomenon where student homework assignments, university projects, and ad-revenue-generating source code repositories are being flooded with thousands of CVEs for the same recycled, insecure code. By analyzing sites like SourceCodester and Code Projects, Moore demonstrates how identical SQL injection vulnerabilities in "reskinned" templates are being assigned unique CVE IDs, creating massive noise in the ecosystem. He estimates that while legitimate vulnerabilities are rising at a steady, manageable rate, the "pollution" from these low-quality sources could easily generate over 80,000 additional, meaningless CVEs if left unchecked.

## Key Points
- **The Data Hoarder's Perspective:** Moore's career began with collecting exploits in 1993, eventually leading to the creation of the X-Force database, one of the four original sources used to seed the CVE program.
- **Historic Spikes:** Significant jumps in CVE counts often correlate with specific events, such as the 2005 rise driven by the "Milw0rm" exploit database and the 2017 expansion of CNAs.
- **The "Hell Breaks Loose" Moment (2021):** The inclusion of research CNAs—organizations that assign CVEs for vulnerabilities reported to them rather than found internally—led to a massive influx of low-quality records.
- **Recycled "Homework" Code:** Sites like SourceCodester host hundreds of "management systems" (zoo, hospital, bank, etc.) that are actually the same vulnerable PHP template reskinned to generate ad revenue.
- **The SQL Injection Template:** Nearly every query in these projects uses simple concatenation (e.g., `select * from table where user = input`), making them "SQL injectable by design."
- **CVE Factory Stats:** SourceCodester alone has 369 projects with 1,700 existing CVEs; however, Moore's analysis suggests 15,000+ more vulnerabilities are ready to be assigned in just those specific projects.
- **Potential for 81,000+ Fake CVEs:** Based on the prevalence of vulnerable code in these "ad-ware" repositories, the ecosystem could be flooded with tens of thousands of IDs for software that no one actually uses in production.
- **AI-Driven Vulnerability Discovery:** Moore demonstrated the "noise" problem by using Claude to find 203 vulnerabilities in 15 WordPress plugins in just two hours, highlighting how easily automated tools can overwhelm manual triage.
- **Rule Violations:** Assigning multiple CVEs to independent projects sharing the same vulnerable code template violates the core CVE rule of "one CVE for one piece of code."
- **Operational Pollution:** Low-quality CVEs distract security teams and executives, making it harder to prioritize "real" software like WordPress, which is used by billions and genuinely requires rigorous CVE management.

## Notable Quotes
- "If you came here to hear about that vulnerabilities are actually not rising, then I have bad news for you... but I have a problem with collecting data and hoarding data."
- "SourceCodester... is a CVE factory that hosts 369 different vulnerable applications... because it hosts one template 369 times."
- "It’s like a cardboard box getting a CVE compared to an automobile."
- "I can estimate... I can assign 81,000 CVEs tomorrow for this code. But this is just all noise and we need to stop doing it."

## Takeaways
- **Differentiate "Real" Risk:** Security organizations must filter out CVEs associated with "homework" repositories (e.g., SourceCodester, PHP Gurukul) to avoid wasting resources on non-production software.
- **Demand CVE Quality:** The community and CVE Secretariat should enforce existing rules to prevent the "reskinning" of vulnerabilities from inflating global stats.
- **Leverage AI Carefully:** AI is a force multiplier for vulnerability discovery (finding 200+ issues in hours), but without strict governance, it will exacerbate the "slop" and noise in vulnerability databases.
- **Focus on Ecosystems:** Prioritize CVEs in widely used platforms like WordPress over niche, ad-driven code repositories that lack a genuine user base or maintenance lifecycle.
