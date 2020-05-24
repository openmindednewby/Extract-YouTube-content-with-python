# download youtube audio as an mp3
def down_audio(URL,BIT_RATE='192', CODEC='mp3', NAME='%(title)s.%(ext)s'):
    import __future__
    import subprocess
    subprocess.run(['youtube-dl', '--extract-audio', '--audio-format', CODEC, '--audio-quality', BIT_RATE, '-o', NAME, URL], capture_output=True)
    return print('download complete')


# download audio visual subtitles
def down_audio_video(URL, VIDEO_QUALITY_CODE = '', AUDIO_QUALITY_CODE = '', MERGE=False, FILE_NAME='%(title)s.f%(format_id)s.%(ext)s'):
    '''
    # terminal example
    youtube-dl -f 137+140 -o '%(title)s.%(ext)s' https://www.youtube.com/watch?v=7Ft4CgALkVI
    The following function us used to download the audio and video from youtube.
    
    AUDIO_QUALITY_CODE and VIDEO_QUALITY_CODE---> code should be found and selected from the output of function 'list_available_AV_formats'
    MERGE----> Specifies if we would like to merge the output or keep the audio and video as separate files.  
    FILE_NAMES ---> We can specify any name we would like to the files (the extension will be different and thuse  we will still be able to distinguish the files). We could also name them with the same name as the owner of the youtubue video using the specified format '%(title)s.f%(format_id)s.%(ext)s'
    '''
    import subprocess
# very useful resource 
#https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
#https://www.ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/ 
    # https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl/1097056#1097056
    # youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 https://youtu.be/FWGC9SqA3J0
    #
    if MERGE==True:
        print('Download initiated')
        AV_QUALITY_CODES=str(VIDEO_QUALITY_CODE)+'+'+str(AUDIO_QUALITY_CODE)
        a=subprocess.run(['youtube-dl', '-f', AV_QUALITY_CODES, '-o', FILE_NAME, URL], capture_output=True)
        print('Download completed')
        print('File saved as',FILE_NAME)
        return str(a)
    elif MERGE==False:
        print('Download initiated')
        AV_QUALITY_CODES=str(VIDEO_QUALITY_CODE)+','+str(AUDIO_QUALITY_CODE)
        a=subprocess.run(['youtube-dl', '-f', AV_QUALITY_CODES, '-o', FILE_NAME, URL], capture_output=True)    
        print('Download completed')
        print('Files saved as',FILE_NAME)
        return str(a)
    else:
        pass


        

# Download subtitles posted by video owners and automaticaly generated subtitles
def down_sub(URL, FILE_NAME, SAVE=True, MAN_SUB=True, AUTO_SUB=True,):
    
    '''
    This funtion downloads the subtitles of the URL provided. The list of supported websites are listed here:https://ytdl-org.github.io/youtube-dl/supportedsites.html
    MAN_SUB --> specifies if we would like to download the subtitles posted by the owner
    AUTO_SUB ---> specifies if we would like to download the automaticaly generated subtitles of youtube
    FILE_NAME ---> just the file name to store the subtitles. DO NOT ADD A EXTENSION TO THE NAME
    DEL_FILE ---> this delets the file which is created in the process of downlading the subtitles as the youtube-dl command doesn't naturaly output a result insted it saves in a text file
    The extansion the subtitles are saved is .en.vtt which is text readable format and can  be opened with the open funtion and the .en.vtt extension
    '''
    
    import subprocess
    import os
   
    if (MAN_SUB==True and AUTO_SUB==False and SAVE==True):
        try:
            # executes command and capture manual subtitles
            subprocess.run(['youtube-dl', '--write-sub', '--skip-download','-o', FILE_NAME, URL], capture_output=True)
            with open(FILE_NAME + '.en.vtt', "r") as manual_sub:
                FileContent = manual_sub.read()
            return str(FileContent)
        except:
            print('The following video does not contain subtitles posed by the owner')

    elif (MAN_SUB==True and AUTO_SUB==False and SAVE==False):
        try:
            # executes command and capture manual subtitles
            subprocess.run(['youtube-dl', '--write-sub', '--skip-download','-o', FILE_NAME, URL], capture_output=True)
            with open(FILE_NAME + '.en.vtt', "r") as manual_sub:
                FileContent = manual_sub.read()
                os.remove(FILE_NAME + '.en.vtt')
            return str(FileContent)
        except:
            print('The following video does not contain subtitles posed by the owner')

    elif (MAN_SUB==False and AUTO_SUB==True and SAVE==True):
        try:
            # executes command and capture automatic subtitles
            subprocess.run(['youtube-dl', '--write-auto-sub', '--skip-download','-o', FILE_NAME, URL], capture_output=True)
            # read the content of the saved file
            with open(FILE_NAME + '.en.vtt', "r") as auto_sub:
                FileContent = auto_sub.read()
            return str(FileContent)
        except:
            print('The following video does not contain automaticaly generated subtitles')

    elif (MAN_SUB==False and AUTO_SUB==True and SAVE==False):
        try:
            # executes command and capture automatic subtitles
            subprocess.run(['youtube-dl', '--write-auto-sub', '--skip-download','-o', FILE_NAME, URL], capture_output=True)
            # read the content of the saved file
            with open(FILE_NAME + '.en.vtt', "r") as auto_sub:
                FileContent = auto_sub.read()
            os.remove(FILE_NAME + '.en.vtt')
            return str(FileContent)
        except:
            print('The following video does not contain automaticaly generated subtitles')

    elif (MAN_SUB==True and AUTO_SUB==True):
        return print('Please select only one of the 2 options, MAN_SUB or AUTO_SUB')
    
    elif (MAN_SUB==False and AUTO_SUB==False):
        return print('Please select only one of the 2 options, MAN_SUB or AUTO_SUB')
    
    else:
        pass




