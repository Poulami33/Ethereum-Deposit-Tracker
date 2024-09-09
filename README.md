# **Ether Tracker**

## **Overview**

Ether Tracker is a Python application that monitors Ethereum deposits on a specified contract and sends notifications via Telegram when new deposits are detected. The application uses the Web3.py library to interact with the Ethereum blockchain and the `python-telegram-bot` library to handle Telegram notifications.

## **Features**

* **Monitor Ethereum Deposits**: Tracks deposits on a specified Ethereum smart contract.  
* **Telegram Notifications**: Sends real-time notifications to a specified Telegram chat when a new deposit is detected.  
* **Asynchronous Processing**: Uses `asyncio` for efficient processing and notifications.

## **Setup**

### **Prerequisites**

* **Python 3.7+**: Ensure you have Python 3.7 or higher installed.  
* **Telegram Bot**: Create a bot on Telegram and obtain a bot token.  
* **Ethereum Node**: Access to an Ethereum node provider (e.g., Alchemy).

### **Installation**

**Clone the Repository**  
bash  
Copy code  
`git clone https://github.com/your-username/your-repository-name.git`  
`cd your-repository-name`

1. 

**Create a Virtual Environment** (optional but recommended)  
bash  
Copy code  
`python -m venv venv`  
`` source venv/bin/activate  # On Windows, use `venv\Scripts\activate` ``

2. 

**Install Dependencies**  
bash  
Copy code  
`pip install -r requirements.txt`

3. 

**Configure the Application**  
Update the configuration file `src/config.py` with your specific details:  
python  
Copy code  
`# Configuration details`  
`ALCHEMY_URL = "https://eth-mainnet.alchemyapi.io/v2/your-alchemy-api-key"`  
`BOT_TOKEN = "your-telegram-bot-token"`  
`CHAT_ID = "your-chat-id"`  
`CONTRACT_ADDRESS = "0x0000000000000000000000000000000000000000"  # Replace with your contract address`

4. Ensure the ABI file (`contract_abi.json`) is placed in the root directory of the project.

## **Usage**

To run the Ether Tracker application, execute the following command:

bash  
Copy code  
`python src/main.py`

The application will start fetching deposits from the Ethereum blockchain and sending notifications via Telegram. It will continue to run indefinitely, fetching deposits every 60 seconds.

## **Code Structure**

* **`src/config.py`**: Contains configuration details like API keys and contract address.  
* **`src/telegram_bot.py`**: Defines functions for sending notifications via Telegram.  
* **`src/web3_utils.py`**: Contains utility functions for interacting with the Ethereum blockchain.  
* **`src/main.py`**: The main script that runs the application, processes deposits, and sends notifications.  
* **`contract_abi.json`**: ABI file for the smart contract.

## **Examples**

### **Configuration**

Update the `src/config.py` with your actual Alchemy API key, Telegram bot token, chat ID, and contract address. For example:

python  
Copy code  
`ALCHEMY_URL = "https://eth-mainnet.alchemyapi.io/v2/your-alchemy-api-key"`  
`BOT_TOKEN = "your-telegram-bot-token"`  
`CHAT_ID = "your-chat-id"`  
`CONTRACT_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"`

### **Running the Application**

Execute the main script:

bash  
Copy code  
`python src/main.py`

You should see log messages indicating the detection of new deposits and corresponding Telegram notifications.

### **Handling Errors**

If you encounter errors related to sending Telegram messages or processing deposits, ensure:

* Your Telegram bot token and chat ID are correct.  
* Your Ethereum node provider URL is valid.  
* The ABI file is correctly formatted and matches the contract.

## **Troubleshooting**

* **Connection Issues**: Ensure your internet connection is stable and your API keys are correct.  
* **ABI Mismatch**: Verify that the ABI file is correct and matches the smart contract.  
* **Telegram Errors**: Check if the Telegram bot token and chat ID are valid.

