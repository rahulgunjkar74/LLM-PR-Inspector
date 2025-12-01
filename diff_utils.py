def extract_changed_lines(patch):
    """
    Returns list of (position, line_text) for added lines starting with '+'
    """
    changed = []
    lines = patch.split("\n")
    position = 0

    for line in lines:
        if line.startswith("@@"):
            position = 0
        else:
            position += 1

        if line.startswith("+") and not line.startswith("+++"):
            changed.append((position, line[1:].strip()))

    return changed
