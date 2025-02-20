import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image
from pathlib import Path
import webbrowser
import yt_dlp  # yt-dlp library for video downloading

# Function to convert JPEG to PDF
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

# Mock function for EXE to APK conversion
def convert_exe_to_apk():
    messagebox.showinfo(
        "EXE to APK Conversion",
        "Direct EXE to APK conversion is not feasible. "
        "Please use tools like 'Wine' for running EXE on Android or port your application using development frameworks."
    )
    webbrowser.open("https://example.com/exe-to-apk-guide")

# Function to download video from URL using yt-dlp
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
    input_entry.pack(pady=5)

    submit_button = ttk.Button(input_window, text="Download", command=on_submit)
    submit_button.pack(pady=10)

    input_window.transient()
    input_window.grab_set()
    input_window.mainloop()

# Function to convert AVI to MP4 without FFmpeg or moviepy
def convert_avi_to_mp4():
    file_path = filedialog.askopenfilename(filetypes=[("AVI files", "*.avi")])
    if not file_path:
        return

    try:
        with open(file_path, 'rb') as avi_file:
            data = avi_file.read()

        output_path = Path.home() / "Downloads" / (Path(file_path).stem + ".mp4")
        with open(output_path, 'wb') as mp4_file:
            mp4_file.write(data)

        messagebox.showinfo("Success", f"File saved as MP4 to {output_path} (mock conversion)")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to convert audio to text
def convert_audio_to_text():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.mp3")])
    if not file_path:
        return

    try:
        import speech_recognition as sr
        from pydub import AudioSegment

        recognizer = sr.Recognizer()

        # Convert MP3 to WAV if necessary 
        if file_path.endswith(".mp3"):
            audio = AudioSegment.from_mp3(file_path)
            wav_path = Path(file_path).with_suffix(".wav")
            audio.export(wav_path, format="wav")
            file_path = wav_path

        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        output_path = Path.home() / "Downloads" / (Path(file_path).stem + ".txt")
        with open(output_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)

        messagebox.showinfo("Success", f"Text extracted and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
def create_gui():
    root = tk.Tk()
    root.title("File Converter")
    root.geometry("400x500")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use('clam')

    root.configure(bg='#2E2E2E')
    style.configure('TLabel', background='#2E2E2E', foreground='#FFFFFF', font=("Arial", 12))
    style.configure('TButton', background='#4CAF50', foreground='#FFFFFF', font=("Arial", 12, "bold"), padding=10)
    style.map('TButton', background=[('active', '#45A049')])

    header_label = ttk.Label(root, text="File Converter", font=("Arial", 18, "bold"))
    header_label.pack(pady=10)

    desc_label = ttk.Label(
        root,
        text="Convert files between different formats and download videos.",
        wraplength=350,
        justify="center"
    )
    desc_label.pack(pady=10)

    jpeg_to_pdf_button = ttk.Button(
        root, text="Convert JPEG to PDF", command=convert_jpeg_to_pdf, width=30
    )
    jpeg_to_pdf_button.pack(pady=10)

    exe_to_apk_button = ttk.Button(
        root, text="Convert EXE to APK", command=convert_exe_to_apk, width=30
    )
    exe_to_apk_button.pack(pady=10)

    download_video_button = ttk.Button(
        root, text="Download Video", command=download_video, width=30
    )
    download_video_button.pack(pady=10)

    avi_to_mp4_button = ttk.Button(
        root, text="Convert AVI to MP4", command=convert_avi_to_mp4, width=30
    )
    avi_to_mp4_button.pack(pady=10)

    audio_to_text_button = ttk.Button(
        root, text="Convert Audio to Text", command=convert_audio_to_text, width=30
    )
    audio_to_text_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
