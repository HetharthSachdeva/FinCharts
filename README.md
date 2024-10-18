# Financial Dashboard

This project is a simple financial dashboard built with Streamlit, yfinance, and Plotly. It allows users to visualize stock trends, including price movements and trading volumes, for any publicly traded company.

## Features

- Interactive date range selection
- Stock symbol input
- Real-time stock data fetching
- Candlestick chart for stock price visualization
- Trading volume chart
- Key statistics display (Current Price, Market Cap, P/E Ratio, etc.)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.7 or later
- You have a Windows/Linux/Mac machine

## Installing Financial Dashboard

To install the Financial Dashboard, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/financial-dashboard.git
   cd financial-dashboard
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Using Financial Dashboard

To use the Financial Dashboard, follow these steps:

1. Ensure your virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501).

4. Use the sidebar to select a date range and enter a stock symbol.

5. Explore the interactive charts and statistics displayed on the dashboard.

## Contributing to Financial Dashboard

To contribute to Financial Dashboard, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).
