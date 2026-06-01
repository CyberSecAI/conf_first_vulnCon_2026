# Vulnerabilities Without CVEs: Governing the Dark Matter of Internal and Unknown Software

## Executive Summary
This talk argues that most vulnerability management (VM) programs are "structurally incapable" of seeing the risks that lead to real-world compromises. While traditional VM programs focus on "World 1" (known software with public CVEs), attackers thrive in "Worlds 2 and 3" (uncovered or "dark matter" software like internal tools, abandoned services, and mystery binaries). Because scanners rely on fingerprinting and matching against CVE databases, any software that cannot be identified produces zero findings—a "blind spot" that may encompass 20% or more of an enterprise's software stack. The speaker proposes a shift from "outside-in" scanning to "inside-out" host telemetry, using "Synthetic CVEs" to track and remediate risks based on observable behavior (e.g., command injection, insecure TLS, and unquoted paths) rather than public identifiers.

## Key Points
*   **The Identity Crisis:** Vulnerability finding depends on fingerprinting. if a scanner cannot name a product and version, it cannot match it to a CVE. No match equals no finding, which leads to a false sense of security in the dashboard.
*   **The Three Worlds of Software:**
    *   **World 1 (Known Universe):** Named products with CVE coverage (where VM programs work).
    *   **World 2 (Known but Uncovered):** Regional or niche vendors with no advisory ecosystem.
    *   **World 3 (Dark Matter):** Internal tools, abandoned forks, and temporary services that lack any system of record.
*   **Ask the Host, Not the Scanner:** Scanners infer from the outside (banners, ports), while the host observes from the inside (what actually ran, what privileges it held, and what it touched).
*   **Synthetic CVEs:** A finding based on host evidence and behavior (e.g., location, binary name, telemetry) that is routed through existing VM pipelines (SLAs, owners, dashboards) alongside traditional CVEs.
*   **OS-Native Telemetry Primitives:**
    *   **Windows:** Microsoft Detours for API hooking; Event Tracing for Windows (ETW) for kernel-grade process and network correlation.
    *   **Linux:** eBPF and Linux Security Module (LSM) for verified, low-overhead kernel visibility without shipping modules.
    *   **Mac:** Endpoint Security Framework (ESF) for process/file events and code signing metadata; Network Extension for attributed network flows.
*   **Detection Pattern: Web-to-Shell:** Identifying web-parented processes (e.g., Gunicorn) that spawn shells with interpolated input—a clear indicator of command injection (CWE-78) in software with zero CVE coverage.
*   **Detection Pattern: Execution Path Integrity:** Using host telemetry to find unquoted service paths or ambiguous binary references that allow for privilege escalation—a 20-year-old bug class still prevalent in internal tools.
*   **Detection Pattern: Insecure TLS:** Identifying clients that explicitly disable certificate validation at the socket/session level, which is often invisible to wire-based inspection but clear from host API monitoring.
*   **Lineage Matters:** A shell spawned by a web server is an anomaly; a shell spawned by a cron job is a routine backup. Host telemetry provides this "parent lineage" context for free.
*   **Practical Remediation for Dark Matter:** Since you often can't "patch" internal or abandoned software, remediation should focus on hardening (AppLocker/MAC), monitoring (EDR), isolating (segmentation), or decommissioning.

## Notable Quotes
*   "The dashboard can't see what isn't named... the risk doesn't disappear, the ticket disappears."
*   "If you only govern the risk that comes with a public identifier, you're only governing the street light, not the street."
*   " attackers are perfectly happy living in worlds two and three... because that's when the engagements got really interesting... because that's where nobody was watching."
*   "The difference is not the syscall, but actually the lineage."
*   "We're not inventing a new queue. We're sneaking new problems into the queue that we already trust."

## Takeaways
*   **Inventory Your Dark Matter:** Realize that "no findings" on a system doesn't mean "no risk." Actively look for software that isn't appearing in your vulnerability scanners.
*   **Implement Synthetic CVEs:** Don't build a parallel program; translate behavioral findings (like those from EDR or host logs) into a CVE-like format so they can be prioritized using existing organizational workflows.
*   **Leverage OS-Native Tools:** Use the telemetry tools you already own (ETW, eBPF, ESF) to monitor for high-risk behaviors like command injection or memory boundary crossings in internal applications.
*   **Prioritize Parentage over Ports:** When analyzing alerts, look at the process lineage (who spawned what) to distinguish legitimate system activity from exploitation of "dark matter" software.
*   **Decommission by Default:** If you find "dark matter" software that has no owner and no documentation, prioritize removing it rather than trying to find a patch that doesn't exist.
