from bank.storage import save_accounts, load_accounts, find_account

def test_save_accounts(tmp_path):
    path = tmp_path / "accounts.json"
    save_accounts([{"owner": "Ada", "balance": 100}], path)
    assert path.exists()

def test_load_accounts(tmp_path):
    path = tmp_path / "accounts.json"
    original = ([{"owner": "Ada", "balance": 100}])
    save_accounts(original, path)
    assert load_accounts(path) == original

def test_load_accounts_missing_file_returns_empty(tmp_path):
    assert load_accounts(tmp_path / "nope.json") == []


def test_find_account():
    accounts = [{"owner": "Ada", "balance": 100}]
    assert find_account(accounts, "Ada") == {"owner": "Ada", "balance": 100}
    assert find_account(accounts, "Zed") is None