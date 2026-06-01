# Saving Ourselves the ID Headache： How Purls Can Work for Models and Datasets

## Executive Summary
Daniel (CEO of Manifest Cyber) addresses the looming problem of AI security, specifically the lack of standard identifiers for AI artifacts like models and datasets. He argues that because AI is a subset of software, the industry should avoid creating a brand-new identifier and instead adopt the existing Package URL (PURL) standard. This would allow organizations to precisely identify the models they use, track vulnerabilities, and manage their AI supply chain using existing AppSec and PSIRT workflows.

## Key Points
* **Identification Gap:** Most organizations do not know which specific versions or snapshots of AI models (e.g., Claude, GPT) they are using, making vulnerability response impossible.
* **AI Risks are Present:** AI "vulnerabilities" (traditional exploits, biased datasets, poisoned weights) are already increasing and targeted by adversaries.
* **Workflow Dependency:** Effective PSIRT response depends on identifiers to answer: "Am I affected?", "Where is it?", and "What is the blast radius?"
* **CPE vs. PURL:** CPEs describe vendor products but lack artifact precision. PURLs are native to ecosystems and better at identifying the exact thing (e.g., a specific Hugging Face model file) deployed.
* **AI Artifact Complexity:** Models involve owners (Meta), base names (Llama), snapshots (commit shas), formats (GGUF, Safetensors), and mutations (quantization, fine-tuning).
* **Avoiding Standard Proliferation:** Creating a new AI-specific identifier would lead to the "15 concurrent standards" problem; PURLs are flexible enough to adapt.
* **Sourcing Variation:** The same model can be fetched from Hugging Face, Bedrock, or Vertex; PURLs can explicitly encode these different source locations and interfaces.
* **Use Cases:** Standardized identifiers enable automated SBOM generation, governance for regulatory compliance (e.g., FDA), and vulnerability tracking across the AI supply chain.
* **Call to Action:** The community needs to align on PURL taxonomies for AI, and tools/databases (NVD, OSV) must bake in support for these identifiers to reduce friction.

## Notable Quotes
* "AI is a subset and necessarily is deployed into software."
* "Vulnerability response depends on identifiers... the foundational aspect that is missing is how do we actually name and identify the AIs that we're using?"
* "PURLs answer the question, 'What exactly is this thing, this artifact that we have deployed in our environment?'"
* "Please let's not do this [create a brand new standard]. Let's use an existing standard to actually name our AI assets."

## Takeaways
* Adopt PURLs as the primary identifier for AI models and datasets to leverage existing software supply chain security tools and processes.
* Ensure AI SBOMs include granular details such as model snapshots, quantization types, and provider sources (e.g., Bedrock vs. direct API).
* Collaborate with CNAs and vulnerability databases to standardize the nomenclature for AI-related security advisories.
