import os
import re
import urllib.parse

mapping = {
    "NyQy-oubdSI": ("Accuracy Is Not Enough: Detecting Hidden Risk in CVE Impact Prediction", "Keerthana Purushotham (IEEE, US)"),
    "aNC7rsAB5es": ("AI Is Writing Your Bug Reports. Can You Tell?", "Khushali Dalal (VulnCheck, US)"),
    "Gm-jwyYwiLU": ("AI Systems Are Software Systems", "Jonathan Spring (CISA, US)"),
    "3_s61rBvIVo": ("A Paradigm Shift in Vulnerability Identity: Why Vulnerability Databases Struggle", "Art Manion (Tharros Labs, US), Jay Jacobs (Empirical Security, US)"),
    "e7EnCS2kUxc": ("Automating CNA CVE Reporting and Monthly Bulletins at Atlassian", "Deepak Chintala (Atlassian, US), Zachary Echouafni (Atlassian, US)"),
    "b-sdKHpqPEs": ("Axiomatic Events that Evolved Vulnerability Databases", "Johnny Shaieb (IBM, US)"),
    "vV3kftnWkfg": ("Boosting Vulnerability Intelligence: How Accurate CWE Mappings Transform ML Model Performance", "David Starobinski (Boston University, US), Sevval Simsek (Boston University, US), Varsha Athreya (Boston University, US)"),
    "rrSIeBnJfC0": ("CISA-ENISA Joint Messaging", "Lindsey Cerkovnik (CISA, US), Nuno Rodrigues Carvalho (ENISA, BE)"),
    "Fo7BMKHpJWk": ("Contextual SBOMs: Unlocking Precise Vulnerability Management with Build-Time Content Intelligence", "Przemysław Roguski (Red Hat, PL)"),
    "B-HwXHcGIaA": ("CVE Decaf: Brewing Better and More Actionable Data Quality", "Jerry Gamblin (Cisco, US), Jay Jacobs (Empirical Security, US)"),
    "Oy9__NxBVfs": ("CVE Record Format - Purl and CPE Workshop", "Chris Coffin (MITRE), MZ MegaZone (F5, Inc., US)"),
    "Qdu2i8gTpWQ": ("Deriving CVSS from Multi-Scenario Attack Graphs: A Reproducible, Auditable Scoring Method", "Karel Knibbe (Volerion, NL), Ruben Bos (Volerion, NL)"),
    "FWFEjXXBdb8": ("Diving into the CVSS Base Score Metrics - An Exploratory Analysis Bridging Product Security Assessments and Real-World Attacks", "Kohei Taguchi (Panasonic Holdings Corporation, JP), Takayuki Uchiyama (Panasonic Holdings Corporation, JP), Yuichi Kikuchi (Panasonic Holdings Corporation, JP)"),
    "_yTAUmVhN6o": ("Embracing the Era of Transparency: Automating VEX Application for Scalable, Context-Aware Security", "Jessica Butler (NVIDIA, US), Kristina Joos (NVIDIA, US)"),
    "ZjKSqGkyZZI": ("Flipping the Criticality Funnel, A Practical Path to Real Prioritization", "Sophia Sanles-Luksetich (GitHub, US), Zachary Goldman (GitHub, US)"),
    "cvnQhjpDnyo": ("Fragile by Design: Large-Scale Evidence of Supply Chain Risk", "Gary Schwartz (NetRise)"),
    "Px3sNpTdsMY": ("From JSON to Clarity: Practical Tools for SBOM Interpretation", "John Bergland (IBM, US), Zadia Alden (Supply Chain Manager, GB)"),
    "mVO-j8CNYFo": ("From Roadmap to Results: Measuring CWE Adoption to Enable Prevention", "Alec Summers (The MITRE Corporation, US), Steve Christey Coley (The MITRE Corporation, US)"),
    "6PMGtHXag3E": ("How to Answer “What’s Affected” in Open Source", "Jess Lowe (Google, AU), Rex Pan (Google, AU)"),
    "YGl19THCXmE": ("Identifying Exploited and Likely-to-Be-Exploited Vulnerabilities", "Patrick Garrity (VulnCheck, US), Wade Sparks (VulnCheck, US)"),
    "qQ_n9_nbEE0": ("Lessons From NPM's Dark Side: Preventing the Next Shai-Hulud", "Jenn Gile (OpenSourceMalware, US)"),
    "_WYMpvXlmHI": ("Mind the Match: Why Vulnerability Matching Is Harder Than You Think", "Alexandra Selldorff (Manifest Cyber, US)"),
    "mJ52or3IadI": ("National CSIRT as a CVD Hub: Lessons from CERT.PL’s Vulnerability Coordination Cases", "Michał Dondajewski (CERT.PL, PL)"),
    "bBunxDmWb0A": ("NIST’s National Vulnerability Database Update and the Vulnerability Enrichment Ecosystem", "Harold Booth (National Institute of Standards and Technology (NIST), US)"),
    "k58hZqnNUbM": ("Operationalizing AIBOMs: Extending Vulnerability Management to AI Models and Datasets", "Alexandra Selldorff (Manifest Cyber, US), Ugur Koc (Manifest Cyber)"),
    "b1-XjLTOKtE": ("Organizational Context Matters: Security Control Effectiveness on Vulnerabilities for Prioritization", "Ertugrul Yaprak (Picus Security, TR), Mehmet Kiliç (Picus Security, TR)"),
    "zIMeD0yns2k": ("Panel: CVE Record Disputes Discussion: Policy, Process, and Opportunities for Improvement", "Alec Summers (The MITRE Corporation, US), Yogesh Mittal (Red Hat, IN), Lisa Olson (Microsoft, US), Lindsey Cerkovnik (CISA, US), Jimmy Calderon (TrendAI)"),
    "UW0MzmMQ4bY": ("Panel: The CVE Supplier ADP (SADP) Pilot: Am I Affected by Upstream?", "Art Manion (Tharros Labs, US), Jeremy Daigneau (MITRE, US), Lisa Olson (Microsoft, US), Yogesh Mittal (Red Hat, IN)"),
    "3rs1uYn7fe4": ("Preparing Vulnerability Management for the Post-Quantum Era: From Legacy Cryptography to Crypto-Agility", "Arun Singh (Qualys, US)"),
    "K6Z3YRWZ1zA": ("Production Is the New Attack Surface: Why Post-Deployment Endpoint Detection Is Now Critical", "Tracy Ragan (DeployHub.com, US)"),
    "Wo77sqI_Sqs": ("Quantifying Swiss Cheese, the Bayesian Way", r"Stephen Shaffer (Moderna \| EPSS SIG, US)"),
    "KXNi0oLXbEw": ("Remediation-Aware Reachability: Patching Containers, Prioritizing with Agentic-CTI, and Scaling Fixes from Code to Cloud", "Francesco Cipollone (Phoenix Security, GB)"),
    "m4bM2pWJBUQ": ("Saving Ourselves the ID Headache: How Purls Can Work for Models and Datasets", "Daniel Bardenstein (Manifest, US)"),
    "gUEjbWGH1Ro": ("Speeding Up Vulnerability Triage: Automating Context Retrieval with AI Agents", "Jorge Gimenez (Kraken, ES)"),
    "9qQUbDoa0-k": ("Stepping up the ENISA's role in Support of EU Vulnerability Services", "Johannes Kaspar Clos (ENISA, BE)"),
    "XPb2bTzpBAs": ("Supply Chains and Malware Campaigns: Is CVE the Right Way to Name the Game?", "Art Manion (Tharros Labs, US), Caitlin Condon (VulnCheck, US), David Welch (HeroDevs, US), Shelby Cunningham (GitHub, US)"),
    "YKBIdPfQ2Zc": ("Taming the Scanner Storm: How VEX Brings Context to Vulnerability Data", "Jessica Butler (NVIDIA, US)"),
    "FsR3aKEXsxM": ("The AI Arms Race in Vulnerability Management, Who’s Winning?", "Yotam Perkal (Pluto Security, IL)"),
    "qiTQGY9vxks": ("The CVE Blind Spot: Defeating \"Hidden EOLs\" and Repo Jacking with Engineering Triage & Code Diet", "Kota Kanbe (Future Corporation, JP), Ryunosuke Tanai (Future Corporation, JP)"),
    "ci5a19peUag": ("The CVE Program Quality Era: Strengthening Trust and Impact In Global Vulnerability Data", "Lindsey Cerkovnik (CISA, US), Alec Summers (The MITRE Corporation, US)"),
    "4TuSNHXdWTo": ("The Dependency Mirage: Hidden Vulnerabilities in Your Compiled Binaries", "Craig Heffner (NetRise, US), Peter Eacmen (Netrise)"),
    "iCzssRtsh3o": ("The Hidden Cost of CVEs: Can CSAF and VEX Change the Equation?", "Lisa Olson (Microsoft, US)"),
    "H8sYl2fPtDs": ("The Myth of the Meteoric Rise in Vulnerabilities", "Scott Moore (VulnCheck, US)"),
    "t_CYTZo9GjI": ("The Quality Era of CVE: A Blueprint for Global Software Safety", "Bob Lord (US)"),
    "_jkKknGcD28": ("The Vulnerability Ecosystem’s Vendor Bias — Exposed by Open Source", "Pete Allor (CVE Board, US), Yogesh Mittal (Red Hat, IN)"),
    "xBrXAzWhmv0": ("The Weaponization Gap: What 20 Million KEV Detections Reveal About Edge Remediation", "Saeed Abbasi (Qualys Threat Research Unit (TRU), US)"),
    "yxz70bkDOwM": ("Three Musketeers: CVE, CSAF, and VEX", "Eoin Wilson-Manion (Tharros Labs), Tyler Zellers (Tharros Labs), Jonathan Spring (CISA, US)"),
    "4r4ENWFynu8": ("Transforming Vulnerability Management with Advanced Dependency Knowledge Graphs", "David Starobinski (Boston University, US), Sevval Simsek (Boston University, US)"),
    "dMejnDGQHYo": ("Vulnerabilities Without CVEs: Governing the Dark Matter of Internal and Unknown Software", "Josh Skorich (Spektion, US)"),
    "hgS0kXkX_HI": ("Vulnrichment Playground", "Art Manion (Tharros Labs, US), Lindsey Cerkovnik (CISA, US)")
}

