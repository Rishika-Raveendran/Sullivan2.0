from gtts import gTTS

import os

mytext = 'Good evening. Sullivan 2.0 on this end'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("sullivan.mp3")

os.system("mpg321 sullivan.mp3")