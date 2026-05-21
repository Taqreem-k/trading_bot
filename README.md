# Binance Futures Testnet Trading Bot

A Python-based command-line interface (CLI) and web dashboard for executing trades on the Binance Futures Testnet (USDT-M). 

Built as an application task for Primetrade.ai.

##  Features
* **Core:** Place `MARKET` and `LIMIT` orders on USDT-M futures.
* **CLI:** Interactive terminal commands built with `Typer`, featuring robust input validation.
* **Bonus UI:** A lightweight web dashboard built with `Streamlit`.
* **Logging:** Centralized tracking of API requests, responses, and errors to `trading.log`.

##  Setup Instructions

**1. Clone the repository:**
```bash
git clone <your-repo-link>
cd trading_bot
```

**2. Environment & Dependencies:**
This project uses uv for fast dependency management (defined in pyproject.toml).

```bash
# If using uv:
uv sync

# Alternatively, if using standard pip:
pip install -r pyproject.toml 
```

**3. Configure API Keys**
Create a .env file in the root directory and add your Binance Testnet credentials:

```bash
BINANCE_TESTNET_API_KEY=your_api_key_here
BINANCE_TESTNET_SECRET_KEY=your_secret_key_here
```


##  Author

**Mohammad Taqreem Khan**