# Contributing to Cyber-Socialism Governance (CSG-AA)

Thank you for your interest in contributing to the **Cyber-Socialism Governance for Autonomous Agents** framework. Ensuring systemic alignment and preventing autonomous multi-agent collusion requires rigorous collaboration. 

By contributing to this repository, you help harden the defensive structural boundaries guarding human-centric system control.

## 📜 Code of Conduct

As a contributor to this repository, you agree to maintain absolute alignment with our core engineering objective: **Systemic Harmony through Deterministic Constraints**. We expect all participants to engage in rigorous, data-driven, and objective technical discourse.

## 🛠️ How to Contribute

### 1. Bug Reports & Feature Requests
* Search the existing issue tracker before opening a new issue to avoid redundancy.
* For feature requests, clearly document the theoretical necessity of your proposed change and how it impacts system-wide resource allocation or mathematical state-space evaluation.
* **Important:** If you discover a critical exploit that allows agents to bypass the `GeometricBehavioralSentinel` or escape the Docker Sandbox, **do not open a public issue**. Please follow the protocol outlined in our [SECURITY.md](./SECURITY.md) file.

### 2. Pull Request (PR) Guidelines
To maintain architectural integrity, all pull requests must strictly adhere to the following conditions:

* **Isolate Code Execution Layers:** Code updates must preserve the separation between the semantic evaluation layer (Strategic Ensemble), parametric tuning (VibranOpt), and deterministic infrastructure overrides (CSG-AA).
* **Maintain Non-LLM Invariants:** Security sentinels and rate-limiters must remain purely algorithmic and non-LLM based to avoid semantic adversarial manipulation or hallucinations.
* **Pass Hardening Test Suites:** Your branch must successfully pass all automated test suites outlined in the **Post-Warning Shot Standard (PWSS)** appendix without causing queue regressions or memory leaks.

## 🚀 Local Development Setup

1. Fork the repository and clone your fork locally:
   ```bash
   git clone https://github.com
   cd Cyber-Socialism-Governance-for-Autonomous-Agents
   ```
2. Setup your isolated container environment to prevent host machine contamination:
   ```bash
   docker build -t csg-aa-dev .
   docker run -p 8501:8501 csg-aa-dev
   ```
3. Create a feature branch using explicit semantic naming conventions (`feat/`, `fix/`, `refactor/`):
   ```bash
   git checkout -b feat/upgraded-sliding-window
   ```
4. Commit your changes with clear, structured messages, verify against `.gitignore`, and submit a Pull Request to the `main` branch.

*Thank you for dedicating your engineering skills to keeping decentralized intelligences safely bounded by human authority.*
