# Embracing the Era of Transparency: Automating VEX Application for Scalable, Context-Aware Security
## Executive Summary
Jessica Butler (NVIDIA, US) and Kristina Joos (NVIDIA, US) address the challenges of managing vulnerability transparency at scale, where modern container images often contain hundreds of dependencies. Despite automating the production of over 700,000 VEX (Vulnerability Exploitability eXchange) records, a critical "consumption gap" remains where security data often fails to reach the end user. The presenters discuss how NVIDIA uses VexStream and Agentic workflows to bridge this gap, proposing a shift toward "attestation-based" security to ensure that context-aware vulnerability data is actionable and visible at the point of deployment.

## Key Points
- AI and enterprise software stacks are increasingly complex; an average NVIDIA container image contains over 350 third-party dependencies.
- VEX is a critical tool for "proactive transparency," allowing vendors to tell customers which CVEs are "not affected" or "fixed" before they are even scanned.
- NVIDIA developed "VexStream" to automate VEX generation by integrating upstream vendor data (Ubuntu, Red Hat) and applying global rules across their portfolio.
- The team uses "Agentic workflows" (AI-assisted analysis) to help security experts perform exploitability assessments on thousands of CVEs simultaneously.
- A major ecosystem bottleneck exists because "publishing is not consumption"—customers often scan images without realizing a VEX record exists elsewhere.
- The presentation proposes using OCI attestations (via Cosign) to "staple" VEX and SBOM data directly to the container image.
- By attaching the VEX context to the image, scanners like Trivy can automatically filter out "not affected" vulnerabilities, eliminating "red alert" fatigue for customers.
- The shift to "attestation-based" security ensures that the results of complex internal security assessments are actionable and visible at the point of deployment.

## Notable Quotes
- "The software they pull from us... we want to make sure it's ready for production... VEX is a massive time saver."
- "Publishing isn't consumption... the data exists, but the workflow didn't."
- "Without VEX documents, we're causing red alerts everywhere we go."
- "We're basically a phone switchboard... manually adding the connection between the document and the consumer."

## Takeaways
- Automate VEX generation by leveraging upstream vendor data and internal heuristics to keep up with the scale of modern containerized software.
- Use OCI attestations (Cosign) to bind security context (VEX/SBOM) directly to your software artifacts to prevent information loss.
- Collaborate with scanner vendors to ensure they can automatically ingest VEX attestations during the standard vulnerability scanning process.
- Focus on closing the "transparency loop" by making vendor assessments as easy to consume as the vulnerability scans themselves.
