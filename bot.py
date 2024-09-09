import requests

# Replace with your Telegram bot token
bot_token = "7331501704:AAHlKQSwSZGiT8LpdhsVKW5StLuFmAgDFlM"
response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
data = response.json()

# Print the chat ID
if data['result']:
    print(data['result'][0]['message']['chat']['id'])
else:
    print("No new messages received by the bot.")