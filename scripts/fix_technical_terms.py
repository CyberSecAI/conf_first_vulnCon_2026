import os
import re

# Technical corrections mapping
corrections = {
    r'fishing-resistant': 'phishing-resistant',
    r'fishing scam': 'phishing scam',
    r'fishing training': 'phishing training',
    r'fishing attack': 'phishing attack',
    r'S-bomb(s?)': r'SBOM\1',
    r'S-BOM(s?)': r'SBOM\1',
    r'AI bomb(s?)': r'AIBOM\1',
    r'rich ability': 'reachability',
    r'vuln richment': 'Vulnrichment',
    r'vulnerichment': 'Vulnrichment',
    r'SS-VC': 'SSVC',
    r'K-E-V': 'KEV',
    r'N-V-D': 'NVD',
    r'C-V-E': 'CVE',
    r'C-W-E': 'CWE',
    r'zero trust': 'Zero Trust',
    r'shift left': 'Shift Left',
    r'shift right': 'Shift Right',
    r'zero day': 'zero-day',
    r'cross site': 'cross-site',
    r'server side': 'server-side',
    r'built in': 'built-in'
}

def apply_corrections(text):
    for pattern, replacement in corrections.items():
        # Case insensitive replacement for terms
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def main():
    # Fix insights
    insights_dir = 'insights'
    for filename in os.listdir(insights_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(insights_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = apply_corrections(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed technical terms in {filename}")

    # Fix README.md
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = apply_corrections(content)
        
        if new_content != content:
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Fixed technical terms in README.md")

if __name__ == "__main__":
    main()
