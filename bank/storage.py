import json
from pathlib import Path


def save_accounts(account: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(account, indent=2))

def load_accounts(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text())

def find_account(accounts: list[dict], owner: str) -> dict | None:
    for account in accounts:
        if account["owner"] == owner:
            return account
    return None