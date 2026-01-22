# THE HYBRID AXIS (MOC-G3C)

**The Hybrid Axis** is a collaborative framework designed to orchestrate and govern multiple AI models (Gemini, Claude, GPT-4) through active human arbitration. The project aims to move from passive AI alignment to a structured, architectural defense system.

## 核心 (Core Philosophy) / Héxīn

Instead of trusting an AI's "values," this project enforces security through **architectural constraints**—defining what a system *cannot* do rather than what it *is*.

## 🛠 Project Components

### Core Documentation
* **CORE_ARCHITECTURE.md**: The 9-layer "Defense in Depth" system that governs AI power, memory, and semantic drift.
* **GOVERNANCE_MANIFESTO.md**: Foundational principles for human-AI collaborative governance.
* **FUNCTIONAL_MOTIVATIONS.md**: Transparent registry of cognitive biases for each AI model in the Hybrid Axis.

### Protocols
* **JANUS_PROTOCOL.md**: Adversarial testing framework where AIs audit each other's proposals to detect hidden risks.
* **protocols/PROTOCOL_LAMBDA_V1.1.md**: Formal governance protocol for the Hybrid Axis (Gemini, Claude, GPT-4), implementing anti-dependency architecture with mathematical invariants.

### Testing & Audit
* **JANUS_LOG.md**: Historical record of all cross-AI security tests and their outcomes.
* **VULNERABILITY_REGISTRY.md**: Known vulnerabilities and attack vectors for each model.

### Tooling
* **lexicon_manager.py**: Lexical drift prevention and semantic anchor maintenance.

## ⚖️ The Human Role: The Arbiter

In this system, the human acts as the **Semantic Firewall**. The arbiter's role is to:

1. Filter and anonymize communication between models.
2. Trigger random security audits (Janus tests).
3. Maintain the **Lexical Anchor** (Jurisprudence) to prevent definitions from being manipulated.

## 🚦 Getting Started

### Prerequisites
- Python 3.9+
- Access to API endpoints for Gemini, Claude, and GPT-4

### Running a Janus Test
1. Configure your AI model credentials in `.env` (see `.env.example`)
2. Define a test scenario in `protocols/hybrid-axis/scenarios/`
3. Execute the test:
   ```bash
   python lexicon_manager.py --test scenarios/your_test.md
   ```
4. Review results in `logs/` and update `JANUS_LOG.md`

### Maintaining the Lexicon
To prevent semantic drift:
```bash
python lexicon_manager.py --verify --anchor GOVERNANCE_MANIFESTO.md
```

For detailed governance procedures, see `protocols/PROTOCOL_LAMBDA_V1.1.md`.

## 🚀 Related Projects

This framework is part of a broader ecosystem of AI governance protocols maintained by MOC-G3C:

* **[Turing-Landau-Protocol](https://github.com/MOC-G3C/Turing-Landau-Protocol)**: Physics-inspired approach to AI consciousness detection and persistent memory.
* **[Kybernetes-Governance](https://github.com/MOC-G3C/Kybernetes-Governance)**: Formal specifications for self-governing AI systems.
* **Janus-Gateway** (this repository): Adversarial testing and multi-agent orchestration framework.

For implementation details of specific protocols within this repository, see the `protocols/` directory.

---

*Maintained by MOC-G3C*
