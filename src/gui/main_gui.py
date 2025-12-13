# Import libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk  # Necesario para manejar imágenes

# Configuration of the window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.geometry("640x480")
app.title("Datagenius Toolkit")

# Configuration of the background
background_frame = ctk.CTkFrame(
    app, 
    fg_color=("#0a0a2a", "#1a1a2e"), 
    corner_radius=0)
background_frame.place(relwidth=1, relheight=1)  # Ocupa toda la ventana

# Title
title_label = ctk.CTkLabel(
    app, 
    text="DATAGENIUS TOOLKIT", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=42, weight="bold"), 
    text_color="#00ccff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER) 

# Subtitle
subtitle_label = ctk.CTkLabel(
    app,
    text="Calculation toolset",
    font=ctk.CTkFont(size=16),
    text_color="#8888ff",
    bg_color="#1a1a2e")
subtitle_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Decoration ring 
central_device = ctk.CTkFrame(
    app,
    width=180,
    height=180,
    corner_radius=90,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    border_width=4,
    border_color="#00ffaa")
central_device.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Icon inside of the central_device
# Possible errors
try:
    device_image_original = Image.open("docs/images/icon_firstframe.jpg")
    image_size = (160, 160)
    device_image_resized = device_image_original.resize(image_size, Image.Resampling.LANCZOS)
    device_photo = ImageTk.PhotoImage(device_image_resized)
except Exception as e:
    print(f"Error loading image: {e}. Using text icon.")
    device_photo = None
# Image/Icon placement
if device_photo:
    device_label = ctk.CTkLabel(central_device, text="", image=device_photo, bg_color="#1a1a2e")
    device_label.image = device_photo
else:
    device_label = ctk.CTkLabel(
        central_device, text="⚙️", 
        font=ctk.CTkFont(size=64), text_color="#00ffaa")
device_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Principal button
start_button = ctk.CTkButton(
    app,
    text="START SYSTEM",
    font=ctk.CTkFont(size=20, weight="bold"),
    width=200,
    height=50,
    text_color="#00ccff",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#00ccff")
start_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

app.mainloop()