'''
# one method to capture output from the terminal
output = subprocess.Popen( './list_all_formats.sh', stdout=subprocess.PIPE ).communicate()[0]
'''
#This function lists all available audio and video formats for download.
def list_available_AV_formats(URL, CLEAN=True, LIST=True, SAVE=False, FILE_NAME='list_all_formats'):
    '''
    This function extracts all the formating information about the URL video
    substitude the URL with the video URL you would like to download
    Clean  removes unecessary  text fromt the format infomration
    LIST produces a list with each format in a row insted of a str obj
    SAVE=True saves your file with in a text file with the specified FILE_NAME
    '''
    import subprocess
    
    # executes command and captures the output 
    list_all_formats=subprocess.run(['youtube-dl', '--list-formats', URL], capture_output=True)
    
    #creates a str variable of all available formats
    string_list_all_formats = str(list_all_formats)
        
        
    # returns un cleaned info
    if (CLEAN == False and SAVE== False and LIST==False):      
        print('Available formats have been extracted from the URL:', URL)
        return string_list_all_formats

    # returns un cleaned info and saves to filename
    if (CLEAN == False and SAVE== True and LIST==False):  
        # saves the output of the command
        f = open(FILE_NAME + '.txt', 'w')
        f.write(string_list_all_formats)
        f.close()
        print('File with all available AV formats for the URL:', URL, 'have been saved in', FILE_NAME)
        return string_list_all_formats
                
    
    # returns clean format
    if (CLEAN == True and SAVE== False and LIST==False):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # Clean info so that each line contains a single AV format
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace('\\n', '\n')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()
        
        return simple_useful_info_available_formats
    
    # returns clean format and saves to file as well
    if (CLEAN == True and SAVE== True and LIST==False):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # Clean info so that each line contains a single AV format
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace('\\n', '\n')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()
        
        # saves the output of the command
        f = open(FILE_NAME + '.txt', 'w')
        f.write(simple_useful_info_available_formats)
        f.close()
        return simple_useful_info_available_formats
    
    # returns clean format as a list
    if (CLEAN == True and SAVE== False and LIST==True):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()        
    
        # creates a list and assigns each audio or video format to its dedicated slot
        list_useful=simple_useful_info_available_formats.rsplit('\\n')
        
        # Removes empty elements. Note: should have removed all '' in the list however the one towards the end remains :/
        list_useful= list(filter(('').__ne__, list_useful))    
        return list_useful
        
        
        # returns clean format as a list and saves to a file
    if (CLEAN == True and SAVE== True and LIST==True):      
        
        # Finds the position in which the usful information origintes
        index_of_useful_info=string_list_all_formats.find('format code  extension  resolution note') + len('format code  extension  resolution note')
        
        # creates a new var with only that info
        useful_info_available_formats=string_list_all_formats[index_of_useful_info:]
        
        # Clean info and rename
        simple_useful_info_available_formats=useful_info_available_formats.replace('\'' ,' ')
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace(' , stderr=b  )', ' ')
        
        # remove additional white space from the ends
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()
    
        # creates a list and assigns each audio or video format to its dedicated slot
        list_useful=simple_useful_info_available_formats.rsplit('\\n')
        
        # Removes empty elements. Note: should have removed all '' in the list however the one towards the end remains :/
        list_useful= list(filter(('').__ne__, list_useful))   
        
        # Clean info so that each line contains a single AV format. This will only be used for the saved file
        simple_useful_info_available_formats=simple_useful_info_available_formats.replace('\\n', '\n')
        
        simple_useful_info_available_formats=simple_useful_info_available_formats.strip()

        
        # saves the output of the command
        f = open(FILE_NAME + '.txt', 'w')
        f.write(simple_useful_info_available_formats)
        f.close()
        return list_useful



