# AI-Driven Cloud Security Auditor 🛡️🤖

A Python-based DevSecOps tool that scans cloud configuration data, identifies dangerous security vulnerabilities, and uses AI (LLMs) to automatically generate remediation guidance and infrastructure fixes.

## Key Features
- **Config Scanning:** Evaluates infrastructure data for compliance risks (e.g., Open SSH ports, missing MFA).
- **AI Triage:** Integrates with LLM APIs to interpret raw logs and evaluate severity context.
- **Auto-Remediation:** Generates copy-pasteable CLI commands or code adjustments to instantly close security gaps.

## How It Works
1. The script parses `mock_cloud_config.json` representing current cloud architecture states.
2. Flagged issues are passed to an AI model specializing in cloud defense.
3. The AI outputs exact mitigation steps for security engineering teams.

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Export your API Key: `export OPENAI_API_KEY="your-key-here"`
4. Run the tool: `python auditor.py`
