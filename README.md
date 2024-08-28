
# Ravan Voice Bot

Ravan Voice Bot is a personal assistant voice bot for PC that allows users to interact with their computer using voice commands. The bot can perform tasks such as playing music, telling the time and date, managing Bluetooth settings, opening applications, and more.

## System Requirements

To run the Ravan Voice Bot, your system must meet the following requirements:

- **Operating System**: Windows 10 or later
- **Python Version**: Python 3.x
- **Internet Connection**: Required for certain functionalities like playing songs from YouTube.

## Modules to Install

Before running the bot, you need to install the following Python modules:

- **`speech_recognition`**: For capturing and recognizing voice commands.
- **`pyttsx3`**: For text-to-speech conversion.
- **`pywhatkit`**: For playing songs on YouTube.
- **`pyautogui`**: For controlling mouse and keyboard actions.
- **`keyboard`**: For handling keyboard events.
- **`subprocess`**: For running system commands.
- **`ctypes`**: For interacting with Windows-specific features.
- **`os`**: For interacting with the operating system.
- **`wmi`**: For accessing system information.
- **`psutil`**: For retrieving information on system utilization (CPU, memory, etc.).
- **`winreg`**: For working with the Windows Registry.
- **`requests`**: For making HTTP requests.
- **`datetime`**: For working with dates and times.
- **`speedtest-cli`**: For testing internet speed.
- **`getpass`**: For securely handling passwords.
- **`csv`**: For working with CSV files.
- **`time`**: For time-related functions.
- **`pygetwindow`**: For controlling windows on your desktop.

## Installation

Follow these steps to set up the Ravan Voice Bot on your system:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/ravan-voice-bot.git
    ```
   
2. **Navigate to the Project Directory**:
    ```bash
    cd ravan-voice-bot
    ```

3. **Install the Required Modules**:
    You can install all the required modules by running the following command:
    ```bash
    pip install speechrecognition pyttsx3 pywhatkit pyautogui keyboard wmi psutil speedtest-cli pygetwindow requests
    ```

4. **Run the Bot**:
    After installing all the required modules, you can start the bot by running:
    ```bash
    python main.py
    ```

## Usage

Once the bot is running, you can interact with it using voice commands to play music, check the time and date, manage Bluetooth settings, open applications, and more.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License.

