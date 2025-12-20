# Import libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import sys
import os
import math
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'calculators')
sys.path.append(src_dir)

# Configuration of the window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk()
app.geometry("640x480")
app.title("Datagenius Toolkit")

# Creation of the pages
pages = {}

def show_page(page_name):
    for page in pages.values():
        page.place_forget()

    if page_name in pages:
        pages[page_name].place(relwidth=1, relheight=1)
    else:
        print(f"Error: La página '{page_name}' no existe.")

page_names_list = [
    "initial_page",
    "menu_page",
    "temperature_conversion_page",
    "cloud_storage_cost_page",
    "execution_time_calculator_page",
    "euclidean_distance_calculator_page",
    "average_grade_page",
    "simple_interest_calculator_page",
    "average_speed_of_a_drone_page",
    "body_mass_index_calculator_page",
    "energy_consumption_page",
    "currency_conversion_page",
]

for name in page_names_list:
    frame = ctk.CTkFrame(app, fg_color=("#0a0a2a", "#1a1a2e"))
    pages[name] = frame


# INITIAL PAGE CONTENT-------------------------------------------------
# Title
title_label = ctk.CTkLabel(
    pages["initial_page"], 
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
    pages["initial_page"],
    text="Calculation toolset",
    font=ctk.CTkFont(size=16),
    text_color="#8888ff",
    bg_color="#1a1a2e")
subtitle_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Decoration ring 
central_device = ctk.CTkFrame(
    pages["initial_page"],
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
    pages["initial_page"],
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
    command=lambda: show_page("menu_page"))
start_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# MENU PAGE CONTENT--------------------------------------------
# Title
title_label = ctk.CTkLabel(
    pages["menu_page"], 
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
    pages["menu_page"],
    text="Back",
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
    command=lambda: show_page("initial_page"))
return_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

# Frame for ubicate others buttons
scrollable_frame = ctk.CTkScrollableFrame(pages["menu_page"], width=600, height=300)
scrollable_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

scrollable_frame.columnconfigure(0, weight=1, uniform="group1")
scrollable_frame.columnconfigure(1, weight=1, uniform="group1")
scrollable_frame.columnconfigure(2, weight=1, uniform="group1")

# Program 1
buttons_config = [
    {"text":"Temperature", "image":"docs/images/icon1.jpg", "color":"#ff5555", "command": lambda: show_page("temperature_conversion_page")},
    {"text":"Cloud Storage Cost", "image":"docs/images/icon2.jpg", "color":"#aa55ff", "command": lambda: show_page("cloud_storage_cost_page")},
    {"text":"Execution Time", "image":"docs/images/icon3.jpg", "color":"#ffff55", "command": lambda: show_page("execution_time_calculator_page")},
    {"text":"Euclidean Distance", "image":"docs/images/icon4.jpg", "color":"#55ff55", "command": lambda: show_page("euclidean_distance_calculator_page")},
    {"text":"Average Grade", "image":"docs/images/icon5.jpg", "color":"#ff55aa", "command": lambda: show_page("average_grade_page")},
    {"text":"Simple Interest", "image":"docs/images/icon6.jpg", "color":"#ffaa00", "command": lambda: show_page("simple_interest_calculator_page")},
    {"text":"Average Speed", "image":"docs/images/icon7.jpg", "color":"#55ffff", "command": lambda: show_page("average_speed_of_a_drone_page")},
    {"text":"Body Mass Index", "image":"docs/images/icon8.jpg", "color":"#5555ff", "command": lambda: show_page("body_mass_index_calculator_page")},
    {"text":"Energy Consumption", "image":"docs/images/icon9.jpg", "color":"#aaff55", "command": lambda: show_page("energy_consumption_page")},
    {"text":"Currency Conversion", "image":"docs/images/icon10.jpg", "color":"#aaff00", "command": lambda: show_page("currency_conversion_page")},
]


for i, config in enumerate(buttons_config):
    row_val = i // 3
    column_val = i % 3
    
    # Icon
    # Possible errors
    try:
        icon_original = Image.open(config["image"])
        icon_photo = ctk.CTkImage(light_image=icon_original, size=(64, 64))
    except Exception as e:
        print(f"Error loading image: {e}.")
        icon_photo = None
# Icon placement
    if icon_photo:
        option_button = ctk.CTkButton(
        scrollable_frame,
        text=config["text"],
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color=config["color"],
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color=config["color"],
        compound="bottom",
        image=icon_photo,
        command=config["command"])
    else:
        option_button = ctk.CTkButton(
        scrollable_frame,
        text=config["text"],
        font=ctk.CTkFont(size=15, weight="bold"),
        width=200,
        height=45,
        text_color=config["color"],
        corner_radius=25,
        fg_color="#0a0a2a",
        bg_color="#1a1a2e",
        hover_color="#0e0e3d",
        border_width=3,
        border_color=config["color"],
        command=config["command"])
    option_button.grid(row=row_val, column=column_val, pady=10,sticky="NSEW")

