from moviepy.editor import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

#clip = VideoFileClip("90’s Hip Hop Music Video in 10 Seconds #shorts.mp4")

#clip.write_gif("90’s Hip Hop Music Video in 10 Seconds #shorts.gif")

#clip.write_gif("secondgif.gif",fps=10)


clip = VideoFileClip("90’s Hip Hop Music Video in 10 Seconds #shorts.mp4").subclip(1,3 )

clip2 = VideoFileClip("90’s Hip Hop Music Video in 10 Seconds #shorts.mp4").subclip(2,6)

final_clip = concatenate_videoclips([clip, clip2])

final_clip.write_videofile("output_1.mp4")
