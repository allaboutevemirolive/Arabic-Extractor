import docx2txt
from gtts import gTTS
import os

# Read the Microsoft Word document
text = docx2txt.process("document.docx", "utf-8")

# Convert the Arabic text to speech
tts = gTTS(text, lang='ar')

# Save the speech to an MP3 file
tts.save("output.mp3")

# Play the speech using the default media player on the system
os.system("start output.mp3")
