'''Downloa YouTube audio and video using youtube-dl'''
import module_youtube_extract


# specify desired youtube URL
URL_I = 'https://www.youtube.com/watch?v=Tx-qXGGlF6k'


# specify desired file name
FILE_NAME_I = '%(title)s.%(ext)s'


# Specify desireable download formats if Function 5 is executed.
# The list of available formats can be found from the output of Function 2 in the variable available_formats
#VIDEO_QUALITY_CODE_I = '22'
#AUDIO_QUALITY_CODE_I = '140'
VIDEO_QUALITY_CODE_I = '137'
AUDIO_QUALITY_CODE_I = '140'


# Function 1
# get URL meta data

meta_data = module_youtube_extract.meta_data(URL=URL_I,FILE_NAME='vide_x_meta_data', TXT_CLEAN=True, TXT=False, JSON=False, DOWNLOAD=False)


# Function 2
# get all available downloadble formats

available_formats = module_youtube_extract.list_available_AV_formats(URL=URL_I, CLEAN=True, LIST=True, SAVE=False, FILE_NAME= FILE_NAME_I)


# Function 3
# downlaod subtitles posted by the owner

man_sub_var = module_youtube_extract.down_sub(URL=URL_I, FILE_NAME=FILE_NAME_I, SAVE=False, MAN_SUB=True,  AUTO_SUB=False)


# Function 4
# downlaods automaticaly generated subtitles

auto_sub_var = module_youtube_extract.down_sub(URL=URL_I,  FILE_NAME=FILE_NAME_I, SAVE=False, MAN_SUB=False, AUTO_SUB=True)


# Function 5
# download audio and visual content

module_youtube_extract.down_audio_video(URL=URL_I, VIDEO_QUALITY_CODE= VIDEO_QUALITY_CODE_I, AUDIO_QUALITY_CODE= AUDIO_QUALITY_CODE_I, MERGE=True, FILE_NAME=FILE_NAME_I)
# terminal example
# youtube-dl -f 18+140 -o '%(title)s.%(ext)s' https://www.youtube.com/watch?v=7Ft4CgALkVI


# Function 6
# download audio as mp3

module_youtube_extract.down_audio(URL = URL_I, BIT_RATE='192',CODEC='mp3',NAME=FILE_NAME_I)



