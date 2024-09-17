from web3 import Web3
import json
import logging
import time
from telegram import Bot
from telegram.ext import Updater
import asyncio

# Configuration
alchemy_url = ""  # Alchemy API URL for Ethereum mainnet
bot_token = ""  # Telegram bot token
chat_id = ""  # Telegram chat ID to receive notifications
contract_address = ""  # Ethereum contract address to monitor

# Setup
web3 = Web3(Web3.HTTPProvider(alchemy_url))  # Initialize Web3 connection
bot = Bot(token=bot_token)  # Initialize Telegram bot
logging.basicConfig(level=logging.INFO)  # Set up logging configuration

# Load the ABI (Application Binary Interface) from file
with open('./contract_abi.json', 'r') as file:
    abi = json.load(file)  # Load ABI JSON data

# Initialize contract object
contract = web3.eth.contract(address=contract_address, abi=abi)

async def send_telegram_notification(message):
    """
    Send a notification message to a specified Telegram chat.
    
    Args:
        message (str): The message text to send.
    """
    try:
        await bot.send_message(chat_id=chat_id, text=message)  # Send message
        await asyncio.sleep(1)  # Small delay to avoid rate limiting
    except Exception as e:
        logging.error(f"Error sending Telegram message: {e}")  # Log error if message fails

async def process_deposit(deposit):
    """
    Process a single deposit event log from the blockchain.
    
    Args:
        deposit (dict): The deposit event log data.
    """
    try:
        tx_hash = deposit['transactionHash'].hex()  # Get transaction hash
        receipt = web3.eth.get_transaction_receipt(tx_hash)  # Get transaction receipt
        logs = contract.events.DepositEvent().process_receipt(receipt)  # Process event logs from receipt
        
        for log in logs:
            # Extract relevant data from log
            pubkey = log.args.pubkey.hex()
            amount = web3.from_wei(int.from_bytes(log.args.amount, 'big'), 'ether')
            timestamp = web3.eth.get_block(receipt['blockNumber'])['timestamp']
            
            # Log deposit details
            logging.info(f"Transaction Hash: {tx_hash}, Pubkey: {pubkey}, Amount: {amount} ETH, Timestamp: {timestamp}")
            
            # Send notification about the new deposit
            await send_telegram_notification(f"New deposit detected: Transaction Hash: {tx_hash}, Pubkey: {pubkey}, Amount: {amount} ETH")
    except Exception as e:
        logging.error(f"Error processing deposit: {e}", exc_info=True)  # Log error if processing fails

async def fetch_deposits():
    """
    Fetch and process deposit events from recent blocks.
    """
    try:
        latest_block = web3.eth.get_block('latest')  # Get latest block
        from_block = max(0, latest_block['number'] - 100)  # Define block range for fetching logs
        deposits = web3.eth.get_logs({
            "fromBlock": from_block,
            "toBlock": latest_block['number'],
            "address": contract_address  # Filter logs by contract address
        })
        
        for deposit in deposits:
            await process_deposit(deposit)  # Process each deposit
    except Exception as e:
        logging.error(f"Error fetching deposits: {e}", exc_info=True)  # Log error if fetching fails

async def main():
    """
    Main function to continuously fetch and process deposit events.
    """
    while True:
        await fetch_deposits()  # Fetch and process deposits
        await asyncio.sleep(60)  # Delay between fetches to avoid excessive API calls

if __name__ == "__main__":
    asyncio.run(main())  # Run the main function in the asyncio event loop
