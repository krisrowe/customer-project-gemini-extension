#!/usr/bin/env python3
import os
import sys
import datetime

def create_issue(issue_name):
    issue_dir = os.path.join("customer", "issues", issue_name)
    
    os.makedirs(os.path.join(issue_dir, "assets"), exist_ok=True)
    os.makedirs(os.path.join(issue_dir, "notes"), exist_ok=True)
    
    md_path = os.path.join(issue_dir, f"{issue_name}.md")
    if not os.path.exists(md_path):
        today = datetime.date.today().strftime("%Y-%m-%d")
        content = f"""# Issue: {issue_name}\n\n## Context\n<!-- Describe the background of the issue -->\n\n## Progress Logs\n### {today}\n- Issue initialized.\n\n## Findings\n<!-- Add research findings here -->\n\n## Next Steps\n- [ ] \n"""
        with open(md_path, 'w') as f:
            f.write(content)
        print(f"Issue folder created at {issue_dir}")
    else:
        print(f"Issue tracking file already exists at {md_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 create_issue.py <issue-name>")
        sys.exit(1)
    
    create_issue(sys.argv[1])