# META DATA
def meta_data(URL,  FILE_NAME='vide_x_meta_data', TXT_CLEAN=True, TXT=True, JSON=True,DOWNLOAD=False):
    ''' 
    This function extracts the meta data of a youtube video and saves it into a file
    URL of the format URL = 'https://www.youtube.com/watch?v=YHCZt8LeQzI&fbclid=IwAR2e436VcxEBWWnnz48W2vPU4iTfFpxgglA9U7uIOFP1XCA1sdp4h_qnmLI'
    DOWNLOAD =  either True or False
    FILE_NAME ---> Do not include the extension of the fle, in case both TXT_CLEAN and TXT = True the '_clean_format' is added at the en of the file name
    
    '''
    
#    from __future__ import unicode_literals
    import __future__
    import youtube_dl
    import json
    ydl_opts = {}

    # gets the meta data of the video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(URL, download=DOWNLOAD) 

    meta_keys=list(meta.keys())
    meta_values=list(meta.values())

    if (TXT==False and TXT_CLEAN==False and JSON==False):    # save into text file
        pass
    elif (TXT==True and TXT_CLEAN==False and JSON==False):    # save into text file
        f = open(FILE_NAME + '.txt', 'w')
        f.write( str(meta) )
        f.close()
        
    elif (TXT==False and TXT_CLEAN==True and JSON==False):    # save into text file with nice format and adds _clean_format.txt at the end.
        with open(FILE_NAME + '.txt', 'w') as f:
            for i in range(len(meta_keys)):
                f.write(str(meta_keys[i]) + ':' + str(meta_values[i]) + '\n')

    elif (TXT==False and TXT_CLEAN==False and JSON==True):    #save into a json file
        json = json.dumps(meta)
        f = open(FILE_NAME+'.json', 'w')
        f.write(json)
        f.close()
        
    elif (TXT==True and TXT_CLEAN==True and JSON==False):
        f = open(FILE_NAME + '.txt', 'w')
        f.write( str(meta) )
        f.close()
        with open(FILE_NAME + '_clean_format.txt', 'w') as f:
            for i in range(len(meta_keys)):
                f.write(str(meta_keys[i]) + ':' + str(meta_values[i]) + '\n')
                
    elif (TXT==False and TXT_CLEAN==True and JSON==True):
        with open(FILE_NAME + '.txt', 'w') as f:
            for i in range(len(meta_keys)):
                f.write(str(meta_keys[i]) + ':' + str(meta_values[i]) + '\n')
        json = json.dumps(meta)
        f = open(FILE_NAME+'.json', 'w')
        f.write(json)
        f.close()
    
    elif (TXT==True and TXT_CLEAN==False and JSON==True):
        f = open(FILE_NAME + '.txt', 'w')
        f.write( str(meta) )
        f.close()
        json = json.dumps(meta)
        f = open(FILE_NAME+'.json', 'w')
        f.write(json)
        f.close()
        
    elif (TXT==True and TXT_CLEAN==True and JSON==True):
        f = open(FILE_NAME + '.txt', 'w')
        f.write( str(meta) )
        f.close()
        with open(FILE_NAME + '_clean_format.txt', 'w') as f:
            for i in range(len(meta_keys)):
                f.write(str(meta_keys[i]) + ':' + str(meta_values[i]) + '\n')
        json = json.dumps(meta)
        f = open(FILE_NAME+'.json', 'w')
        f.write(json)
        f.close()
    else:
        pass

    return meta
    
