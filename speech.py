from gtts import gTTS

import os 

dummy_text = "My name is aditya"

language = 'en'

object = gTTS(text=dummy_text, lang=language, slow=False)

object.save("welcome.mp3")

os.system("mpg321 welcome.mp3")
