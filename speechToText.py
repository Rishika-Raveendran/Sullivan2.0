import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import clip

num_seconds_video= 52*60

dictionary={}
for i in range(len(l)-1):
    clip("videorl.mp4", l[i]-2*(l[i]!=0), l[i+1], targetname="chunks/cut{}.mp4".format(i+1))
    clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i+1)) 
    clip.audio.write_audiofile(r"converted/converted{}.wav".format(i+1))
    r = sr.Recognizer()
    audio = sr.AudioFile("converted/converted{}.wav".format(i+1))
    with audio as source:
      r.adjust_for_ambient_noise(source)  
      audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    dictionary['chunk{}'.format(i+1)]=result


l_chunks=[dictionary['chunk{}'.format(i+1)] for i in range(len(dictionary))]
text='\n'.join(l_chunks)

with open('sullivan20.txt',mode ='w') as file: 

   file.write("\n") 
   file.write(text) 
