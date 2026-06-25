import pytest
import app_functions
from app_functions import add_to_history, init_conversion_history, Calculation, convert

@pytest.fixture
def RATES():
    """Taux de change de référence (EUR comme base)."""
    return {
        "EUR": 1.0,
        "USD": 1.1,
        "GBP": 0.85,
    }

@pytest.fixture(autouse=True)
def fake_session_state(monkeypatch):
    """Remplace st.session_state par un faux objet propre avant chaque test."""
    class FakeSessionState:
        pass
    monkeypatch.setattr(app_functions.st, "session_state", FakeSessionState())


def test_init_conversion_history():
    init_conversion_history()
    assert app_functions.st.session_state.history == []   # init crée une liste VIDE


def test_add_to_history():
    init_conversion_history()
    val = Calculation(
        amount=10.0,
        result=11.0,
        from_currency='USD',
        to_currency='EUR',
    )
    add_to_history(val, app_functions.st.session_state.history)
    assert len(app_functions.st.session_state.history) == 1
    assert app_functions.st.session_state.history[0] == val   # index 0, pas 1

    def test_convert_basic(RATES):
        # 100 EUR -> USD : 100 * 1.1 / 1.0 = 110
        assert convert(100.0, "EUR", "USD", RATES) == pytest.approx(110.0)

def test_convert_amount_zero_raises(RATES):
    with pytest.raises(ValueError, match="supérieur à 0"):
        convert(0.0, "EUR", "USD", RATES)


def test_convert_amount_negative_raises(RATES):
    with pytest.raises(ValueError, match="supérieur à 0"):
        convert(-5.0, "EUR", "USD", RATES)


def test_convert_same_currency_raises(RATES):
    with pytest.raises(ValueError, match="différentes"):
        convert(100.0, "EUR", "EUR", RATES)


def test_convert_unknown_from_currency_raises(RATES):
    with pytest.raises(ValueError, match="invalide"):
        convert(100.0, "XXX", "USD", RATES)


def test_convert_unknown_to_currency_raises(RATES):
    with pytest.raises(ValueError, match="invalide"):
        convert(100.0, "EUR", "XXX", RATES)