# import required module
from playsound import playsound
from gtts import gTTS

  
def text_to_audio(content):
    # Enter the text in string format which you want to convert to audio
    mytext = content

    # Specify the language in which you want your audio
    language = "en"

    # Create an instance of gTTS class
    myobj = gTTS(text=mytext, lang=language, slow=False,tld='co.in')

    # Method to create your audio file in mp3 format
    myobj.save("welcome.mp3")
    print("Audio Saved")

    # This will play your audio file
    # for playing note.wav file
    playsound('welcome.mp3')
    print('playing sound using  playsound')

text=str(input("Enter: "))
text_to_audio(text)