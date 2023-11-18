# YouTube Live Chatbot: Adventure Role Selector

Welcome to the repository of the YouTube Live Chatbot: Adventure Role Selector! This live chatbot project, inspired by DougDoug's Twitch streams and developed in response to @TheJan's request on YouTube, enables random role assignment (barbarian, rogue, or wizard) to players in a YouTube chat. Coupled with a Microsoft text-to-speech AI, the chatbot also voices out the messages sent in the chat.

You can experience this amazing feature firsthand by subscribing to @TheJan at [https://www.youtube.com/@TheJan](https://www.youtube.com/@TheJan).

## Setup and Configuration

Follow these steps to install and configure the YouTube Live Chatbot on your system.

### Pre-requisites
- Python 3.11: You can download it from the Microsoft Store [here](https://www.microsoft.com/store/apps/python)
- Visual Studio Code (VS Code): Any version will suffice, available for download from the Microsoft Store.

### Installation
1. **Open project in VS Code**: Open VS Code, press `ctrl+k`, keep holding `ctrl`, then press `o`. Navigate and select the project directory.

2. **Install necessary packages**: Open a terminal in VS Code by pressing `shift+ctrl+~`. In the terminal that opens at the bottom, type and execute these commands:
    ```
    pip install pytchat
    pip install azure.cognitiveservices.speech
    ```

3. **Obtain Azure Key and Region**: Once obtained, paste them in line 3 and 4 of `speech.py`, respectively.

4. **Get the YouTube Stream code**: This code can be found in the URL after "v=". Put this code in line 5 of `main.py` and line 4 of `choice.py`, replacing "VIDEO ID".

5. **Setup On-Screen Text**: If you're using OBS, setup the on-screen text by using the files "barbsays.txt", "wizsays.txt", and "roguesays.txt" as the source for the text.

### Running the Bot
1. In the same terminal you opened earlier, type: `python main.py`. You will receive a message saying "the bot is running".

2. Press the start button to initialize the bot.

3. When you want to select a character, click the button to make a selection.

4. Once you're done, make sure to close the app properly. Click on the trash can icon in the terminal to exit.

Enjoy your journey with the YouTube Live Chatbot: Adventure Role Selector! Feel free to contribute or report any issues you encounter.

Happy adventuring!

## License

This project is licensed under the terms of the MIT License.

```
MIT License

Copyright (c) 2023 YouTube Live Chatbot: Adventure Role Selector

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

For more details, please refer to the [MIT License](https://opensource.org/licenses/MIT).
