# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:48:11 2020

@author: Vincent

GUI wrapper for youtube-dl
Allow selection of saved file in MP3 or MP4 format
Require: youtube-dl, tkinter, subprocess

"""

import tkinter as tk
import subprocess

class YTDownloader(object):
    """
    Class to encapsulate Youtube Downloader
    Attributes: 
        save_path: path where file will be saved
        format_string: download format MP3 for audio (default) or MP4 for video
        url_link: Youtube URL link
    """

    def __init__(self):
        self.save_path = ''
        self.format_string = '--extract-audio --audio-format mp3 '
        self.url_link = ''
        
    # Load the path of the driver for use from file SavePath.ini
    def load_save_path(self):
        path_file = open('SavePath.ini', 'r')
        self.save_path = path_file.read().strip()
        path_file.close()

    # Start Download command
    def download_click(self):
        print('Start Download')
        text = 'youtube-dl --rm-cache-dir ' + self.format_string + self.url_link.get() 
        print(text)
        result = subprocess.Popen(text, shell=True, stdout=subprocess.PIPE, cwd=self.save_path)
        output,error = result.communicate()
        print (output)
        print(error)

    # Radio Button selection
    def set_type(self,type_var):
        if type_var == 'Audio MP3':
            self.format_string = '--extract-audio --audio-format mp3 '
        elif type_var == 'Video MP4':
            self.format_string = '--recode-video mp4 '

    # Create Main GUI    
    def create_gui(self):    
        main_window = tk.Tk() 
        main_window.geometry('600x300')
        self.url_link = tk.Entry(main_window, width = 60)
        url_label = tk.Label(main_window, text = 'Enter URL Address: ')
        
        main_window.title('Youtube Downloader') 
        button_download = tk.Button(main_window, text='Download', width=12, command = self.download_click) 
        button_quit = tk.Button(main_window, text='Quit', width=8, command = main_window.destroy) 
        path_text = tk.Label(main_window, text = 'Save Path: '+ self.save_path)
        
        radio_selection = ['Audio MP3','Video MP4']
        
        radio_var = tk.StringVar()
        radio_var.set(radio_selection[0])   
        url_label.pack(anchor = tk.NW)
        self.url_link.pack(anchor = tk.NW)
        for key in radio_selection:
            tk.Radiobutton(main_window, text = key,
                        command = lambda: self.set_type(radio_var.get()),
                        variable = radio_var, value = key).pack(anchor = tk.NW)
        # Example of using lambda to pass argument to function

        
        button_download.pack(anchor = tk.NW)
        path_text.pack(anchor = tk.NW)
        button_quit.pack(anchor = tk.NW)
        
        main_window.mainloop() 

if __name__ == '__main__':
    yt = YTDownloader()
    yt.load_save_path()
    yt.create_gui()
    

