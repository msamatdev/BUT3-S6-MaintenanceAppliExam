import streamlit as st
from app_functions import (
    RATES,
    add_to_history,
    convert,
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
    list(RATES.keys()),
    key="from_currency"
)


to_currency = st.selectbox(
    "Vers :",
    list(RATES.keys()),
    key="to_currency"
)


if st.button("Convertir"):
    try:
        result = convert(amount, from_currency, to_currency, RATES)
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        add_to_history(Calculation(
            amount=amount,
            result=result,
            from_currency=from_currency,
            to_currency=to_currency
        ))
    except Exception as e:
        error_text = str(e)
        st.error(error_text)


st.button(
    "Inverser les devises",
    on_click=invert_currencies
)
