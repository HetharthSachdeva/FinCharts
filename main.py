import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date, timedelta

st.set_page_config(page_title="Financial Dashboard", layout="wide")
st.title("Financial Dashboard")
st.sidebar.header("Settings")

start_date = st.sidebar.date_input("Start Date", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", date.today())
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, GOOGL)", value="AAPL")

@st.cache_data
def load_data(symbol, start, end):
    data = yf.download(symbol, start=start, end=end)
    return data

data = load_data(symbol, start_date, end_date)

if not data.empty:
    try:
        # Fetch stock data
        stock = yf.Ticker(symbol)
        info = stock.info
        
        # Check if we actually got any data
        if not info:
            st.error(f"Unable to fetch data for {symbol}. Please check if the ticker symbol is correct.")
            st.stop()
        
        # Display financial metrics
        st.header(f"{info['longName']} ({symbol})")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"${info['currentPrice']:.2f}")
        col2.metric("Market Cap", f"${info['marketCap']:,.0f}")
        col3.metric("52 Week High", f"${info['fiftyTwoWeekHigh']:.2f}")

        fig = go.Figure(data=[go.Candlestick(x=data.index,
                            open=data['Open'],
                            high=data['High'],
                            low=data['Low'],
                            close=data['Close'])])

        fig.update_layout(title=f"{symbol} Stock Price", xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)

        volume_fig = go.Figure(data=[go.Bar(x=data.index, y=data['Volume'])])
        volume_fig.update_layout(title=f"{symbol} Trading Volume", xaxis_title="Date", yaxis_title="Volume")
        st.plotly_chart(volume_fig, use_container_width=True)

        st.header("Key Statistics")
        col1, col2, col3 = st.columns(3)
        col1.metric("P/E Ratio", f"{info['trailingPE']:.2f}")
        col2.metric("Dividend Yield", f"{info['dividendYield']*100:.2f}%" if info['dividendYield'] else "N/A")
        col3.metric("52 Week Low", f"${info['fiftyTwoWeekLow']:.2f}")

        # Helper function to safely get info
        def safe_get(dict, key, default="N/A"):
            return f"{dict.get(key, default):.2f}" if dict.get(key) is not None else default

        col1.metric("P/E Ratio", safe_get(info, 'trailingPE'))
        col2.metric("Market Cap", f"${info.get('marketCap', 'N/A'):,}")
        col3.metric("52 Week High", safe_get(info, 'fiftyTwoWeekHigh'))

    except Exception as e:
        st.error(f"An error occurred while fetching data for {symbol}: {str(e)}")
        st.stop()

else:
    st.error("No data available for the selected stock symbol and date range.")

st.markdown("---")
st.markdown("Data provided by Yahoo Finance")
