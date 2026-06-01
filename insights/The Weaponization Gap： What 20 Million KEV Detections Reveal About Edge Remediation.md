# The Weaponization Gap: What 20 Million KEV Detections Reveal About Edge Remediation

## Executive Summary
This presentation by Saeed Abbasi, Senior Manager of Security Research at Qualys, analyzes remediation data from over 20 million vulnerability detections across 10,000+ global customers between 2022 and 2025. The research focuses specifically on edge devices—firewalls, VPNs, and routers—which serve as the "crown jewels" and "front doors" of corporate networks. The findings highlight a stark reality: remediation for edge devices is often delayed by manual processes and maintenance windows, with 60% of vulnerabilities remaining open after a full year in some cases. However, the data also shows that vendor engineering choices, such as auto-updates, are far more effective than mandates or policies. Crucially, CISA’s Known Exploited Vulnerabilities (KEV) list acts more as a "discovery tool" than a prioritization tool for 85% of organizations, who only identify their exposure after a CVE is added to the list.

## Key Points
*   **The Edge Device Risk:** Edge devices are internet-facing assets that control data flow and security; they are highly targeted because they sit between trusted networks and internal data.
*   **Remediation Performance:** While remediation speed improved nine-fold from 2022 to 2025, a significant "long tail" remains. By the end of a year, roughly 60% of edge vulnerabilities across the study period were still unpatched.
*   **The Power of Auto-Updates:** Analysis of Fortinet (FortiWeb) data showed a massive spike in quick remediation due to auto-update features, proving that vendor engineering is more effective than manual organizational patching policies.
*   **CISA KEV as Discovery:** For 85% of customers, the first time they scanned for a specific vulnerability was *after* it appeared on the CISA KEV list. These "unaware" customers took an average of 319 days to fix vulnerabilities, compared to 41 days for those already aware of them.
*   **Vendor-Specific Bottlenecks:** Remediation times vary drastically by vendor. F5 and Fortinet vulnerabilities are often fixed in weeks, while Cisco and Juniper can take months due to requirements for manual firmware upgrades and reboots.
*   **Maintenance Window Cliffs:** Survival charts for vendors like Juniper show "cliffs" at roughly 200 days, indicating that many organizations wait for semi-annual maintenance windows to apply critical security patches.
*   **Negative Time-to-Exploit:** A study of 91 weaponized vulnerabilities showed many were exploited *prior* to public disclosure (zero-day exploitation), meaning organizations were already behind before they even knew the vulnerability existed.
*   **Low Reversion Rate:** Unlike endpoint OS or browser patches, edge device fixes are highly stable. Only 1 in 1,000 edge patches are reverted to a vulnerable state, providing a high ROI for patching efforts.
*   **The "Graveyard" Zone:** If an edge vulnerability is not patched within the first 90 days, it is unlikely to ever be patched, creating a permanent attack surface.
*   **Concentrated Threat Landscape:** Despite 48,000+ vulnerabilities being dropped in a year, less than 1% are weaponized and remotely accessible. Ransomware groups like Black Basta focused on only 62 specific vulnerabilities over an 18-month period.

## Notable Quotes
*   "You cannot solve your edge devices security by telling IT to patch faster. This doesn't happen... you need to put the right policy in order to help them."
*   "Suddenly we are saying that the KEV doesn't act as a prioritization, it acts as a discovery for a lot of customers."
*   "The vendor engineering choices is much more effective than any sort of mandate or policy."
*   "If things doesn't fix in first 90 days, so it is like a graveyard. You're not going to get fixed."
*   "The list of the one that you need to really prioritize and make sure that it is getting fixed... they're all under 1%."

## Takeaways
*   **Automate Where Possible:** Prioritize edge vendors that offer auto-update or streamlined patching mechanisms to bypass the limitations of human speed and manual approvals.
*   **Implement Pre-Approved Patching:** Establish policies that allow IT teams to bypass lengthy approval cycles for high-profile edge vulnerabilities (e.g., those on the CISA KEV list).
*   **Assume Breach on Edge Vulns:** For vulnerabilities weaponized prior to disclosure (like recent Ivanti cases), organizations must assume a breach has already occurred and initiate threat hunting and post-exploitation analysis rather than just patching.
*   **Invest in Asset Visibility:** Since 85% of KEV hits are "new" discoveries to organizations, maintaining a real-time, integrated asset inventory is critical to reducing the discovery-to-patch window.
*   **Focus on the 1%:** Prioritize remediation based on actual weaponization and remote accessibility rather than just CVSS scores to manage the overwhelming volume of CVEs.
