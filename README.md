# Twitter Complaint Bot

The **Twitter Complaint Bot** is an automated Python script that checks internet speed using [Speedtest.net](https://www.speedtest.net) and tweets a complaint to the internet service provider on [Twitter](https://x.com). The bot logs in to Twitter and tweets about the observed internet speed, comparing it with the promised speed from the ISP.

## Features

- **Automated Speed Test:** The bot checks download and upload speeds using Speedtest.net.
- **Automated Login and Tweeting:** Logs into Twitter and posts a complaint if the internet speed is lower than expected.
- **Customizable Speed Thresholds:** You can adjust the promised download and upload speed limits to trigger the complaint.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Chrome WebDriver (compatible with your Chrome browser version)

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/Aditya1066/tinder-swiping-bot.git
   ```
2. **Navigate to the Project Directory:**
   ```
   cd twitter-complaint-bot
   ```
3. **Create and Activate a Virtual Environment:**
   ```
   python -m venv .venv
   .venv\Scripts\activate   # For Windows
   source .venv/bin/activate  # For macOS/Linux
   ```
4. **Install Required Packages:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Edit the Bot Credentials:**
   Update your email, username, and password in the `bot` code.

2. **Run the Script:**
   ```
   python Main.py
   ```

## Configuration

- **Internet Speed Threshold:** You can set the expected download and upload speeds within the script to trigger complaints accordingly.

## Known Issues

- The bot may fail if the Twitter login flow changes. You may need to update the code to reflect these changes.

## Disclaimer

This project is for educational purposes only. Automated interactions with Twitter may violate their terms of service. Use it responsibly.
