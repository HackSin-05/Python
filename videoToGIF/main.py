from moviepy.editor import *

video = VideoFileClip(PATH_TO_FILE).subclip(00,5) # Replace PATH_TO_FILE with your video file.

video.write_gif("test1.gif") # Replace "test1.gif" with your desire gif file name.