# TEMPERATURE CONVERSION PAGE CONTENT-----------------------
# Functions
import temperature_conversion
def calculate_values():
    value = entry.get()
    try:
        value = float(value)
    except ValueError as v:
        entry.delete(0, "end")
        entry.insert(0, f"Error: {v}")
        return
    if value < -273.15:
        entry.delete(0, "end")
        entry.insert(0, "Error: Temperature cannot be below absolute zero (-273.15°C)")
        return
    fahrenheit_results.configure(text=f"{temperature_conversion.celsius_to_fahrenheit(value):.2f}°F")
    kelvin_results.configure(text=f"{temperature_conversion.celsius_to_kelvin(value):.2f}K")
    entry.delete(0, "end")
    entry.focus()

def clean():
    entry.delete(0, "end")
    entry.focus()
    fahrenheit_results.configure(text="00.00°F")
    kelvin_results.configure(text="00.00K")
    
def copy_text_fahrenheit():
    text_copy = fahrenheit_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(text_copy)
    app.update()
    button_copy1.configure(text="Copied Text")
    app.after(2000, lambda: button_copy1.configure(text="Copy"))
    
def copy_text_kelvin():
    text_copy = kelvin_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(text_copy)
    app.update()
    button_copy2.configure(text="Copied Text")
    app.after(2000, lambda: button_copy2.configure(text="Copy"))
        
# Title
title1 = ctk.CTkLabel(
    pages["temperature_conversion_page"], 
    text="TEMPERATURE CONVERSION", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#ff5555", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title1.place(relx=0.5, rely=0.08, anchor=tk.CENTER) 

# Input section
frame_input = ctk.CTkFrame(
    pages["temperature_conversion_page"], 
    width=600, height=150, 
    fg_color="#1a1a2e",
    border_color="#ff5555",
    border_width=2,
    corner_radius=15)
frame_input.place(relx=0.5, rely=0.32, anchor=tk.CENTER)
# Title
title_input = ctk.CTkLabel(
    frame_input, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ff5555", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input.place(relx=0.5, rely=0.15,anchor=tk.CENTER)
# Order
order = ctk.CTkLabel(
    frame_input, 
    text="Enter temperature in Celsius:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffaa66", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order.place(relx=0.2, rely=0.43, anchor=tk.CENTER)
# Entry order
entry = ctk.CTkEntry(
    frame_input, 
    placeholder_text="0.0",
    fg_color="#0a0a2a",                 
    text_color="#ffffff",               
    border_color="#ffaa66",             
    placeholder_text_color="#8888ff")
entry.place(relx=0.55, rely=0.43, anchor=tk.CENTER)
# Buttons order
button_convert = ctk.CTkButton(
    frame_input,
    text="CONVERT",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#ff5555",
    bg_color="#1a1a2e",
    hover_color="#ff3333",
    border_width=3,
    border_color="#ffffff",
    command=calculate_values)
button_convert.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean = ctk.CTkButton(
    frame_input,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#cccccc",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    border_width=3,
    border_color="#8888ff",
    command=clean)
button_clean.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results = ctk.CTkFrame(
    pages["temperature_conversion_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#333355",
    border_width=3,
    corner_radius=10)
frame_results.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_input = ctk.CTkLabel(
    frame_results, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#00ccff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Fahrenheit results
fahrenheit_title = ctk.CTkLabel(
    frame_results, 
    text="The temperature in Fahrenheit is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffaa66",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
fahrenheit_title.place(relx=0.23, rely=0.43, anchor=tk.CENTER)

fahrenheit_results = ctk.CTkLabel(
    frame_results,
    text="00.00°F",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffaa44", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
fahrenheit_results.place(relx=0.52, rely=0.43, anchor=tk.CENTER)

button_copy1 = ctk.CTkButton(
    frame_results,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffaa66",
    corner_radius=25,
    fg_color="transparent",
    bg_color="#1a1a2e",
    hover_color="#332211",
    border_width=3,
    border_color="#ff8844",
    command=copy_text_fahrenheit)
button_copy1.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Kelvin results
kelvin_title = ctk.CTkLabel(
    frame_results, 
    text="The temperature in Kelvin is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#66aaff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
kelvin_title.place(relx=0.23, rely=0.80, anchor=tk.CENTER)

kelvin_results = ctk.CTkLabel(
    frame_results,
    text="00.00K",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#4488ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
kelvin_results.place(relx=0.52, rely=0.80, anchor=tk.CENTER)

button_copy2 = ctk.CTkButton(
    frame_results,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#66aaff",
    corner_radius=25,
    fg_color="transparent",
    bg_color="#1a1a2e",
    hover_color="#112233",
    border_width=3,
    border_color="#4488ff",
    command=copy_text_kelvin)
button_copy2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button = ctk.CTkButton(
    pages["temperature_conversion_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#ff5555",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#ff5555",
    command=lambda: show_page("menu_page"))
return_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


show_page("initial_page")

app.mainloop()
