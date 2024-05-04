import subprocess
from rpocket import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_add_credit_card():
    # Testa l'aggiunta di una carta di credito
    result = subprocess.run(
        [
            "python",
            "rpocket/cli.py",
            "add-credit-card",
            "1234567812345678",
            "2024-12-31",
            "Mario Rossi",
            "123",
            "Carta di credito principale",
        ]
    )
    assert result.returncode == 0


def test_add_subscription():
    # Testa l'aggiunta di un abbonamento
    result = subprocess.run(
        [
            "python",
            "rpocket/cli.py",
            "add-subscription",
            "Netflix",
            "1",  # Sostituisci con l'ID della carta di credito aggiunta nei test precedenti
            "2024-12-31",
            "Abbonamento mensile",
        ]
    )
    assert result.returncode == 0


def test_list_subscriptions():
    # Testa la visualizzazione degli abbonamenti
    result = subprocess.run(
        ["python", "rpocket/cli.py", "list-subscriptions"],
        capture_output=True,
        text=True,
    )
    assert "Netflix" in result.stdout
