Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Demo/Testnet. The application supports both BUY and SELL orders, includes input validation, structured logging, and robust error handling.

Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL sides
* Command-line interface using argparse
* Input validation
* Logging of requests, responses, and errors
* Error handling for API, validation, and network failures
* Modular project structure

## Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore


Prerequisites

* Python 3.10+
* Binance Demo/Testnet Account
* Binance Demo/Testnet API Key and Secret

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd TradingBotAssignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root directory:

```env
API_KEY=MY_API_KEY
API_SECRET=MY_API_SECRET
```

## Running the Application

### MARKET BUY Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### MARKET SELL Order
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001

LIMIT BUY Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 65000

LIMIT SELL Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 68000

Sample Outputs
MARKET Order
<img width="534" height="366" alt="image" src="https://github.com/user-attachments/assets/40a0e7de-e4d9-433f-83ee-35d3304de1f9" />
LIMIT Order
<img width="528" height="375" alt="image" src="https://github.com/user-attachments/assets/8ec0399f-f39a-425a-b35e-52a49c31985a" />
Logs
All requests, responses, and errors are logged to:
logs/trading.log
Example log entries:
INFO - MARKET ORDER REQUEST
INFO - MARKET ORDER RESPONSE
ERROR - Binance API Error

Validation Examples
Invalid Side
python cli.py --symbol BTCUSDT --side ABC --type MARKET --quantity 0.001
Invalid Quantity
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity -1
Missing Price for LIMIT Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001

Error Handling

The application handles:

* Invalid user inputs
* Binance API exceptions
* Network failures
* Unexpected runtime errors

Assumptions
* User has valid Binance Demo/Testnet API credentials.
* User has sufficient demo balance available.
* Supported order types are MARKET and LIMIT only.
* Supported order sides are BUY and SELL only.

Dependencies
python-binance
python-dotenv
