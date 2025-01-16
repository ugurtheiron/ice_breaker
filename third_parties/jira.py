"""
parse_issues
                    "key": key,
                    "summary": summary,
                    "created": created,
                    "assignee": assignee,
                    "priority": priority,
                    "status": status,
                    "related_issues": rel_issues,
"""

import requests

def get_jira_issue_details(base_url, issue_key, auth_token):
    """
    Fetch Jira issue details and extract specific fields.
    
    Args:
        base_url (str): The base URL of the Jira instance (e.g., https://your-domain.atlassian.net).
        issue_key (str): The key of the Jira issue to retrieve (e.g., "PROJECT-123").
        auth_token (str): The Jira API token for authentication.
        
    Returns:
        dict: A dictionary containing the extracted issue details.
    """
    # API endpoint for fetching issue details
    url = f"{base_url}/rest/api/2/issue/{issue_key}"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Raise an exception if the request fails
    if response.status_code != 200:
        return {"error": f"Failed to fetch issue details. Status Code: {response.status_code}, Message: {response.text}"}
    
    # Parse the response JSON
    issue_data = response.json()
    
    # Extract desired fields
    key = issue_data.get("key", "N/A")
    fields = issue_data.get("fields", {})
    summary = fields.get("summary", "N/A")
    created = fields.get("created", "N/A")
    assignee = fields.get("assignee", {}).get("displayName", "Unassigned")
    priority = fields.get("priority", {}).get("name", "N/A")
    status = fields.get("status", {}).get("name", "N/A")
    rel_issues = [
        link.get("outwardIssue", {}).get("key", "N/A")
        for link in fields.get("issuelinks", [])
        if "outwardIssue" in link
    ]
    
    # Return extracted information as a dictionary
    return {
        "key": key,
        "summary": summary,
        "created": created,
        "assignee": assignee,
        "priority": priority,
        "status": status,
        "related_issues": rel_issues
    }