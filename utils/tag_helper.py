def get_tag_value(context, key):
    """Get the value of a tag like @username=abc"""
    prefix = f"{key}="
    for tag in context.tags:
        if tag.startswith(prefix):
            return tag.split("=", 1)[1]
    return None
