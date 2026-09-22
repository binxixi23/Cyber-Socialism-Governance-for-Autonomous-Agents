# Security Policy: Vulnerability Disclosure Protocol

Because `CSG-AA` operates as a hard-coded structural defense mechanism to stop multi-agent collusion, adversarial breakouts, and token-drain exploits, the security of this codebase is of paramount importance. 

We take all architectural vulnerabilities seriously and mandate a **Responsible and Coordinated Disclosure Process** to protect environments deploying this framework.

## 🛡️ Supported Versions

Only the latest release commit on the `main` branch of this repository is actively supported and monitored for security hardening.

| Version | Supported |
| :--- | :--- |
| v1.x.x (Active Main) | ❤️ Yes |
| All prior development tags | ❌ No |

## ⚠️ Reporting a Vulnerability

If you discover a systemic flaw, an exploit capable of tricking the Shannon Entropy metrics, an acrostic bypass vector, or a Docker hypervisor breakout scenario, **please do not publish your findings publicly on social media or GitHub Issues.**

Please report all vulnerabilities securely via the following protocol:

1. **Submit a Private Report:** Reach out to the maintainer (`binxixi23`) via secure channels, or utilize the GitHub **Private Vulnerability Reporting** feature directly on the repository dashboard.
2. **Include Technical Telemetry:** Provide a detailed description of the exploit vector, including:
   * The exact agent payload or command logs used to execute the bypass.
   * Telemetry logs demonstrating how the spatial drift distance calculation failed to exceed the threshold (d ≤ θ).
   * Step-by-step reproduction code or shell configurations.

## 🕒 Our Disclosure Process

Upon receiving a valid vulnerability report, the maintainer will:

* Acknowledge receipt of the report within **48 hours**.
* Triage and validate the exploit internally using specialized local Red-Teaming testing environments.
* Work collaboratively on a critical patch in a private security fork.
* Automatically issue a hard-hardened release update to the public `main` tree.
* Provide full credit and attribution to the security researcher in the release documentation (unless anonymity is requested).

*We ask that you maintain absolute confidentiality regarding the exploit until a secure patch is pushed to prevent malicious orchestration actors from weaponizing the vulnerability.*
