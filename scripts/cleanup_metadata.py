import os
import re

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
    "Wo77sqI_Sqs": ("Quantifying Swiss Cheese, the Bayesian Way", "Stephen Shaffer (Moderna | EPSS SIG, US)"),
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

# Update README.md
with open('README.md', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    match = re.search(r'\| `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', line)
    if match:
        vid_id = match.group(1)
        if vid_id in mapping:
            title, speaker = mapping[vid_id]
            insights_link = match.group(3).strip()
            transcript_link = match.group(4).strip()
            video_link = match.group(5).strip()
            new_line = f"| `{vid_id}` | {title} | {speaker} | {insights_link} | {transcript_link} | {video_link} |\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    elif '| Video ID | Title | Key Insights |' in line:
        new_lines.append('| Video ID | Title | Speaker | Key Insights | Transcript | Video |\n')
    elif '| --- | --- | --- |' in line:
        new_lines.append('| --- | --- | --- | --- | --- | --- |\n')
    else:
        new_lines.append(line)

with open('README.md', 'w') as f:
    f.writelines(new_lines)

# Update insights files
insights_dir = 'insights'
for filename in os.listdir(insights_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(insights_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Find matching speaker from mapping
        matched_speaker = None
        official_title = None
        for vid_id, (title, speaker) in mapping.items():
            # Check if filename contains title (simplified match)
            # Remove special chars for matching
            clean_filename = re.sub(r'[^a-zA-Z0-9]', '', filename.lower().replace('.md', ''))
            clean_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            if clean_title in clean_filename or clean_filename in clean_title:
                matched_speaker = speaker
                official_title = title
                break
        
        if matched_speaker:
            # Update Title
            content = re.sub(r'^# .+', f"# {official_title}", content)
            
            # Update Executive Summary speaker info
            # We want to replace the first paragraph of Exec Summary with a clean version
            exec_summary_match = re.search(r'## Executive Summary\n(.*?)\n\n## Key Points', content, re.DOTALL)
            if exec_summary_match:
                old_exec = exec_summary_match.group(1)
                # Find common speaker mentions and replace
                # e.g. "The speaker, [Name], discusses..."
                # Or just prepend the clean speaker name if it's messy
                
                # Rule: Replace everything before the first "discusses" or "talks about" or "argues"
                new_exec = re.sub(r'^.*?(discusses|talks about|argues|explores|introduces|presents)', f"{matched_speaker} \\1", old_exec, flags=re.IGNORECASE)
                
                # If substitution didn't happen, just clean up generic subagent slop
                if new_exec == old_exec:
                    new_exec = f"{matched_speaker} presents a session on {official_title}. " + old_exec
                
                content = content.replace(old_exec, new_exec)
                
            with open(filepath, 'w') as f:
                f.write(content)

print("Done.")
