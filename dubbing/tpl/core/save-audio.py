from moviepy.audio.io.AudioFileClip import AudioFileClip
import os

# Save video.
node_in_audio: AudioFileClip = in_audio
node_in_path = 'in_path'
if not os.path.exists(os.path.dirname(node_in_path)):
    os.makedirs(os.path.dirname(node_in_path))
node_in_audio.write_audiofile(node_in_path)
