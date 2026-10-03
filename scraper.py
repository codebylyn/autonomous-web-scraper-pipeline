from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Technical Keywords Configuration by Domain
TECH_KEYWORDS = {
    "Help Desk / Tech Support": [
        "Technical Support Specialist", "Help Desk Technician", "IT Support Analyst",
        "Tier 1 Support", "Tier 2 Support", "Tier 3 Escalation", "Remote Desktop Support",
        "Desktop Support", "Microsoft Entra ID", "Microsoft 365 Administration",
        "Exchange Online", "Ticketing System", "Zendesk", "Freshservice", "ServiceNow",
        "Autotask", "Jira Service Management", "Hardware Troubleshooting",
        "Software Troubleshooting", "Windows 11 Deployment", "macOS Support",
        "VPN Configuration", "Network Connectivity Troubleshooting", "Printer/Peripheral Support",
        "Password Reset / Account Provisioning", "User Onboarding/Offboarding",
        "Remote Support Tools", "SLA Compliance", "First Call Resolution",
        "Incident Management", "Problem Management", "ITIL 4 Framework",
        "Mobile Device Management", "Multi-Factor Authentication", "Endpoint Protection",
        "Knowledge Base Documentation", "AI-Assisted Ticket Triage", "Zero Trust Basics",
        "Call/Chat Queue Management", "Customer Service Orientation"
    ],
    "MSP": [
        "Remote Monitoring and Management", "NinjaOne", "ConnectWise Automate",
        "ConnectWise Manage", "Datto RMM", "Datto BCDR", "Kaseya VSA", "Atera",
        "N-able", "Autotask PSA", "Patch Management", "Endpoint Detection and Response",
        "SentinelOne", "Huntress", "Webroot", "Backup and Disaster Recovery",
        "Multi-tenant Environment", "Multi-client Support", "Windows Server Administration",
        "Hyper-V", "VMware Virtualization", "Firewall Management", "Network Switch/Router Configuration",
        "Microsoft Entra ID / Intune", "Google Workspace Admin", "Client Onboarding",
        "Asset Lifecycle Management", "Vendor/License Management", "SOP Documentation",
        "Change Management", "Remote Site Deployment", "Business Continuity Planning",
        "SOC 2 / HIPAA Compliance", "Zero Trust Architecture", "IT Asset Inventory",
        "Proactive Maintenance Alerts"
    ],
    "DevOps": [
        "CI/CD Pipeline", "Jenkins", "GitHub Actions", "GitLab CI/CD", "CircleCI",
        "Docker", "Kubernetes", "Container Orchestration", "Terraform", "Ansible",
        "AWS CloudFormation", "Infrastructure as Code", "AWS", "Microsoft Azure",
        "Google Cloud Platform", "Site Reliability Engineering", "Monitoring & Observability",
        "Datadog", "Grafana", "Prometheus", "ELK Stack", "Git / Version Control",
        "Linux System Administration", "Bash Scripting", "YAML Configuration",
        "Load Balancing", "Microservices Architecture", "Configuration Management",
        "Blue-Green Deployment", "Artifact Repository", "Secrets Management",
        "SSL/TLS Certificate Management", "High Availability", "Disaster Recovery",
        "GitOps", "AI-Assisted Code Review", "Platform Engineering",
        "Zero Trust Networking", "Agile / Scrum", "Mean Time to Recovery"
    ],
    "Automation / Scripting": [
        "PowerShell Scripting", "Python Automation", "Bash/Shell Scripting",
        "API Integration", "REST API", "Zapier", "Make", "n8n", "Power Automate",
        "RPA", "UiPath", "Automation Anywhere", "Workflow Automation",
        "Task Scheduling", "Windows Task Scheduler", "Webhooks", "SQL Queries",
        "Database Automation", "Excel Macros", "Google Apps Script",
        "JSON/XML Data Handling", "Regular Expressions", "Process Documentation",
        "Error Handling / Logging", "ETL", "No-code/Low-code Tools", "Selenium",
        "AI Workflow Builders", "Chatbot Scripting", "Low-code AI Agents"
    ]
}

def analyze_text(text):
    """Scans scraped text for matching keywords across all domains."""
    results = {}
    for domain, keywords in TECH_KEYWORDS.items():
        matches = [kw for kw in keywords if kw.lower() in text.lower()]
        if matches:
            results[domain] = matches
    return results

def main():
    print(f"Scraper started at: {datetime.now()}")
    
    # Target URL (Replace with your actual target website)
    target_url = "https://example.com" 
    
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(target_url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Safe element extraction (Fixes the previous AttributeError)
    h1_element = soup.select_one("h1")
    if h1_element:
        title = h1_element.text.strip()
    else:
        title = "Title not found"
        print("Warning: Could not find the <h1> tag on the target page.")

    print(f"Extracted Page Title: {title}")

    # Example: Scan the entire page text for technical keywords
    page_text = soup.get_text()
    found_tech = analyze_text(page_text)

    print("\n--- Keyword Match Results ---")
    if found_tech:
        for domain, keywords in found_tech.items():
            print(f"[{domain}] Found {len(keywords)} matches: {keywords[:5]}...")
    else:
        print("No matching technical keywords found on this page.")

    print(f"\nScraper finished successfully at: {datetime.now()}")

if __name__ == "__main__":
    main()
