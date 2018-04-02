# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:27:09 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

from moviepy.editor import *

video = VideoFileClip("2.mp4").subclip(50,60)
# Make the text
text_clip = ( TextClip("Welcome to LingShui", fontsize = 70, color = 'white').set_position('center').set_duration(10) )

result = CompositeVideoClip([video, text_clip])
result.write_videofile("2.webm", fps=25)