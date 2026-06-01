# The Dependency Mirage： Hidden Vulnerabilities in Your Compiled Binaries
## Executive Summary
This presentation by Craig Heffner and Peter Esmond from NetRise explores the critical gaps in traditional Software Composition Analysis (SCA) and Software Bill of Materials (SBOM) generation, particularly within compiled binaries. They demonstrate how statically linked libraries, vendored code, and build-time injections often lead to "hidden dependencies" that package managers like RPM or Debian fail to detect. By analyzing the "ground truth" of the binary itself rather than relying on manifests, organizations can uncover significant security risks, such as vulnerable versions of OpenSSL or zlib embedded deep within seemingly unrelated utilities. The speakers advocate for a "trust but verify" approach to SBOMs and the development of internal binary analysis capabilities to ensure true software supply chain transparency.

## Key Points
- **The Failure of Package Managers:** Tools like RPM only report what was installed via the package manager, completely missing statically linked or vendored libraries embedded within binaries.
- **Hidden OpenSSL Risk:** In one case study, a customer's RPM reported OpenSSL 3.0.7 (not vulnerable), but binary analysis revealed OpenSSL 3.0.0 (vulnerable) was statically linked into a Python shared object.
- **Vendored Code Pitfalls:** Developers often "copy-paste" source code (e.g., zlib into rsync) into their projects, leading to vulnerabilities that persist indefinitely regardless of system-level updates.
- **Static vs. Dynamic Linking:** Static linking embeds library code directly into the final binary, making it invisible to standard system scanners but permanently part of the attack surface.
- **Modern Language Challenges:** Languages like Go and Rust favor static linking by default, meaning every dependency in a project's tree is baked into the final binary and requires a full recompile to patch.
- **Binary as Ground Truth:** Source code is an intention; the binary is the reality of what actually runs on a system. Analysis must focus on the binary to find what "sneaks in" during build processes.
- **Recursive Dependencies:** A project with five direct dependencies may actually pull in dozens of sub-dependencies, all of which are statically compiled into the final product in languages like Rust.
- **Detection Techniques:** Simple methods like running `strings`, inspecting ELF headers for symbols, and searching for vendor-specific function names can uncover many hidden components.
- **Scaling Analysis:** Building a binary analysis capability requires baseline creation, manual verification of findings, and continuous monitoring as software evolves.
- **The "Probably Wrong" SBOM:** Third-party SBOMs are frequently incomplete; they might correctly list one version of a library while failing to mention an older, vulnerable version also present in the binary.

## Notable Quotes
- "What runs on a computer is not your source code... Computers don't know what source code is. But they understand the binary and that's really what's the truth."
- "The SBOM that you have, if it says you have libfoo version 123, yeah, you probably have libfoo version 123, but you may also have libfoo version 120, and it's just not in the SBOM."
- "Just because you have this file that lists all your dependencies doesn't mean those are all your dependencies."
- "I'm not saying [SBOMs] are wrong, but they're probably wrong... They're probably just incomplete."

## Takeaways
- **Verify Third-Party Claims:** Treat every incoming SBOM as a starting point, not a definitive list; use binary analysis to verify the actual contents of delivered software.
- **Audit Build Decisions:** Document why developers choose static linking or specific compiler flags, as these decisions have long-term security implications for patching.
- **Modernize Triage:** Security teams must move beyond manifest-based scanning and invest in tools or teams capable of deep binary inspection to find "lurking" vulnerabilities.
- **Full Rebuilds Matter:** When patching a critical library, don't assume a single update covers all instances; a full rebuild and binary scan are necessary to ensure the vulnerability is eradicated from all statically linked components.
