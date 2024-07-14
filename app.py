import streamlit as st
import requests

# Função para obter taxas de câmbio
def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or data.get('result') != 'success':
        st.error("Erro ao obter taxas de câmbio")
        return None
    return data['conversion_rates'].get(target_currency)

# Interface do usuário usando Streamlit
def main():
    st.title("Conversor de Moeda")
    
    api_key = st.secrets["exchange_rate_api_key"]
    
    base_currency = st.selectbox("Moeda base", ["USD", "EUR", "BRL", "JPY", "GBP"])
    target_currency = st.selectbox("Moeda alvo", ["USD", "EUR", "BRL", "JPY", "GBP"])
    amount = st.number_input("Valor a converter", min_value=0.0, value=1.0)

    if st.button("Converter"):
        rate = get_exchange_rate(api_key, base_currency, target_currency)
        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
    # main
