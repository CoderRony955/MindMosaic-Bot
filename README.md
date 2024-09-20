# MindMosaic | AI Facts Discord Bot
![Screenshot of the bot](https://github.com/CoderRony955/MindMosaic-Bot/blob/master/bot-imgs/MindMosaic.jpg)
A simple Discord bot that shares random new AI facts every time it's called. This bot provides users with up-to-date insights about the latest AI developments, advancements, and trends.

## Features

- Shares **random AI facts** on demand.
- Includes **cutting-edge AI advancements** in fields such as generative AI, natural language processing (NLP), automation, healthcare, and ethical AI.
- Pulls from **up-to-date sources** to ensure that users get the latest AI news and breakthroughs.

## How It Works

The bot listens for specific commands in your Discord server and responds with a random AI fact. It can be integrated easily into any Discord channel to provide informative and engaging AI content.

### Commands

- `!aifact`: Posts a random fact about recent advancements in AI.
- `!help`: Displays a list of available commands and usage instructions.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CoderRony955/ai-facts-bot.git
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Discord bot**:
    - Create a Discord bot through the [Discord Developer Portal](https://discord.com/developers/applications).
    - Copy the bot token and add it to a `.env` file or as an environment variable:
      ```bash
      DISCORD_TOKEN=your_bot_token_here
      ```

4. **Run the bot**:
    ```bash
    python bot.py
    ```

## Configuration

Make sure you have a valid `DISCORD_TOKEN` environment variable set before running the bot.

I added a AI random facts in JSON file you can also add more AI facts by editing the `facts.json` file, which contains the list of random AI facts.

```json
{
  "facts": [
    "Generative AI is being used to enhance creative industries, from art to music production.",
    "The U.S. Copyright Office currently does not recognize AI-generated works as copyrightable.",
    "AI-powered healthcare solutions are improving early diagnostics and treatment outcomes."
 ]
}
```

## Thanks for visiting
Happy programming:)💖


## 📲 Get in Touch

<a href="https://www.instagram.com/__raunakk__/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="instagram logo"  />
  </a>
<a href="https://discord.gg/SK9k6mdzvP" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="discord logo"  />
  </a>


