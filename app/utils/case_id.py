import uuid


def generate_case_id() -> str:
    """
    Generate a short, unique, human-shareable Case ID.

    Format: GLV-XXXXXXXX (8 uppercase hex characters).
    Not tied to any personal information.
    """

    unique_part = uuid.uuid4().hex[:8].upper()

    return f"GLV-{unique_part}"