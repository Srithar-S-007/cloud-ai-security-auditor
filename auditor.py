import json
import os
from openai import OpenAI

# Initialize the AI Client (Ensure you set your OPENAI_API_KEY environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_cloud_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_ai_remediation(issue, resource_type):
    prompt = f"""
    You are an expert Cloud Security AI Engineer. 
    Review the following cloud security issue and provide:
    1. A brief explanation of the security risk.
    2. The exact CLI command or Terraform snippet to fix it.
    
    Resource Type: {resource_type}
    Security Issue: {issue}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices.message.content

def run_security_audit():
    print("🛡️ Starting AI Cloud Security Audit...\n")
    config = load_cloud_config("mock_cloud_config.json")
    
    for element in config["infrastructure_elements"]:
        print(f"==================================================")
        print(f"🚨 [ALERT] Resource: {element['resource_id']} ({element['type']})")
        print(f"Severity: {element['severity']}")
        print(f"Issue: {element['issue']}")
        print(f"🤖 Fetching AI-Powered Remediation...\n")
        
        # Get response from AI
        try:
            remediation = get_ai_remediation(element['issue'], element['type'])
            print(remediation)
        except Exception as e:
            print(f"Could not fetch AI advice. Error: {e}")
        print(f"==================================================\n")

if __name__ == "__main__":
    run_security_audit()
