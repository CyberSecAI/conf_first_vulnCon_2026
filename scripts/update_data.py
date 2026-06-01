
import os
import re

mapping = {
    "Accuracy Is Not Enough: Detecting Hidden Risk in CVE Impact Prediction": "Keerthana Purushotham (IEEE, US)",
    "AI Is Writing Your Bug Reports. Can You Tell?": "Khushali Dalal (VulnCheck, US)",
    "AI Systems Are Software Systems": "Jonathan Spring (CISA, US)",
    "A Paradigm Shift in Vulnerability Identity: Why Vulnerability Databases Struggle": "Art Manion (Tharros Labs, US), Jay Jacobs (Empirical Security, US)",
    "Automating CNA CVE Reporting and Monthly Bulletins at Atlassian": "Deepak Chintala (Atlassian, US), Zachary Echouafni (Atlassian, US)",
    "Axiomatic Events that Evolved Vulnerability Databases": "Johnny Shaieb (IBM, US)",
    "Boosting Vulnerability Intelligence: How Accurate CWE Mappings Transform ML Model Performance": "David Starobinski (Boston University, US), Sevval Simsek (Boston University, US), Varsha Athreya (Boston University, US)",
    "CISA-ENISA Joint Messaging": "Lindsey Cerkovnik (CISA, US), Nuno Rodrigues Carvalho (ENISA, BE)",
    "Contextual SBOMs: Unlocking Precise Vulnerability Management with Build-Time Content Intelligence": "Przemysław Roguski (Red Hat, PL)",
    "CVE Decaf: Brewing Better and More Actionable Data Quality": "Jerry Gamblin (Cisco, US), Jay Jacobs (Empirical Security, US)",
    "CVE Record Format - Purl and CPE Workshop": "Chris Coffin (MITRE), MZ MegaZone (F5, Inc., US)",
    "Deriving CVSS from Multi-Scenario Attack Graphs: A Reproducible, Auditable Scoring Method": "Karel Knibbe (Volerion, NL), Ruben Bos (Volerion, NL)",
    "Diving into the CVSS Base Score Metrics - An Exploratory Analysis Bridging Product Security Assessments and Real-World Attacks": "Kohei Taguchi (Panasonic Holdings Corporation, JP), Takayuki Uchiyama (Panasonic Holdings Corporation, JP), Yuichi Kikuchi (Panasonic Holdings Corporation, JP)",
    "Embracing the Era of Transparency: Automating VEX Application for Scalable, Context-Aware Security": "Jessica Butler (NVIDIA, US), Kristina Joos (NVIDIA, US)",
    "Flipping the Criticality Funnel, A Practical Path to Real Prioritization": "Sophia Sanles-Luksetich (GitHub, US), Zachary Goldman (GitHub, US)",
    "Fragile by Design: Large-Scale Evidence of Supply Chain Risk": "Gary Schwartz (NetRise)",
    "From JSON to Clarity: Practical Tools for SBOM Interpretation": "John Bergland (IBM, US), Zadia Alden (Supply Chain Manager, GB)",
    "From Roadmap to Results: Measuring CWE Adoption to Enable Prevention": "Alec Summers (The MITRE Corporation, US), Steve Christey Coley (The MITRE Corporation, US)",
    "How to Answer “What’s Affected” in Open Source": "Jess Lowe (Google, AU), Rex Pan (Google, AU)",
    "Identifying Exploited and Likely-to-Be-Exploited Vulnerabilities": "Patrick Garrity (VulnCheck, US), Wade Sparks (VulnCheck, US)",
    "Lessons From NPM's Dark Side: Preventing the Next Shai-Hulud": "Jenn Gile (OpenSourceMalware, US)",
    "Mind the Match: Why Vulnerability Matching Is Harder Than You Think": "Alexandra Selldorff (Manifest Cyber, US)",
    "National CSIRT as a CVD Hub: Lessons from CERT.PL’s Vulnerability Coordination Cases": "Michał Dondajewski (CERT.PL, PL)",
    "NIST’s National Vulnerability Database Update and the Vulnerability Enrichment Ecosystem": "Harold Booth (National Institute of Standards and Technology (NIST), US)",
    "Operationalizing AIBOMs: Extending Vulnerability Management to AI Models and Datasets": "Alexandra Selldorff (Manifest Cyber, US), Ugur Koc (Manifest Cyber)",
    "Organizational Context Matters: Security Control Effectiveness on Vulnerabilities for Prioritization": "Ertugrul Yaprak (Picus Security, TR), Mehmet Kiliç (Picus Security, TR)",
    "Panel: CVE Record Disputes Discussion: Policy, Process, and Opportunities for Improvement": "Alec Summers (The MITRE Corporation, US), Yogesh Mittal (Red Hat, IN), Lisa Olson (Microsoft, US), Lindsey Cerkovnik (CISA, US), Jimmy Calderon (TrendAI)",
    "Panel: The CVE Supplier ADP (SADP) Pilot: Am I Affected by Upstream?": "Art Manion (Tharros Labs, US), Jeremy Daigneau (MITRE, US), Lisa Olson (Microsoft, US), Yogesh Mittal (Red Hat, IN)",
    "Preparing Vulnerability Management for the Post-Quantum Era: From Legacy Cryptography to Crypto-Agility": "Arun Singh (Qualys, US)",
    "Production Is the New Attack Surface: Why Post-Deployment Endpoint Detection Is Now Critical": "Tracy Ragan (DeployHub.com, US)",
    "Quantifying Swiss Cheese, the Bayesian Way": "Stephen Shaffer (Moderna | EPSS SIG, US)",
    "Remediation-Aware Reachability: Patching Containers, Prioritizing with Agentic-CTI, and Scaling Fixes from Code to Cloud": "Francesco Cipollone (Phoenix Security, GB)",
    "Saving Ourselves the ID Headache: How Purls Can Work for Models and Datasets": "Daniel Bardenstein (Manifest, US)",
    "Speeding Up Vulnerability Triage: Automating Context Retrieval with AI Agents": "Jorge Gimenez (Kraken, ES)",
    "Stepping up the ENISA's role in Support of EU Vulnerability Services": "Johannes Kaspar Clos (ENISA, BE)",
    "Supply Chains and Malware Campaigns: Is CVE the Right Way to Name the Game?": "Art Manion (Tharros Labs, US), Caitlin Condon (VulnCheck, US), David Welch (HeroDevs, US), Shelby Cunningham (GitHub, US)",
    "Taming the Scanner Storm: How VEX Brings Context to Vulnerability Data": "Jessica Butler (NVIDIA, US)",
    "The AI Arms Race in Vulnerability Management, Who’s Winning?": "Yotam Perkal (Pluto Security, IL)",
    "The CVE Blind Spot: Defeating \"Hidden EOLs\" and Repo Jacking with Engineering Triage & Code Diet": "Kota Kanbe (Future Corporation, JP), Ryunosuke Tanai (Future Corporation, JP)",
    "The CVE Program Quality Era: Strengthening Trust and Impact In Global Vulnerability Data": "Lindsey Cerkovnik (CISA, US), Alec Summers (The MITRE Corporation, US)",
    "The Dependency Mirage: Hidden Vulnerabilities in Your Compiled Binaries": "Craig Heffner (NetRise, US), Peter Eacmen (Netrise)",
    "The Hidden Cost of CVEs: Can CSAF and VEX Change the Equation?": "Lisa Olson (Microsoft, US)",
    "The Myth of the Meteoric Rise in Vulnerabilities": "Scott Moore (VulnCheck, US)",
    "The Quality Era of CVE: A Blueprint for Global Software Safety": "Bob Lord (US)",
    "The Vulnerability Ecosystem’s Vendor Bias — Exposed by Open Source": "Pete Allor (CVE Board, US), Yogesh Mittal (Red Hat, IN)",
    "The Weaponization Gap: What 20 Million KEV Detections Reveal About Edge Remediation": "Saeed Abbasi (Qualys Threat Research Unit (TRU), US)",
    "Three Musketeers: CVE, CSAF, and VEX": "Eoin Wilson-Manion (Tharros Labs), Tyler Zellers (Tharros Labs), Jonathan Spring (CISA, US)",
    "Transforming Vulnerability Management with Advanced Dependency Knowledge Graphs": "David Starobinski (Boston University, US), Sevval Simsek (Boston University, US)",
    "Vulnerabilities Without CVEs: Governing the Dark Matter of Internal and Unknown Software": "Josh Skorich (Spektion, US)",
    "Vulnrichment Playground": "Art Manion (Tharros Labs, US), Lindsey Cerkovnik (CISA, US)"
}

