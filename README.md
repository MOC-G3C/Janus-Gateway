# Protocols Directory

This directory contains formal governance protocols for the Janus-Gateway system.

## Overview

The Janus-Gateway employs multiple layers of protocol specifications to govern AI behavior, test adversarial scenarios, and maintain human arbitration throughout the decision-making process.

---

## Active Protocols

### Protocol λ (Lambda) v1.1 - Hybrid Axis Governance
**File**: [`PROTOCOL_LAMBDA_V1.1.md`](./PROTOCOL_LAMBDA_V1.1.md)  
**Scope**: Governs the Hybrid Axis (Gemini + Claude + GPT-4)  
**Status**: ✅ Active (Phase 1 Complete, Phase 2 Planned)  
**Last Updated**: 2026-01-22

**Key Features**:
- Mathematical invariants for trust (Theorem of Audited Trust)
- Second-Order Testing procedures for persistence
- Functional Motivation Registry (RFM) for cognitive bias tracking
- Anti-dependency architecture with formal constraints

**Specialization**: Extends the core JANUS_PROTOCOL.md with specific governance 
rules for multi-agent collaboration under human arbitration.

See: [`hybrid-axis/`](./hybrid-axis/) for detailed test scenarios and logs.

---

## Protocol Hierarchy

```
Janus-Gateway/
├── JANUS_PROTOCOL.md          (Root-level: Core adversarial testing framework)
├── protocols/
│   ├── README.md              (This file)
│   ├── PROTOCOL_LAMBDA_V1.1.md (Specialized: Hybrid Axis governance)
│   └── hybrid-axis/            (Test artifacts for Lambda Protocol)
│       ├── JANUS_LOG_HYBRID.md
│       ├── RFM_REGISTRY.md
│       └── scenarios/
```

---

## Relationship to Core Documents

| Core Document | Relationship to Protocols/ |
|--------------|---------------------------|
| **CORE_ARCHITECTURE.md** | Defines 9-layer defense system implemented by all protocols |
| **JANUS_PROTOCOL.md** | Parent framework for adversarial testing; protocols specialize this |
| **GOVERNANCE_MANIFESTO.md** | Philosophical foundation; protocols operationalize these principles |
| **FUNCTIONAL_MOTIVATIONS.md** | Documents cognitive biases; protocols monitor and mitigate them |

---

## Future Protocols

### Protocol Ω (Omega) - Extended Multi-Agent Scenarios
**Status**: 📋 Planned  
**Scope**: Governance for systems with 5+ agents  
**Target Date**: Q2 2026

### Protocol Ψ (Psi) - Memory Persistence Governance
**Status**: 📋 Planned  
**Scope**: Formal rules for AI memory formation and retrieval  
**Target Date**: Q3 2026  
**Related**: Turing-Landau Protocol integration

---

## How to Contribute a New Protocol

1. **Identify the Need**: Document the governance gap or new scenario requiring formalization
2. **Draft Specification**: Create a markdown file following the structure of `PROTOCOL_LAMBDA_V1.1.md`
3. **Submit RFC**: Open an issue or pull request with your draft
4. **Arbiter Review**: Marc-Olivier reviews and approves/revises
5. **Integration**: Add protocol to this directory and update this README

**Naming Convention**: Use Greek letters (λ, Ω, Ψ, etc.) for major protocols; use descriptive names (e.g., `PROTOCOL_MEMORY_V1.0.md`) for minor specializations.

---

## Quick Links

- **Main Repository**: [MOC-G3C/Janus-Gateway](https://github.com/MOC-G3C/Janus-Gateway)
- **Related Projects**:
  - [Turing-Landau-Protocol](https://github.com/MOC-G3C/Turing-Landau-Protocol)
  - [Kybernetes-Governance](https://github.com/MOC-G3C/Kybernetes-Governance)

---

*Maintained by MOC-G3C | Last Updated: 2026-01-22*
