from dataclasses import dataclass
import streamlit as st


rates = { # TODO: update with API call
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130,
    "GBP": 0.86
}


@dataclass
class Calculation:
    from_currency: str
    to_currency: str
    amount: float
    result: float


def invert_currencies():
    """
    Callback function that invert the two selected currencies
    """
    st.session_state.from_currency, st.session_state.to_currency = st.session_state.to_currency, st.session_state.from_currency,


def init_conversion_history():
    st.session_state.history = []


def add_to_history(calculation: Calculation):
    st.session_state.history.append(calculation)
