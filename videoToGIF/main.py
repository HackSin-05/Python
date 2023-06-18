from moviepy.editor import *

video = VideoFileClip(PATH_TO_FILE).subclip(00,5)

video.write_gif("test1.gif")