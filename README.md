Here's a `README.md` file for your Python bot project:

```markdown
# Forward Tag Remover Bot

**Forward Tag Remover Bot** is a Telegram bot that removes forward tags from messages. It works in private chats, groups, and channels, allowing users to forward messages without the "Forwarded from" tag.

## Features
- Removes forward tags from all types of messages.
- Supports media messages (except video notes and stickers).
- Can operate in private chats, groups, and channels.
- Developed using Python and the Pyrogram library.

## Installation

### Prerequisites
- Python 3.8 or higher
- A Telegram bot token (create one using [BotFather](https://t.me/BotFather))
- Your Telegram API ID and Hash (obtain them from [my.telegram.org](https://my.telegram.org))

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/forward-tag-remover.git
   cd forward-tag-remover
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `main.py` file with your bot token, API ID, and API hash:
   ```python
   bot = Client(
       "Remove FwdTag",
       bot_token = "Your-Bot-Token",
       api_id = Your-API-ID,
       api_hash = "Your-API-Hash"
   )
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Usage
1. Start the bot in Telegram by sending `/start`.
2. Forward messages to the bot to remove their forward tags.
3. Add the bot to groups or channels to enable tag removal for messages there.

## Bot Commands
- **/start**: Displays the bot's introduction message.

## Libraries Used
- [Pyrogram](https://docs.pyrogram.org/): For interacting with Telegram's API.
- `asyncio`: To handle asynchronous tasks.
- `os`: For operating system interactions.

## Contributing
Feel free to submit issues or pull requests if you'd like to contribute to the project.

## Creator
Developed by **[Abir XD Hackz](https://t.me/abir_xd_bio)**. For inquiries, visit the [developer's channel](https://t.me/abir_xd_bio).

---

**Disclaimer**: Use this bot responsibly and ensure compliance with Telegram's terms of service.
