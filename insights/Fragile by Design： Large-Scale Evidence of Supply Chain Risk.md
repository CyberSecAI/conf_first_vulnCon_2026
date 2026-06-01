# Fragile by Design： Large-Scale Evidence of Supply Chain Risk
## Executive Summary
This presentation reveals the stark reality of the software supply chain through large-scale binary analysis of 19,000 firmware and container assets. The research demonstrates that manifest-based scanning (SCA) captures only a fraction of actual risk, with nearly 99% of vulnerabilities residing in "invisible" components not listed in software manifests. By looking past declared intent to "Software Reality," the session uncovers widespread non-CVE risks, including hardcoded credentials and expired certificates, that represent a failure of basic security hygiene across the industry.

## Key Points
- Manifest-based tools provide an incomplete picture; nearly 60% of firmware assets analyzed had no manifest-declared components but were rife with vulnerabilities.
- Binary analysis uncovers "hidden" components: 99% of vulnerabilities found were in libraries and OS parts that never appear in standard software manifests.
- The Linux kernel is the primary driver of vulnerability exposure, frequently harboring CVEs that are over 20 years old because no one is looking at the base OS layer.
- Static linking and build-time inclusions often introduce vulnerable versions of libraries (like OpenSSL or zlib) that differ from what a developer declared in their source code.
- Non-CVE risks are as critical as vulnerabilities: research found thousands of instances of user IDs with no passwords and private key pairs stored on public-facing devices.
- Expired certificates are a leading indicator of poor security maintenance; if a vendor isn't tracking certificates, they aren't tracking deeper vulnerabilities.
- The "Blast Radius" of a compromise (e.g., a malicious package commit) is often invisible to consumers because they only see the top-level package, not the transitive tree.
- Prioritization must follow visibility; once the total inventory of "2,700 CVEs" on a device is revealed, it can be filtered down to 4 truly actionable ones using accessibility and threat data.

## Notable Quotes
- "What is present comes before what matters most."
- "Expired certificates are there for only one reason: because no one is looking."
- "Whether or not you know about it, you have the risk. Wouldn't you rather know about it?"
- "Companies with no CPEs have no CVEs because the two go together... that's the system working the way it's meant to work, but it's an incomplete picture."

## Takeaways
- Supplement traditional SCA with binary analysis to reveal the "Software Reality" of what is actually running in your production environment.
- Don't accept a vendor's SBOM as absolute truth; verify the inventory by unpacking the artifact to find "invisible" dependencies and kernels.
- Broaden your security audits to include misconfigurations like hardcoded credentials and improper key management, which are often more exploitable than CVEs.
- Map upstream and downstream dependencies to understand your organization's true exposure to "blast radius" events in the open-source ecosystem.