def normalize(s):
    s = s.lower().replace(':', '').replace('：', '').replace('...', '').replace('"', '').replace('“', '').replace('”', '').replace(' ', '').replace('to', '').replace('by', '')
    return s

def get_speaker(title):
    n_title = normalize(title)
    if title in mapping: return mapping[title]
    for k, v in mapping.items():
        if normalize(k) == n_title or normalize(k) in n_title or n_title in normalize(k): return v
    return "UNKNOWN"

def update_readme():
    with open('README.md', 'r') as f: lines = f.readlines()
    new_lines = []
    in_table = False
    for line in lines:
        if line.startswith('| Video ID | Title | Speaker | Key Insights |'):
            new_lines.append('| Video ID | Title | Speaker | Key Insights | Transcript | Video |\n')
            in_table = True
            continue
        if line.startswith('| --- | --- | --- | --- | --- | --- |'):
            new_lines.append('| --- | --- | --- | --- | --- | --- |\n'); continue
        if in_table and line.startswith('| `'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 7:
                title = parts[2]
                clean_title = title
                if '[' in title and ']' in title: clean_title = re.search(r'\[(.*?)\]', title).group(1)
                speaker = get_speaker(clean_title)
                new_line = f"| {parts[1]} | {title} | {speaker} | {parts[4]} | {parts[5]} | {parts[6]} |\n"
                new_lines.append(new_line); continue
        new_lines.append(line)
        if in_table and not line.strip() and not line.startswith('|'): in_table = False
    with open('README.md', 'w') as f: f.writelines(new_lines)

def update_insights():
    files = os.listdir('insights')
    for filename in files:
        if not filename.endswith('.md'): continue
        filepath = os.path.join('insights', filename)
        with open(filepath, 'r') as f: content = f.read()
        h1_match = re.search(r'^# (.*)', content, re.MULTILINE)
        if h1_match:
            current_h1 = h1_match.group(1).strip()
            speaker = get_speaker(current_h1)
            official_title = current_h1
            for k in mapping:
                if get_speaker(k) == speaker: official_title = k; break
            if speaker != "UNKNOWN":
                content = content.replace(f"# {current_h1}", f"# {official_title}")
                # Clean up mess from previous run
                content = re.sub(r'The speakers, .*?, discuss the topic\.\n', '', content)
                content = content.replace('Arun Pratap Singh from QualysArun Singh (Qualys, US)', 'Arun Singh (Qualys, US)')
                content = content.replace('Panasonic researchersKohei Taguchi (Panasonic Holdings Corporation, JP), Takayuki Uchiyama (Panasonic Holdings Corporation, JP), Yuichi Kikuchi (Panasonic Holdings Corporation, JP)', 'Kohei Taguchi (Panasonic Holdings Corporation, JP), Takayuki Uchiyama (Panasonic Holdings Corporation, JP), Yuichi Kikuchi (Panasonic Holdings Corporation, JP)')
                
                def repl_main(m): return f"{m.group(1)}{speaker}{m.group(2)}"
                patterns = [
                    (r'(The speaker(?:s)?,? ).*?(, (?:argues|presents|addresses|discusses|explores|introduces|focuses|highlights|outlines|examines|shares|delves|emphasizes|notes|details))', repl_main),
                    (r'(The speaker(?:s)?,? ).*?(\.)', repl_main),
                    (r'(Speaker ).*?(\.)', repl_main),
                    (r'(Speaker ).*?( (?:highlights|notes|details|points out))'),
                ]
                found = False
                for p in patterns:
                    if isinstance(p, tuple):
                        if re.search(p[0], content, flags=re.IGNORECASE):
                            content = re.sub(p[0], p[1], content, count=1, flags=re.IGNORECASE)
                            found = True; break
                    else:
                        if re.search(p, content, flags=re.IGNORECASE):
                            content = re.sub(p, lambda m: f"{m.group(1)}{speaker}{m.group(2)}", content, count=1, flags=re.IGNORECASE)
                            found = True; break
                if not found:
                    if "## Executive Summary" in content:
                        content = content.replace("## Executive Summary\n", f"## Executive Summary\nThe speaker, {speaker}, discusses the topic.\n")
        with open(filepath, 'w') as f: f.write(content)

if __name__ == "__main__":
    update_readme()
    update_insights()
