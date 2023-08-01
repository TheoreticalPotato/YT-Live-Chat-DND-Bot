import azure.cognitiveservices.speech as speechsdk

speech_key = "SPEECH KEY"
service_region = "REGION"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

def barbSpeak(text):
    speech_config.speech_synthesis_voice_name = "en-US-DavisNeural"
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    result = speech_synthesizer.speak_text_async(text).get()

def wizSpeak(text):
    speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    result = speech_synthesizer.speak_text_async(text).get()

def rogueSpeak(text):
    speech_config.speech_synthesis_voice_name = "en-US-TonyNeural"
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    result = speech_synthesizer.speak_text_async(text).get()   