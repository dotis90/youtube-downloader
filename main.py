import sys
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.folder_selected = ""
        self.master = master
        self.pack()
        self.create_widgets()
        self.winfo_toplevel().title("Youtube Downloader")
        self.winfo_toplevel().geometry("500x200")

    def create_widgets(self):
        
        #url input label
        self.url_label = tk.Label(self, text="Enter Youtube URL:")
        self.url_label.grid(row=1, column=2)

        #URL input field
        self.entry = tk.Entry(self, width=50)
        self.entry.grid(row=2, column=2)

        #choose directory button
        self.select_directory = tk.Button(self, text="Choose Directory", command=self.choose_directory)
        self.select_directory.grid(row=3, column=2)

        #directory display button
        self.directory_label = tk.Label(self, text="Directory Selected:" + self.folder_selected)
        self.directory_label.grid(row=4, column=2)

        #download button
        self.download = tk.Button(self, text="Download", command=self.download_video)
        self.download.grid(row=5, column=2)

        #error label
        self.error_label = tk.Label(self, text="")
        self.error_label.grid(row=6, column=2)

    def download_video(self):

        self.set_error_text("")

        try:
            
            video_url = self.entry.get()

            if self.folder_selected == "":
                self.set_error_text("Please select a folder")
            else:
                YouTube(video_url).streams.filter(res="720p").first().download(self.folder_selected)

        except:
            self.set_error_text("")
            self.set_error_text(sys.exc_info())

    def choose_directory(self):

        self.set_error_text("")

        try:
            self.folder_selected = filedialog.askdirectory()
            self.directory_label["text"] = self.folder_selected  
        except:  
            self.set_error_text("")
            self.set_error_text(sys.exc_info())

    def set_error_text(self, text):
        self.error_label["text"] = text

root = tk.Tk()
app = Application(master=root)
app.mainloop()