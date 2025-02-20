# Screen-recorder
Free screen-recorder in HD quality
# File covnvetor 😊
This is a software which is made by python 100% it contains many features. The realses of the app versions is 1.0 t0 5.0
**realses:** 4 times.
### Features:-
- 0 bugs
- It can download video from youtube.
- It can convert JPEG file to pd
- IT can convert avi files to mp4 files.
- It can convert audio files(mp3 or .wav) to txt file.
- It can guide how toconvert exe file to PK files
- It is secure
### About app:-
- 70 MB
- **Language:** python
- **Libraraies:** Tkinter , os , webbrowser , yt_dlp , pillow , path
- **Structure type:** Dialog box 

## Code explanation:
**Imports and Setup**
``` bash
    pip install tkinter
```
``` bash
    pip install pillow
```
```
    pip install yt_dlp
```
These the libraries you need to make this software.
``` python
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image
from pathlib import Path
import webbrowser
import yt_dlp  # yt-dlp library for video downloading
```
### Uses of these libraries:
- **OS:** Provides a way of using operating system dependent functionality.
-  **Tkinter** Standard Python interface to the Tk GUI toolkit.
- **Pillow:** Python Imaging Library for opening, manipulating, and saving many different image file formats.
- **Webrowser:** provides a high-level interface to allow displaying Web-based documents to users.
- **yt_dlp**: A command-line program to download videos from YouTube and other video sites.

**Function to Convert JPEG to PDF**
``` python
    def convert_jpeg_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg *.jpeg")])
    if not file_path:
        return
    
    try:
        image = Image.open(file_path)
        output_path = Path.home() / "Downloads" / (Path(file_path).stem + ".pdf")
        image.save(output_path, "PDF", resolution=100.0)
        messagebox.showinfo("Success", f"File converted and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
```
 - **filedialog.askopenfilename:** Opens a file dialog to select a JPEG file.
- **Image.open:** Opens the selected image file.
- **Path.home() / "Downloads" / (Path(file_path).stem + ".pdf"):** Constructs the output path in the Downloads folder.
- **image.save:** Saves the image as a PDF.
- **Messagebox.showinfo:** Displays a success message.
- **Messagebox.showerror:** Displays an error message if an exception occurs.

**Mock Function for EXE to APK Conversion**
``` python
    def convert_exe_to_apk():
    messagebox.showinfo(
        "EXE to APK Conversion",
        "Direct EXE to APK conversion is not feasible. "
        "Please use tools like 'Wine' for running EXE on Android or port your application using development frameworks."
    )
    webbrowser.open("https://example.com/exe-to-apk-guide")
```
- **Messagebox.showinfo:** Displays an informational message about the infeasibility of direct EXE to APK conversion.
- **Webbrowser.open:** Opens a web browser to a guide on EXE to APK conversion.

**Function to Download Video from URL using yt-dlp**

``` python
    def download_video():
    def on_submit():
        video_url = url_var.get()
        if not video_url:
            messagebox.showwarning("Warning", "Please enter a valid video URL.")
            return

        try:
            download_path = Path.home() / "Downloads"
            ydl_opts = {
                'outtmpl': str(download_path / '%(title)s.%(ext)s'),
                'format': 'best',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            messagebox.showinfo("Success", f"Video downloaded successfully to {download_path}")
            input_window.destroy()
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    input_window = tk.Toplevel()
    input_window.title("Enter Video URL")
    input_window.geometry("400x150")
    input_window.configure(bg='#2E2E2E')

    url_var = tk.StringVar()

    input_label = ttk.Label(input_window, text="Enter the video URL:", font=("Arial", 12))
    input_label.pack(pady=10)

    input_entry = ttk.Entry(input_window, textvariable=url_var, font=("Arial", 12), width=40)
```
- **on_submit:** Inner function to handle the submission of the video URL.
- **url_var.get():** Retrieves the entered video URL.
- **messagebox.showwarning:** Displays a warning if the URL is not entered.
- **Path.home() / "Downloads":** Specifies the download path.
- **yt_dlp.YoutubeDL(ydl_opts):** Creates a yt-dlp object with specified options.
- **ydl.download([video_url]):** Downloads the video from the URL.
- **messagebox.showinfo:** Displays a success message.
- **input_window.destroy():** Closes the input window.
- **messagebox.showerror:** Displays an error message if an exception occurs.
- **tk.Toplevel():** Creates a new top-level window for URL input.
- **input_window.configure(bg='#2E2E2E'):** Sets the background color of the input window.
- **tk.StringVar():** Creates a variable to store the URL.
- **ttk.Label:** Creates a label widget.
- **ttk.Entry:** Creates an entry widget for URL input.

This code provides a GUI for converting JPEG images to PDF, displaying information about EXE to APK conversion, and downloading videos from URLs using yt-dlp.

## How to use this software:
To use this software download the exe file of this software in relaeses in GIthub website and press the button of exe file two times.

- **Convert jpeg file to pdf** Press the button of JPEG to pdf and choose file which you want to convert and press open button And name the file which the pdf is convert example -pdf and save it. It convert in pdf.
- **Download video from youtube** Press download button and paste url the video is download in you computer.
- **If you want more information press realese button to more information**