header_part = """# CVE/FIRST VulnCon 2026 Conference Index

## Meta Key Insights
*Overarching strategic themes synthesized from recurring topics across 50 conference sessions.*

### Summary
VulnCon 2026 marked the definitive transition of the vulnerability management ecosystem from a "Growth Era" to a "Quality Era." The focus has shifted from the sheer volume of CVE assignments to the technical precision of records, mandatory machine-readable transparency (CSAF/VEX), and the urgent need to govern "dark matter" software that traditional scanners cannot see.

### Key Takeaway
Stop chasing raw CVE counts; prioritize machine-usable data, automate the "Am I Affected?" decision through CSAF/VEX, and pivot to host-based behavioral detection to cover the 20% blind spot of internal and un-named software.

---

### Overarching Themes

#### 1. The Quality Era & Modern Standards
The industry is moving toward a "CAT" (Complete, Accurate, Timely) framework for vulnerability data. This includes mandatory CWE root-cause mapping, structured CVSS 4.0 scoring, and the deprecation of generic "no info" mappings in favor of Knowledge Graph-driven precision.

#### 2. Machine-Readable Transparency (CSAF/VEX)
VEX (Vulnerability Exploitability eXchange) and CSAF (Common Security Advisory Framework) are no longer optional "experiments." They are the primary tools for reducing the global labor cost of vulnerability triage, with pilots showing that automated exploitability assessments can reduce developer noise by up to 84%.

#### 3. Governing the "Dark Matter" & Binary Reality
Traditional manifest-based SCA is failing to detect up to 2/3 of components in compiled binaries. Organizations must govern the "dark matter"—un-named internal tools and abandoned appliances—using host telemetry (eBPF, ETW) and "Synthetic CVEs" to manage behavioral risks that lack public identifiers.

#### 4. Supply Chain Intelligence (SBOM & PURL)
The SBOM ecosystem is maturing from flat lists to "Contextual SBOMs" that track build-time provenance. Package URLs (PURLs) are emerging as the decentralized successor to CPE, providing a standardized way to identify everything from NPM packages to AI model weights and datasets.

#### 5. AI Security & Agentic Triage
AI is accelerating both sides of the arms race: "Mitis" models have boosted exploit success rates to 70%, while "Agentic CTI" and orchestrator-based triage are helping defenders automate context retrieval. The introduction of AI-BOMs ensures that AI models are treated as software systems with clear lineage and vulnerability tracking.

#### 6. The Weaponization Gap
Data reveals that 30% of edge vulnerabilities (VPNs, firewalls) are weaponized *before* public disclosure. With "unaware" organizations taking a median of 319 days to patch, the only viable defense is a "mitigation-first" posture combined with vendor-managed auto-updates.

---

## Individual Talk Insights
*Detailed analysis from each session, including Executive Summaries, Key Points, and Notable Quotes.*

| Video ID | Title | Speaker | Key Insights | Transcript | Video |
| --- | --- | --- | --- | --- | --- |
"""

# Sort sessions by title for the table
sorted_sessions = sorted(mapping.items(), key=lambda x: x[1][0])

table_rows = []
for vid_id, (title, speaker) in sorted_sessions:
    # Match the sanitization logic used during file creation
    safe_filename = title.replace(':', '：').replace('?', '').replace('"', '').strip()
    
    # URL encode ONLY the filename, keep ./insights/ literal
    insights_fn_quoted = urllib.parse.quote(f"{safe_filename}.md")
    transcript_fn_quoted = urllib.parse.quote(f"{safe_filename}.txt")
    
    insights_link = f"[Insights](./insights/{insights_fn_quoted})"
    transcript_link = f"[Transcript](./transcripts/{transcript_fn_quoted})"
    video_link = f"[YouTube](https://www.youtube.com/watch?v={vid_id})"
    
    row = f"| `{vid_id}` | {title} | {speaker} | {insights_link} | {transcript_link} | {video_link} |"
    table_rows.append(row)

with open('README.md', 'w') as f:
    f.write(header_part)
    f.write('\n'.join(table_rows))
    f.write('\n')

print("Done fixing README links.")
