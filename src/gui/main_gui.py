# Import libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# Configuration of the window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.geometry("640x480")
app.title("Datagenius Toolkit")

# Creation of the pages
initial_page = ctk.CTkFrame(app, fg_color=("#0a0a2a", "#1a1a2e"))
menu_page = ctk.CTkFrame(app,fg_color=("#0a0a2a", "#1a1a2e"))
temperature_conversion_page = ctk.CTkFrame(app, fg_color=("#0a0a2a", "#1a1a2e"))

# Switch in the pages
def show_initial_page():
    menu_page.place_forget()
    temperature_conversion_page.place_forget()
    initial_page.place(relwidth=1, relheight=1)
def show_menu_page():
    initial_page.place_forget()
    temperature_conversion_page.place_forget()
    menu_page.place(relwidth=1, relheight=1)
def show_temperature_conversion_page():
    menu_page.place_forget()
    initial_page.place_forget()
    temperature_conversion_page.place(relwidth=1, relheight=1)

# INITIAL PAGE CONTENT-------------------------------------------------
# Title
title_label = ctk.CTkLabel(
    initial_page, 
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
    initial_page,
    text="Calculation toolset",
    font=ctk.CTkFont(size=16),
    text_color="#8888ff",
    bg_color="#1a1a2e")
