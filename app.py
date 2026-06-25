import streamlit as st


st.title("Convertisseur de devises")


rates = {
    "EUR": 1,
    "USD": 1.1,
    "JPY": 130
}


# Currencies select value initialization
if "from_currency" not in st.session_state:
    st.session_state.from_currency = "EUR"


if "to_currency" not in st.session_state:
    st.session_state.to_currency = "USD"


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


def invert_currencies():
    """
    Callback function that invert the two selected currencies
    """
    st.session_state.from_currency, st.session_state.to_currency = st.session_state.to_currency, st.session_state.from_currency,


if st.button("Convertir"):
    if amount > 0:
        if from_currency != to_currency:
            result = amount * rates[to_currency] / rates[from_currency]
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            st.error("Les devises doivent être différentes")
    else:
        st.error("Le montant doit être superieur a 0")


st.button(
    "Inverser les devises",
    on_click=invert_currencies
)
