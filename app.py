import streamlit as st
from bot.client import BinanceFuturesClient

st.set_page_config(page_title="Binance Bot", page_icon="📈")

st.title("Binance Futures Trading Bot")

# Initialize client
try:
    client = BinanceFuturesClient()
except Exception as e:
    st.error(f"Failed to initialize client: {e}")
    st.stop()

with st.form("order_form"):
    st.subheader("Place New Order")
    
    col1, col2 = st.columns(2)
    with col1:
        symbol = st.text_input("Symbol (e.g., BTCUSDT)", value="BTCUSDT")
        side = st.selectbox("Side", ["BUY", "SELL"])
    
    with col2:
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        quantity = st.number_input("Quantity", min_value=0.001, format="%.3f")
        
    price = st.number_input("Price (Required for LIMIT)", min_value=0.0, format="%.2f")
    
    submit = st.form_submit_button("Submit Order")

if submit:
    if order_type == "LIMIT" and price <= 0:
        st.warning("⚠️ Please provide a valid price for LIMIT orders.")
    else:
        with st.spinner("Sending order to Binance..."):
            try:
                if order_type == "MARKET":
                    response = client.place_market_order(symbol.upper(), side, quantity)
                else:
                    response = client.place_limit_order(symbol.upper(), side, quantity, price)
                
                st.success("✅ Order Successful!")
                st.json({
                    "Order ID": response.get("orderId"),
                    "Status": response.get("status"),
                    "Executed Qty": response.get("executedQty"),
                    "Avg Price": response.get("avgPrice")
                })
            except Exception as e:
                st.error(f"❌ Execution Failed: {str(e)}")