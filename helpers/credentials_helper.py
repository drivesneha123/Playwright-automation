def get_credentials(scenario, creds_json):
    """
    Returns credentials based on login tag in scenario or feature.
    Raises ValueError if not found.
    """
    all_tags = scenario.tags + getattr(scenario.feature, "tags", [])
    for tag in all_tags:
        if tag.startswith("login_"):
            role = tag.replace("login_", "")
            if role in creds_json:
                source = (
                    "Scenario Tag" if tag in scenario.tags else "Feature Tag Fallback"
                )
                return creds_json[role], source, role
    raise ValueError(
        "No login tag found on scenario or feature, or role missing in credentials.json"
    )