subtitle_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Decoration ring 
central_device = ctk.CTkFrame(
    initial_page,
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
    device_photo = ctk.CTkImage(light_image=device_image_original, size=(160, 160))
except Exception as e:
    print(f"Error loading image: {e}. Using text icon.")
    device_photo = None
# Image/Icon placement
if device_photo:
    device_label = ctk.CTkLabel(central_device, text="", image=device_photo, bg_color="#1a1a2e")
    device_label.image = device_photo
else:
    device_label = ctk.CTkLabel(central_device, text="⚙️", font=ctk.CTkFont(size=64), text_color="#00ffaa")
device_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Principal button
start_button = ctk.CTkButton(
    initial_page,
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
    border_color="#00ccff",
    command=show_menu_page)
start_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# MENU PAGE CONTENT--------------------------------------------
# Title
title_label = ctk.CTkLabel(
    menu_page, 
    text="MENU", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#00ccff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER) 

# Button to return
return_button = ctk.CTkButton(
    menu_page,
    text="Return to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#00ccff",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#00ccff",
    command=show_initial_page)
return_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

# Frame for ubicate others buttons
scrollable_frame = ctk.CTkScrollableFrame(menu_page, width=600, height=300)
scrollable_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

scrollable_frame.columnconfigure(0, weight=1, uniform="group1")
scrollable_frame.columnconfigure(1, weight=1, uniform="group1")
scrollable_frame.columnconfigure(2, weight=1, uniform="group1")

# Program 1
# Icon
# Possible errors
try:
    icon1_original = Image.open("docs/images/icon1.jpg")
    icon1_photo = ctk.CTkImage(light_image=icon1_original, size=(64, 64))
except Exception as e:
    print(f"Error loading image: {e}.")
    icon1_photo = None
# Icon placement
if icon1_photo:
    option1_button = ctk.CTkButton(
    scrollable_frame,
    text="Temperature",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=200,
    height=45,
    text_color="#ff5555",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#ff5555",
    compound="bottom",
    image=icon1_photo,
    command=show_temperature_conversion_page)
else:
    option1_button = ctk.CTkButton(
    scrollable_frame,
    text="Temperature",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=200,
    height=45,
    text_color="#ff5555",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#ff5555",
    command=show_temperature_conversion_page)
option1_button.grid(row=0, column=0, pady=10,sticky="NSEW")

# Program 2
# Icon
# Possible errors
try:
    icon2_original = Image.open("docs/images/icon2.jpg")
    icon2_photo = ctk.CTkImage(light_image=icon2_original, size=(64, 64))
except Exception as e:
    print(f"Error loading image: {e}.")
    icon2_photo = None
# Icon placement
if icon2_photo:
    option2_button = ctk.CTkButton(
        scrollable_frame,
        text="Cloud Storage Cost",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#aa55ff",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#aa55ff",
        compound = "bottom",
        image = icon2_photo)
else:
    option2_button = ctk.CTkButton(
        scrollable_frame,
        text="Cloud Storage Cost",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#aa55ff",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#aa55ff")
option2_button.grid(row=0, column=1, pady=10, sticky="NSEW")

# Program 3
# Icon
# Possible errors
try:
    icon3_original = Image.open("docs/images/icon3.jpg")
    icon3_photo = ctk.CTkImage(light_image=icon3_original, size=(64, 64))
except Exception as e:
    print(f"Error loading imge: {e}.")
    icon3_photo = None
# Icon placement
if icon3_photo:
    option3_button = ctk.CTkButton(
        scrollable_frame,
        text="Execution Time",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#ffff55",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#ffff55",
        compound = "bottom",
        image = icon3_photo)
else:
    option3_button = ctk.CTkButton(
        scrollable_frame,
        text="Execution Time",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#ffff55",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#ffff55")
option3_button.grid(row=0, column=2, pady=10, sticky="NSEW")

# Program 4
# Icon
# Possible errors
try:
    icon4_original = Image.open("docs/images/icon4.jpg")
    icon4_photo = ctk.CTkImage(light_image=icon4_original, size=(64, 64))
except Exception as e:
    print(f"Error loading image: {e}")
    icon4_photo = None
# Icon placement
if icon4_photo:
    option4_button = ctk.CTkButton(
        scrollable_frame,
        text="Euclidean Distance",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#55ff55",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#55ff55",
        compound = "bottom",
        image = icon4_photo)
else:
    option4_button = ctk.CTkButton(
        scrollable_frame,
        text="Euclidean Distance",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#55ff55",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#55ff55")
option4_button.grid(row=1, column=0, pady=10, sticky="NSEW")

# Program 5
# Icon
# Possible errors
try:
    icon5_original = Image.open("docs/images/icon5.jpg")
    icon5_photo = ctk.CTkImage(light_image=icon5_original, size=(64,64))
except Exception as e:
    print(f"Error loading image: {e}")
    icon5_photo = None
# Icon placement
if icon5_photo:
    option5_button = ctk.CTkButton(
        scrollable_frame,
        text="Average Grade",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#ff55aa",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#ff55aa",
        compound = "bottom",
        image = icon5_photo)
else:
    option5_button = ctk.CTkButton(
        scrollable_frame,
        text="Average Grade",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#ff55aa",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#ff55aa")
option5_button.grid(row=1, column=1, pady=10, sticky="NSEW")

# Program 6
# Icon
# Possible errors
try:
    icon6_original = Image.open("docs/images/icon6.jpg")
    icon6_photo = ctk.CTkImage(light_image=icon6_original, size=(64,64))
except Exception as e:
    print(f"Error loading image: {e}")
    icon6_photo = None
# Icon placement
if icon6_photo:
    option6_button = ctk.CTkButton(
        scrollable_frame,
        text="Simple Interest",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#ffaa00",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#ffaa00",
        compound = "bottom",
        image = icon6_photo)
else:
    option6_button = ctk.CTkButton(
        scrollable_frame,
        text="Simple Interest",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#ffaa00",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#ffaa00")
option6_button.grid(row=1, column=2, pady=10, sticky="NSEW")

# Program 7
# Icon
# Possible errors
try:
    icon7_original = Image.open("docs/images/icon7.jpg")
    icon7_photo = ctk.CTkImage(light_image=icon7_original, size=(64, 64))
except Exception as e:
    print(f"Error loading image: {e}")
    icon7_photo = None
# Icon placement
if icon7_photo:
    option7_button = ctk.CTkButton(
        scrollable_frame,
        text="Average Speed",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#55ffff",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#55ffff",
        compound = "bottom",
        image = icon7_photo)
else:
    option7_button = ctk.CTkButton(
        scrollable_frame,
        text="Average Speed",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#55ffff",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#55ffff")
option7_button.grid(row=2, column=0, pady=10, sticky="NSEW")

# Program 8
# Icon
# Possible errors
try:
    icon8_original = Image.open("docs/images/icon8.jpg")
    icon8_photo = ctk.CTkImage(light_image=icon8_original, size=(64, 64))
except Exception as e:
    print(f"Error loading image: {e}")
    icon8_photo = None
# Icon placement
if icon8_photo:
    option8_button = ctk.CTkButton(
        scrollable_frame,
        text="Body Mass Index",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#5555ff",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#5555ff",
        compound = "bottom",
        image = icon8_photo)
else:
    option8_button = ctk.CTkButton(
        scrollable_frame,
        text="Body Mass Index",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#5555ff",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#5555ff")
option8_button.grid(row=2, column=1, pady=10, sticky="NSEW")

# Program 9
# Icon
# Possible errors
try:
    icon9_original = Image.open("docs/images/icon9.jpg")
    icon9_photo = ctk.CTkImage(light_image=icon9_original, size=(64, 64))
except Exception as e:
    print(f"Error loading image: {e}")
    icon9_photo = None
# Icon placement
if icon9_photo:
    option9_button = ctk.CTkButton(
        scrollable_frame,
        text="Energy Consumption",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#aaff55",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#aaff55",
        compound = "bottom",
        image = icon9_photo)
else:
    option9_button = ctk.CTkButton(
        scrollable_frame,
        text="Energy Consumption",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#aaff55",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#aaff55")
option9_button.grid(row=2, column=2, pady=10, sticky="NSEW")

# Program 10
# Icon
# Possible errors
try:
    icon10_original = Image.open("docs/images/icon10.jpg")
    icon10_photo = ctk.CTkImage(light_image=icon10_original, size=(64, 64))
except Exception as e:
    print(f"Error loading imagen: {e}")
    icon10_photo = None
# Icon placement
if icon10_photo:
    option10_button = ctk.CTkButton(
        scrollable_frame,
        text="Currency Conversion",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#aaff00",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#aaff00",
        compound = "bottom",
        image = icon10_photo)
else:
    option10_button = ctk.CTkButton(
        scrollable_frame,
        text="Currency Conversion",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color="#aaff00",
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color="#aaff00")
option10_button.grid(row=3, column=0, pady=10, sticky="NSEW")

show_initial_page()

app.mainloop()
