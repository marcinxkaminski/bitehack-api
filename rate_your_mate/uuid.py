from uuid import uuid4


def create() -> str:
    return str(uuid4())
