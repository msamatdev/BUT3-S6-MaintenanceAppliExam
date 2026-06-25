from dataclasses import dataclass
import streamlit as st
import dotenv
import os
import requests

dotenv.load_dotenv()


API_KEY = os.getenv('API_KEY')


RATES = requests.get(
    f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
).json()['conversion_rates']


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
    st.session_state.from_currency, st.session_state.to_currency = (
        st.session_state.to_currency, st.session_state.from_currency
    )
    
    
def convert(amount: float, from_currency: str, to_currency: str, rates: dict[str, float]):
    """
    Converts an amount from a currency to another
    """
    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à 0")
    
    if from_currency == to_currency:
        raise ValueError("Les devises doivent être différentes")
    
    if to_currency not in rates or from_currency not in rates:
        raise ValueError("Devise invalide")
    
    return amount * RATES[to_currency] / RATES[from_currency]


def init_conversion_history():
    st.session_state.history = []


def add_to_history(calculation: Calculation, history):
    history.append(calculation)

