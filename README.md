This is a live chatbot for YouTube that allows the user to randomly select a player to be a barbarian, rogue, or wizard. It uses a Microsoft text-to-speech AI to speak the messages sent in the chat. The idea was inspired by DougDoug's Twitch streams and was developed in response to @TheJan's request on YouTube. Make sure to subscribe to him at https://www.youtube.com/@TheJan.

## Setup

1. Install python and vscode 
    Python can be downloaded at the microsoft store, make sure it is 3.11
    Vscode can also be found in the microsoft store. any version will work fine
2. Open the files in vscode
    In vscode, hit ctrl+k, then without letting go of ctrl, hit o and select the directory where you stored the code
3. Install packadges
    While on vscode hit shift+ctrl+~ and in the box that appears at the bottom type these:
    `pip install pytchat`
    `pip install azure.cognitiveservices.speech`
4. Get azure key and region
    Pase them in line 3 and 4 of speech.py respecively
5. Get the youtube code for the stream 
    it can be found in the url after "v=" and put it in line 5 of main.py and line 4 of choice.py replacing "VIDEO ID"
6. Set up the on screen text
    in obs, you can set the files "barbsays.txt", "wizsays.txt" and "roguesays.txt" as the source for your text for wherever you want what the person says to be
7. Run the file
    In the window that you opened in step 3, type:
    `python main.py` and you will get a message in that box saying "the bot is running"
8. Press the start button 
9. When you want to select a character, click the button to select a character. 
10. When you close the app, make sure to hit the trash can icon in the cmd tray you opened up on step 3.
