# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:00:17 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

from moviepy.editor import *

clip = VideoFileClip("2.mp4").rotate(180)
clip.ipython_display(width=200)