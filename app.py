import streamlit as st
from app_functions import (
    rates, 
    add_to_history, 
    invert_currencies, 
    Calculation,
    init_conversion_history
)


st.title("Convertisseur de devises")


# Initialization
if "from_currency" not in st.session_state:
    st.session_state.from_currency = "EUR"


if "to_currency" not in st.session_state:
    st.session_state.to_currency = "USD"
    
    
if "history" not in st.session_state:
    init_conversion_history()


# UI
amount = st.number_input("Montant :", min_value=0.0, format="%.2f")


from_currency = st.selectbox(
    "De :",
    list(rates.keys()),
    key="from_currency"
)


to_currency = st.selectbox(
    "Vers :",
    list(rates.keys()),
    key="to_currency"
)


if st.button("Convertir"):
    if amount > 0:
        if from_currency != to_currency:
            result = amount * rates[to_currency] / rates[from_currency]
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            add_to_history(Calculation(
                amount=amount,
                result=result,
                from_currency=from_currency,
                to_currency=to_currency
            ), st.session_state.history)
        else:
            st.error("Les devises doivent être différentes")
    else:
        st.error("Le montant doit être superieur a 0")


st.button(
    "Inverser les devises",
    on_click=invert_currencies
)
