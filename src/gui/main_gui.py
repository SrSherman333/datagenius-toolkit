# Import libraries
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import sys
import os
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
app.resizable(False, False)

# Configuration of the scroll in the scrolleableframe
def on_mouse_wheel(event, frame):
    if event.num == 4 or event.delta > 0:
        frame._parent_canvas.yview_scroll(-1, "units")
    elif event.num == 5 or event.delta < 0:
        frame._parent_canvas.yview_scroll(1, "units")
    
app.bind("<MouseWheel>", lambda e: on_mouse_wheel(e, scrollable_frame))

app.bind("<Button-4>", lambda e: on_mouse_wheel(e, scrollable_frame))
app.bind("<Button-5>", lambda e: on_mouse_wheel(e, scrollable_frame))


# Creation of the pages
pages = {}

def show_page(page_name):
    for page in pages.values():
        page.place_forget()

    if page_name in pages:
        pages[page_name].place(relwidth=1, relheight=1)
    else:
        print(f"Error: The page '{page_name}' doesn't exist.")

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
    frame = ctk.CTkFrame(app, fg_color= ("#F0F2F5","#1a1a2e"))
    pages[name] = frame


# INITIAL PAGE CONTENT-------------------------------------------------
# Title
title_label = ctk.CTkLabel(
    pages["initial_page"], 
    text="DATAGENIUS TOOLKIT", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=42, weight="bold"), 
    text_color=("#007799","#00ccff"), 
    fg_color=("#F0F2F5","#1a1a2e"),
    bg_color=("#F0F2F5","#1a1a2e"),
    corner_radius=50)
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER) 

# Subtitle
subtitle_label = ctk.CTkLabel(
    pages["initial_page"],
    text="Calculation toolset",
    font=ctk.CTkFont(size=16),
    text_color=("#5555CC", "#8888FF"),
    bg_color=("#F0F2F5","#1a1a2e"))
subtitle_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Decoration ring 
central_device = ctk.CTkFrame(
    pages["initial_page"],
    width=180,
    height=180,
    corner_radius=90,
    fg_color=("#F0F2F5","#1a1a2e"),
    bg_color=("#F0F2F5","#1a1a2e"),
    border_width=4,
    border_color=("#00B377", "#00FFAA"))
central_device.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Icon inside of the central_device
# Possible errors
try:
    devicedark_image_original = Image.open("docs/images/icon_firstframe_dark.jpg")
    devicelight_image_original = Image.open("docs/images/icon_firstframe_light.png")
    device_photo = ctk.CTkImage(light_image=devicelight_image_original, dark_image=devicedark_image_original, size=(160, 160))
except Exception as e:
    print(f"Error loading image: {e}. Using text icon.")
    device_photo = None
# Image/Icon placement
if device_photo:
    device_label = ctk.CTkLabel(central_device, text="", image=device_photo, bg_color=("#F0F2F5","#1a1a2e"))
    device_label.image = device_photo
else:
    device_label = ctk.CTkLabel(central_device, text="⚙️", font=ctk.CTkFont(size=64), text_color=("#00B377", "#00FFAA"))
device_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Principal button
start_button = ctk.CTkButton(
    pages["initial_page"],
    text="START SYSTEM",
    font=ctk.CTkFont(size=20, weight="bold"),
    width=200,
    height=50,
    text_color=("#007799", "#00CCFF"),
    corner_radius=25,
    fg_color=("#F0F2F5", "#1A1A2E"),
    bg_color=("#F0F2F5", "#1A1A2E"),
    hover_color=("#D1D9E6", "#0E0E3D"),
    border_width=3,
    border_color=("#007799", "#00CCFF"),
    command=lambda: show_page("menu_page"))
start_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

try:
    dark_mode_image_original = Image.open("docs/images/icon_darkmode.png")
    light_mode_image_original = Image.open("docs/images/icon_lightmode.png")
    theme_mode_photo = ctk.CTkImage(light_image=light_mode_image_original, dark_image=dark_mode_image_original, size=(80, 80))
except Exception as e:
    print(f"Error loading image: {e}. Using text icon.")
    theme_mode_photo = None

def theme_control():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

theme_mode = ctk.CTkButton(
    pages["initial_page"],
    text="",
    width=80,
    height=80,
    corner_radius=5,
    image=theme_mode_photo,
    fg_color=("#F0F2F5", "#1A1A2E"),
    bg_color=("#F0F2F5", "#1A1A2E"),
    hover_color=("#D1D9E6", "#0E0E3D"),
    command=theme_control
)
theme_mode.place(relx=0.1, rely=0.85, anchor=tk.CENTER)

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
scrollable_frame = ctk.CTkScrollableFrame(
    pages["menu_page"], 
    width=600, height=300,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",)
scrollable_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

scrollable_frame.columnconfigure(0, weight=1, uniform="group1")
scrollable_frame.columnconfigure(1, weight=1, uniform="group1")
scrollable_frame.columnconfigure(2, weight=1, uniform="group1")

# Label Information
information = ctk.CTkLabel(
    pages["menu_page"], 
    text="Hover your mouse over a button to see its description",
    width=370, height=65,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=370,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10
)
information.place(relx=0.67, rely=0.91, anchor=tk.CENTER)

# Functions for the label information
def on_enter(description):
    information.configure(text=description)    
def on_leave():
    information.configure(text="Hover your mouse over a button to see its description")

# Program 1
buttons_config = [
    {"text":"Temperature", "description":"Calculate the equivalent temperature in degrees Fahrenheit and Kelvin from a temperature in Celsius", "image":"docs/images/icon1.jpg", "color":"#ff5555", "command": lambda: show_page("temperature_conversion_page")},
    {"text":"Cloud Storage Cost", "description":"Determine the total monthly and annual cost of cloud storage, based on the GB stored and the unit price", "image":"docs/images/icon2.jpg", "color":"#aa55ff", "command": lambda: show_page("cloud_storage_cost_page")},
    {"text":"Execution Time", "description":"Calculate the total time (in seconds and minutes) that a program takes to execute, given its operations and execution speed", "image":"docs/images/icon3.jpg", "color":"#ffff55", "command": lambda: show_page("execution_time_calculator_page")},
    {"text":"Euclidean Distance", "description":"Calculate the Euclidean distance between two points on a Cartesian plane, using their coordinates (x1, y1) and (x2, y2)", "image":"docs/images/icon4.jpg", "color":"#55ff55", "command": lambda: show_page("euclidean_distance_calculator_page")},
    {"text":"Average Grade", "description":"Calculate a student's final average grade from four individual grades", "image":"docs/images/icon5.jpg", "color":"#ff55aa", "command": lambda: show_page("average_grade_page")},
    {"text":"Simple Interest", "description":"Calculate the final total amount to be paid on a loan, considering the initial capital, the simple interest rate, and the time in years", "image":"docs/images/icon6.jpg", "color":"#ffaa00", "command": lambda: show_page("simple_interest_calculator_page")},
    {"text":"Average Speed", "description":"Calculate the average speed of a drone in km/h and m/s, given the distance traveled and the time taken", "image":"docs/images/icon7.jpg", "color":"#55ffff", "command": lambda: show_page("average_speed_of_a_drone_page")},
    {"text":"Body Mass Index", "description":"Calculate a person's BMI (Body Mass Index), requiring their weight in kilograms and their height in meters", "image":"docs/images/icon8.jpg", "color":"#5555ff", "command": lambda: show_page("body_mass_index_calculator_page")},
    {"text":"Energy Consumption", "description":"Calculate the energy consumption in kWh of a computer during a 30-day month, using its power and the hours of daily use", "image":"docs/images/icon9.jpg", "color":"#aaff55", "command": lambda: show_page("energy_consumption_page")},
    {"text":"Currency Conversion", "description":"Convert an amount of local currency to its equivalent value in US dollars (USD) and euros (EUR), using given exchange rates", "image":"docs/images/icon10.jpg", "color":"#aaff00", "command": lambda: show_page("currency_conversion_page")},
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
# Icon placement and creation of button
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
    
    # Send the corresponding description when the mouse is over a button
    option_button.bind("<Enter>", lambda event, desc=config["description"]: on_enter(desc), add="+")
    option_button.bind("<Leave>", lambda event: on_leave(), add="+")

# TEMPERATURE CONVERSION PAGE CONTENT-----------------------
# Functions
import temperature_conversion
def calculate_values():
    value = entry.get()
    try:
        value = float(value)
    except ValueError as v:
        errors_cloud1.configure(text="")
        errors_cloud1.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_cloud1.configure(text=""))
        return
    if value < -273.15:
        errors_cloud1.configure(text="")
        errors_cloud1.configure(text=f"Error: Temperature cannot be below absolute zero (-273.15°C)")
        app.after(3000, lambda:errors_cloud1.configure(text=""))
        return
    fahrenheit_results.configure(text=f"{temperature_conversion.celsius_to_fahrenheit(value):.2f}°F")
    kelvin_results.configure(text=f"{temperature_conversion.celsius_to_kelvin(value):.2f}K")

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
    button_copy1.configure(text="COPIED TEXT")
    app.after(2000, lambda: button_copy1.configure(text="COPY"))
    
def copy_text_kelvin():
    text_copy = kelvin_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(text_copy)
    app.update()
    button_copy2.configure(text="COPIED TEXT")
    app.after(2000, lambda: button_copy2.configure(text="COPY"))
        
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
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

#Label for errors
errors_cloud1 = ctk.CTkLabel(
    frame_input, 
    text="",
    width=150, height=85,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=150,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_cloud1.place(relx=0.83, rely=0.34, anchor=tk.CENTER)

# Order
order = ctk.CTkLabel(
    frame_input, 
    text="Enter temperature in Celsius:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order.place(relx=0.2, rely=0.43, anchor=tk.CENTER)
# Entry order
entry = ctk.CTkEntry(
    frame_input, 
    placeholder_text="0.0",
    fg_color="#441111",                 
    text_color="#ffffff",               
    border_color="#ff5555",             
    placeholder_text_color="#ffffff")
entry.place(relx=0.55, rely=0.43, anchor=tk.CENTER)
# Buttons order
button_convert = ctk.CTkButton(
    frame_input,
    text="CONVERT",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ff5555",
    bg_color="#1a1a2e",
    hover_color="#ff8888",
    command=calculate_values)
button_convert.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean = ctk.CTkButton(
    frame_input,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean)
button_clean.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results = ctk.CTkFrame(
    pages["temperature_conversion_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_input = ctk.CTkLabel(
    frame_results, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Fahrenheit results
fahrenheit_title = ctk.CTkLabel(
    frame_results, 
    text="The temperature in Fahrenheit is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
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
    text_color="#ff5555", 
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
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ff5555",
    bg_color="#1a1a2e",
    hover_color="#ff8888",
    command=copy_text_fahrenheit)
button_copy1.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Kelvin results
kelvin_title = ctk.CTkLabel(
    frame_results, 
    text="The temperature in Kelvin is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
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
    text_color="#ff5555", 
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
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
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


# CLOUD STORAGE COST PAGE CONTENT-----------------------
# Functions
import cloud_storage_cost
def calculate_cost():
    try:
        gb = float(entry_cloud1.get())
        c = float(entry_cloud2.get())
    except ValueError as v:
        errors_cloud.configure(text="")
        errors_cloud.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_cloud.configure(text=""))
        return
    
    if gb <= 0 or c <= 0:
        errors_cloud.configure(text="")
        errors_cloud.configure(text=f"Error: Values must be greater than zero")
        app.after(3000, lambda:errors_cloud.configure(text=""))
        return
    
    cm = cloud_storage_cost.monthly_cost(gb, c)
    montly_cost_results.configure(text=f"{cm:.2f}$")
    anual_cost_results.configure(text=f"{cloud_storage_cost.annual_cost(cm):.2f}$")
    
def clean_text_cloud():
    entry_cloud1.delete(0, "end")
    entry_cloud1.focus()
    entry_cloud2.delete(0, "end")
    montly_cost_results.configure(text="00.00$")
    anual_cost_results.configure(text="00.00$")
    
def copy_results_cloud1():
    copy = montly_cost_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_cloud.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_cloud.configure(text="COPY"))
    
def copy_results_cloud2():
    copy = anual_cost_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_cloud2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_cloud2.configure(text="COPY"))

# Title
title2 = ctk.CTkLabel(
    pages["cloud_storage_cost_page"], 
    text="CLOUD STORAGE COST", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#aa55ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title2.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input2 = ctk.CTkFrame(
    pages["cloud_storage_cost_page"],
    width=600, height=170,
    border_color="#aa55ff",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input2 = ctk.CTkLabel(
    frame_input2, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#f0e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input2.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_cloud = ctk.CTkLabel(
    frame_input2, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=150,
    justify=tk.LEFT,
    text_color="#f0e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_cloud.place(relx=0.83, rely=0.34, anchor=tk.CENTER)

# Orders
order_cloud_1 = ctk.CTkLabel(
    frame_input2, 
    text="Enter stored data in GB:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#f0e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_cloud_1.place(relx=0.2, rely=0.33, anchor=tk.CENTER)
order_cloud_2 = ctk.CTkLabel(
    frame_input2, 
    text="Enter cost per GB:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#f0e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_cloud_2.place(relx=0.2, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_cloud1 = ctk.CTkEntry(
    frame_input2, 
    placeholder_text="0.0",
    fg_color="#2e1a4d",                 
    text_color="#f0e6ff",               
    border_color="#aa55ff",             
    placeholder_text_color="#f0e6ff")
entry_cloud1.place(relx=0.55, rely=0.33, anchor=tk.CENTER)
entry_cloud2 = ctk.CTkEntry(
    frame_input2, 
    placeholder_text="0.0",
    fg_color="#2e1a4d",                 
    text_color="#ffffff",               
    border_color="#aa55ff",             
    placeholder_text_color="#f0e6ff")
entry_cloud2.place(relx=0.55, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate = ctk.CTkButton(
    frame_input2,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#aa55ff",
    bg_color="#1a1a2e",
    hover_color="#c799ff",
    command=calculate_cost)
button_calculate.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean2 = ctk.CTkButton(
    frame_input2,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#f0e6ff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_cloud)
button_clean2.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results2 = ctk.CTkFrame(
    pages["cloud_storage_cost_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results2.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results = ctk.CTkLabel(
    frame_results2, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#f0e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Montly cost results
montly_cost = ctk.CTkLabel(
    frame_results2, 
    text="The monthly cost is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#f0e6ff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
montly_cost.place(relx=0.23, rely=0.43, anchor=tk.CENTER)

montly_cost_results = ctk.CTkLabel(
    frame_results2,
    text="00.00$",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#aa55ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
montly_cost_results.place(relx=0.52, rely=0.43, anchor=tk.CENTER)

button_copy_cloud = ctk.CTkButton(
    frame_results2,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#aa55ff",
    bg_color="#1a1a2e",
    hover_color="#c799ff",
    command=copy_results_cloud1)
button_copy_cloud.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Anual cost results
anual_cost = ctk.CTkLabel(
    frame_results2, 
    text="The annual cost is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#f0e6ff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
anual_cost.place(relx=0.23, rely=0.80, anchor=tk.CENTER)

anual_cost_results = ctk.CTkLabel(
    frame_results2,
    text="00.00$",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#aa55ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
anual_cost_results.place(relx=0.52, rely=0.80, anchor=tk.CENTER)

button_copy_cloud2 = ctk.CTkButton(
    frame_results2,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#f0e6ff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_cloud2)
button_copy_cloud2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button2 = ctk.CTkButton(
    pages["cloud_storage_cost_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#aa55ff",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#aa55ff",
    command=lambda: show_page("menu_page"))
return_button2.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# EXECUTION TIME CALCULATOR PAGE CONTENT-----------------------
# Functions
import execution_time_calculator
def calculate_execution():
    try:
        n = float(entry_exe1.get())
        v = float(entry_exe2.get())
    except ValueError as v:
        errors_exe.configure(text="")
        errors_exe.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_exe.configure(text=""))
        return
    
    if n <= 0 or v <= 0:
        errors_exe.configure(text="")
        errors_exe.configure(text=f"Error: Values must be greater than zero")
        app.after(3000, lambda:errors_exe.configure(text=""))
        return
    
    ts = execution_time_calculator.time_seconds(n,v)
    time_seconds_results.configure(text=f"{ts:.2f}s")
    time_minutes_results.configure(text=f"{execution_time_calculator.time_minutes(ts):.2f}min")
    
def clean_text_exe():
    entry_exe1.delete(0, "end")
    entry_exe1.focus()
    entry_exe2.delete(0, "end")
    time_seconds_results.configure(text="00.00s")
    time_minutes_results.configure(text="00.00min")
    
def copy_results_exe1():
    copy = time_seconds_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_exe.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_exe.configure(text="COPY"))
    
def copy_results_exe2():
    copy = time_minutes_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_exe2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_exe2.configure(text="COPY"))

# Title
title3 = ctk.CTkLabel(
    pages["execution_time_calculator_page"], 
    text="PROGRAM EXECUTION TIME CALCULATOR", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=26, weight="bold"), 
    text_color="#ffff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title3.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input3 = ctk.CTkFrame(
    pages["execution_time_calculator_page"],
    width=600, height=170,
    border_color="#ffff55",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input3.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input3 = ctk.CTkLabel(
    frame_input3, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input3.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_exe = ctk.CTkLabel(
    frame_input3, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_exe.place(relx=0.86, rely=0.34, anchor=tk.CENTER)

# Orders
order_exe_1 = ctk.CTkLabel(
    frame_input3, 
    text="Enter the number of operations:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_exe_1.place(relx=0.22, rely=0.33, anchor=tk.CENTER)
order_exe_2 = ctk.CTkLabel(
    frame_input3, 
    text="Enter execution speed (operations/second):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_exe_2.place(relx=0.28, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_exe1 = ctk.CTkEntry(
    frame_input3, 
    placeholder_text="0.0",
    width=100,
    fg_color="#333311",                 
    text_color="#ffffff",               
    border_color="#ffff55",             
    placeholder_text_color="#ffffff")
entry_exe1.place(relx=0.64, rely=0.33, anchor=tk.CENTER)
entry_exe2 = ctk.CTkEntry(
    frame_input3, 
    placeholder_text="0.0",
    width=100,
    fg_color="#333311",                 
    text_color="#ffffff",               
    border_color="#ffff55",             
    placeholder_text_color="#ffffff")
entry_exe2.place(relx=0.64, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_exe = ctk.CTkButton(
    frame_input3,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ffff55",
    bg_color="#1a1a2e",
    hover_color="#ffffa2",
    command=calculate_execution)
button_calculate_exe.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean3 = ctk.CTkButton(
    frame_input3,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_exe)
button_clean3.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results3 = ctk.CTkFrame(
    pages["execution_time_calculator_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results3.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_exe = ctk.CTkLabel(
    frame_results3, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_exe.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Time seconds results
time_seconds = ctk.CTkLabel(
    frame_results3, 
    text="The time in seconds is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
time_seconds.place(relx=0.23, rely=0.43, anchor=tk.CENTER)

time_seconds_results = ctk.CTkLabel(
    frame_results3,
    text="00.00s",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
time_seconds_results.place(relx=0.52, rely=0.43, anchor=tk.CENTER)

button_copy_exe = ctk.CTkButton(
    frame_results3,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ffff55",
    bg_color="#1a1a2e",
    hover_color="#ffffa2",
    command=copy_results_exe1)
button_copy_exe.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Time minutes results
time_minutes = ctk.CTkLabel(
    frame_results3, 
    text="The time in minutes is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
time_minutes.place(relx=0.23, rely=0.80, anchor=tk.CENTER)

time_minutes_results = ctk.CTkLabel(
    frame_results3,
    text="00.00min",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
time_minutes_results.place(relx=0.52, rely=0.80, anchor=tk.CENTER)

button_copy_exe2 = ctk.CTkButton(
    frame_results3,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_exe2)
button_copy_exe2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button3 = ctk.CTkButton(
    pages["execution_time_calculator_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#ffff55",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#ffff55",
    command=lambda: show_page("menu_page"))
return_button3.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# EUCLIDEAN DISTANCE CALCULATOR PAGE CONTENT-----------------------
# Functions
import euclidean_distance_calculator
def calculate_euclidean():
    try:
        x1 = float(entry_euclidean1.get())
        y1 = float(entry_euclidean2.get())
        x2 = float(entry_euclidean3.get())
        y2 = float(entry_euclidean4.get())
    except ValueError as v:
        errors_euclidean.configure(text="")
        errors_euclidean.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_euclidean.configure(text=""))
        return
    
    coordinates_results.configure(text=f"(P1: {entry_euclidean1.get()}, {entry_euclidean2.get()} | P2: {entry_euclidean3.get()}, {entry_euclidean4.get()})")
    euclidean_distance_results.configure(text=f"{euclidean_distance_calculator.euclidean_distance(x1, y1, x2, y2):.2f}")
    
def clean_text_euclidean():
    entry_euclidean1.delete(0, "end")
    entry_euclidean2.delete(0, "end")
    entry_euclidean3.delete(0, "end")
    entry_euclidean4.delete(0, "end")
    entry_euclidean1.focus()
    coordinates_results.configure(text="(P1: 0, 0 | P2: 0, 0)")
    euclidean_distance_results.configure(text="00.00")
    
def copy_results_euclidean1():
    copy = coordinates_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_euclidean.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_euclidean.configure(text="COPY"))
    
def copy_results_euclidean2():
    copy = euclidean_distance_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_euclidean2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_euclidean2.configure(text="COPY"))

# Title
title4 = ctk.CTkLabel(
    pages["euclidean_distance_calculator_page"], 
    text="EUCLIDEAN DISTANCE CALCULATOR", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#55ff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title4.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input4 = ctk.CTkFrame(
    pages["euclidean_distance_calculator_page"],
    width=600, height=170,
    border_color="#55ff55",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input4.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input4 = ctk.CTkLabel(
    frame_input4, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input4.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_euclidean = ctk.CTkLabel(
    frame_input4, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_euclidean.place(relx=0.86, rely=0.34, anchor=tk.CENTER)

# Orders
order_euclidean1 = ctk.CTkLabel(
    frame_input4, 
    text="Enter the value of point 1 - x1:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_euclidean1.place(relx=0.21, rely=0.33, anchor=tk.CENTER)
order_euclidean2 = ctk.CTkLabel(
    frame_input4, 
    text="y1:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_euclidean2.place(relx=0.57, rely=0.33, anchor=tk.CENTER)
order_euclidean3 = ctk.CTkLabel(
    frame_input4, 
    text="Enter the value of point 2 - x2:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_euclidean3.place(relx=0.21, rely=0.53, anchor=tk.CENTER)
order_euclidean4 = ctk.CTkLabel(
    frame_input4, 
    text="y2:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_euclidean4.place(relx=0.57, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_euclidean1 = ctk.CTkEntry(
    frame_input4, 
    placeholder_text="0.0",
    width=60,
    fg_color="#113311",                 
    text_color="#e6ffe6",               
    border_color="#55ff55",             
    placeholder_text_color="#e6ffe6")
entry_euclidean1.place(relx=0.47, rely=0.33, anchor=tk.CENTER)
entry_euclidean2 = ctk.CTkEntry(
    frame_input4, 
    placeholder_text="0.0",
    width=60,
    fg_color="#113311",                 
    text_color="#e6ffe6",               
    border_color="#55ff55",             
    placeholder_text_color="#e6ffe6")
entry_euclidean2.place(relx=0.67, rely=0.33, anchor=tk.CENTER)
entry_euclidean3 = ctk.CTkEntry(
    frame_input4, 
    placeholder_text="0.0",
    width=60,
    fg_color="#113311",                 
    text_color="#e6ffe6",               
    border_color="#55ff55",             
    placeholder_text_color="#e6ffe6")
entry_euclidean3.place(relx=0.47, rely=0.53, anchor=tk.CENTER)
entry_euclidean4 = ctk.CTkEntry(
    frame_input4, 
    placeholder_text="0.0",
    width=60,
    fg_color="#113311",                 
    text_color="#e6ffe6",               
    border_color="#55ff55",             
    placeholder_text_color="#e6ffe6")
entry_euclidean4.place(relx=0.67, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_euclidean = ctk.CTkButton(
    frame_input4,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#55ff55",
    bg_color="#1a1a2e",
    hover_color="#99ff99",
    command=calculate_euclidean)
button_calculate_euclidean.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean4 = ctk.CTkButton(
    frame_input4,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#e6ffe6",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_euclidean)
button_clean4.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results4 = ctk.CTkFrame(
    pages["euclidean_distance_calculator_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results4.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_euclidean = ctk.CTkLabel(
    frame_results4, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6ffe6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_euclidean.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Coordinates results
coordinates = ctk.CTkLabel(
    frame_results4, 
    text="Coordinates:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#e6ffe6",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
coordinates.place(relx=0.15, rely=0.43, anchor=tk.CENTER)

coordinates_results = ctk.CTkLabel(
    frame_results4,
    text="(P1: 0, 0 | P2: 0, 0)",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#55ff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
coordinates_results.place(relx=0.46, rely=0.43, anchor=tk.CENTER)

button_copy_euclidean = ctk.CTkButton(
    frame_results4,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#55ff55",
    bg_color="#1a1a2e",
    hover_color="#99ff99",
    command=copy_results_euclidean1)
button_copy_euclidean.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Euclidean distance results
euclidean_distance = ctk.CTkLabel(
    frame_results4, 
    text="The Euclidean distance is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#e6ffe6",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
euclidean_distance.place(relx=0.19, rely=0.80, anchor=tk.CENTER)

euclidean_distance_results = ctk.CTkLabel(
    frame_results4,
    text="00.00",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#55ff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
euclidean_distance_results.place(relx=0.50, rely=0.80, anchor=tk.CENTER)

button_copy_euclidean2 = ctk.CTkButton(
    frame_results4,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#e6ffe6",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_euclidean2)
button_copy_euclidean2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button4 = ctk.CTkButton(
    pages["euclidean_distance_calculator_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#55ff55",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#55ff55",
    command=lambda: show_page("menu_page"))
return_button4.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# AVERAGE GRADE PAGE CONTENT-----------------------
# Functions
import average_grade
def calculate_grades():
    try:
        n1 = float(entry_grade1.get())
        n2 = float(entry_grade2.get())
        n3 = float(entry_grade3.get())
        n4 = float(entry_grade4.get())
    except ValueError as v:
        errors_grade.configure(text="")
        errors_grade.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_grade.configure(text=""))
        return
    
    if n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0:
        errors_grade.configure(text="Error: Please enter only numbers greater than or equal to zero")
        app.after(3000, lambda:errors_grade.configure(text=""))
        return
    
    grades_results.configure(text=f"(G1: {entry_grade1.get()}| G2: {entry_grade2.get()}| G3: {entry_grade3.get()}| G4: {entry_grade4.get()})")
    average_grade_results.configure(text=f"{average_grade.calculate_average(n1, n2, n3, n4):.2f}")
    
def clean_text_grade():
    entry_grade1.delete(0, "end")
    entry_grade2.delete(0, "end")
    entry_grade3.delete(0, "end")
    entry_grade4.delete(0, "end")
    entry_grade1.focus()
    grades_results.configure(text="(G1: 0| G2: 0| G3: 0| G4: 0)")
    average_grade_results.configure(text="00.00")
    
def copy_results_grade1():
    copy = grades_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_grades.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_grades.configure(text="COPY"))
    
def copy_results_grade2():
    copy = average_grade_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_grades2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_grades2.configure(text="COPY"))

# Title
title5 = ctk.CTkLabel(
    pages["average_grade_page"], 
    text="AVERAGE GRADE CALCULATOR", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#ff55aa", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title5.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input5 = ctk.CTkFrame(
    pages["average_grade_page"],
    width=600, height=170,
    border_color="#ff55aa",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input5.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input5 = ctk.CTkLabel(
    frame_input5, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input5.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_grade = ctk.CTkLabel(
    frame_input5, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_grade.place(relx=0.86, rely=0.34, anchor=tk.CENTER)

# Orders
order_grade1 = ctk.CTkLabel(
    frame_input5, 
    text="Enter the value of the grade 1:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_grade1.place(relx=0.21, rely=0.33, anchor=tk.CENTER)
order_grade2 = ctk.CTkLabel(
    frame_input5, 
    text="2:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_grade2.place(relx=0.57, rely=0.33, anchor=tk.CENTER)
order_grade3 = ctk.CTkLabel(
    frame_input5, 
    text="Enter the value of the grade 3:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_grade3.place(relx=0.21, rely=0.53, anchor=tk.CENTER)
order_grade4 = ctk.CTkLabel(
    frame_input5, 
    text="4:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_grade4.place(relx=0.57, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_grade1 = ctk.CTkEntry(
    frame_input5, 
    placeholder_text="0.0",
    width=60,
    fg_color="#44112b",                 
    text_color="#ffffff",               
    border_color="#ff55aa",             
    placeholder_text_color="#ffffff")
entry_grade1.place(relx=0.47, rely=0.33, anchor=tk.CENTER)
entry_grade2 = ctk.CTkEntry(
    frame_input5, 
    placeholder_text="0.0",
    width=60,
    fg_color="#44112b",                 
    text_color="#ffffff",               
    border_color="#ff55aa",             
    placeholder_text_color="#ffffff")
entry_grade2.place(relx=0.67, rely=0.33, anchor=tk.CENTER)
entry_grade3 = ctk.CTkEntry(
    frame_input5, 
    placeholder_text="0.0",
    width=60,
    fg_color="#44112b",                 
    text_color="#ffffff",               
    border_color="#ff55aa",             
    placeholder_text_color="#ffffff")
entry_grade3.place(relx=0.47, rely=0.53, anchor=tk.CENTER)
entry_grade4 = ctk.CTkEntry(
    frame_input5, 
    placeholder_text="0.0",
    width=60,
    fg_color="#44112b",                 
    text_color="#ffffff",               
    border_color="#ff55aa",             
    placeholder_text_color="#ffffff")
entry_grade4.place(relx=0.67, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_grade = ctk.CTkButton(
    frame_input5,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ff55aa",
    bg_color="#1a1a2e",
    hover_color="#ff99cc",
    command=calculate_grades)
button_calculate_grade.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean5 = ctk.CTkButton(
    frame_input5,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_grade)
button_clean5.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results5 = ctk.CTkFrame(
    pages["average_grade_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results5.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_grade = ctk.CTkLabel(
    frame_results5, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_grade.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Grades results
grades = ctk.CTkLabel(
    frame_results5, 
    text="Grades:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
grades.place(relx=0.15, rely=0.43, anchor=tk.CENTER)

grades_results = ctk.CTkLabel(
    frame_results5,
    text="(G1: 0| G2: 0| G3: 0| G4: 0)",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ff55aa", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
grades_results.place(relx=0.46, rely=0.43, anchor=tk.CENTER)

button_copy_grades = ctk.CTkButton(
    frame_results5,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ff55aa",
    bg_color="#1a1a2e",
    hover_color="#ff99cc",
    command=copy_results_grade1)
button_copy_grades.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Average grade results
average = ctk.CTkLabel(
    frame_results5, 
    text="The average grade is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
average.place(relx=0.19, rely=0.80, anchor=tk.CENTER)

average_grade_results = ctk.CTkLabel(
    frame_results5,
    text="00.00",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ff55aa", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
average_grade_results.place(relx=0.50, rely=0.80, anchor=tk.CENTER)

button_copy_grades2 = ctk.CTkButton(
    frame_results5,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_grade2)
button_copy_grades2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button5 = ctk.CTkButton(
    pages["average_grade_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#ff55aa",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#ff55aa",
    command=lambda: show_page("menu_page"))
return_button5.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# SIMPLE INTEREST CALCULATOR PAGE CONTENT-----------------------
# Functions
import simple_interest_calculator
def calculate_interest():
    try:
        c = float(entry_interest1.get())
        i = float(entry_interest3.get())
        t = float(entry_interest2.get())
    except ValueError as v:
        errors_interest.configure(text="")
        errors_interest.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_interest.configure(text=""))
        return
    
    if c <= 0 or i <= 0 or t <= 0:
        errors_interest.configure(text="Error: All values must be greater than zero")
        app.after(3000, lambda:errors_interest.configure(text=""))
        return
    
    i = simple_interest_calculator.rate_percentage(i)
    m = simple_interest_calculator.calculate_total_amount(c, i ,t)
    
    interest_results.configure(text=f"{m-c:.2f}$")
    amount_results.configure(text=f"{m:.2f}$")
    
def clean_text_interest():
    entry_interest1.delete(0, "end")
    entry_interest2.delete(0, "end")
    entry_interest3.delete(0, "end")
    entry_interest1.focus()
    interest_results.configure(text="00.00$")
    amount_results.configure(text="00.00$")
    
def copy_results_interest1():
    copy = interest_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_interest.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_interest.configure(text="COPY"))
    
def copy_results_interest2():
    copy = amount_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_interest2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_interest2.configure(text="COPY"))

# Title
title6 = ctk.CTkLabel(
    pages["simple_interest_calculator_page"], 
    text="SIMPLE INTEREST CALCULATOR", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#ffaa00", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title6.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input6 = ctk.CTkFrame(
    pages["simple_interest_calculator_page"],
    width=600, height=170,
    border_color="#ffaa00",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input6.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input6 = ctk.CTkLabel(
    frame_input6, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#fff5e6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input6.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_interest = ctk.CTkLabel(
    frame_input6, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#fff5e6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_interest.place(relx=0.86, rely=0.34, anchor=tk.CENTER)

# Orders
order_interest1 = ctk.CTkLabel(
    frame_input6, 
    text="Enter the initial capital:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#fff5e6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_interest1.place(relx=0.17, rely=0.33, anchor=tk.CENTER)
order_interest2 = ctk.CTkLabel(
    frame_input6, 
    text="Years:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#fff5e6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_interest2.place(relx=0.55, rely=0.33, anchor=tk.CENTER)
order_interest3 = ctk.CTkLabel(
    frame_input6, 
    text="Enter the annual interest rate (%):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#fff5e6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_interest3.place(relx=0.23, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_interest1 = ctk.CTkEntry(
    frame_input6, 
    placeholder_text="0.0",
    width=60,
    fg_color="#442d00",                 
    text_color="#fff5e6",               
    border_color="#ffaa00",             
    placeholder_text_color="#fff5e6")
entry_interest1.place(relx=0.39, rely=0.33, anchor=tk.CENTER)
entry_interest2 = ctk.CTkEntry(
    frame_input6, 
    placeholder_text="0.0",
    width=60,
    fg_color="#442d00",                 
    text_color="#fff5e6",               
    border_color="#ffaa00",             
    placeholder_text_color="#fff5e6")
entry_interest2.place(relx=0.67, rely=0.33, anchor=tk.CENTER)
entry_interest3 = ctk.CTkEntry(
    frame_input6, 
    placeholder_text="0.0",
    width=60,
    fg_color="#442d00",                 
    text_color="#fff5e6",               
    border_color="#ffaa00",             
    placeholder_text_color="#fff5e6")
entry_interest3.place(relx=0.51, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_interest = ctk.CTkButton(
    frame_input6,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ffaa00",
    bg_color="#1a1a2e",
    hover_color="#ffcc66",
    command=calculate_interest)
button_calculate_interest.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean6 = ctk.CTkButton(
    frame_input6,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#fff5e6",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_interest)
button_clean6.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results6 = ctk.CTkFrame(
    pages["simple_interest_calculator_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results6.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_interest = ctk.CTkLabel(
    frame_results6, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#fff5e6", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_interest.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Interest Earned results
interest = ctk.CTkLabel(
    frame_results6, 
    text="The interest earned is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#fff5e6",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
interest.place(relx=0.17, rely=0.43, anchor=tk.CENTER)

interest_results = ctk.CTkLabel(
    frame_results6,
    text="00.00$",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffaa00", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
interest_results.place(relx=0.52, rely=0.43, anchor=tk.CENTER)

button_copy_interest = ctk.CTkButton(
    frame_results6,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#ffaa00",
    bg_color="#1a1a2e",
    hover_color="#ffcc66",
    command=copy_results_interest1)
button_copy_interest.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Total Amount results
amount = ctk.CTkLabel(
    frame_results6, 
    text="The total amount to be paid is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#fff5e6",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
amount.place(relx=0.22, rely=0.80, anchor=tk.CENTER)

amount_results = ctk.CTkLabel(
    frame_results6,
    text="00.00$",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffaa00", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
amount_results.place(relx=0.52, rely=0.80, anchor=tk.CENTER)

button_copy_interest2 = ctk.CTkButton(
    frame_results6,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#fff5e6",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_interest2)
button_copy_interest2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button6 = ctk.CTkButton(
    pages["simple_interest_calculator_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#ffaa00",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#ffaa00",
    command=lambda: show_page("menu_page"))
return_button6.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# AVERAGE SPEED OF A DRONE PAGE CONTENT-----------------------
# Functions
import average_speed_of_a_drone
def calculate_speed():
    try:
        d = float(entry_speed1.get())
        t = float(entry_speed2.get())
    except ValueError as v:
        errors_speed.configure(text="")
        errors_speed.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_speed.configure(text=""))
        return
    
    if d <= 0 or t <= 0:
        errors_speed.configure(text="Error: All values must be greater than zero")
        app.after(3000, lambda:errors_speed.configure(text=""))
        return
    
    vkm = average_speed_of_a_drone.speed_kmh(d, t)
    
    kmh_results.configure(text=f"{vkm:.2f}km/h")
    ms_results.configure(text=f"{average_speed_of_a_drone.speed_ms(vkm):.2f}m/s")
    
def clean_text_speed():
    entry_speed1.delete(0, "end")
    entry_speed2.delete(0, "end")
    entry_speed1.focus()
    kmh_results.configure(text="00.00km/h")
    ms_results.configure(text="00.00m/s")
    
def copy_results_speed1():
    copy = kmh_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_speed.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_speed.configure(text="COPY"))
    
def copy_results_speed2():
    copy = ms_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_speed2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_speed2.configure(text="COPY"))

# Title
title7 = ctk.CTkLabel(
    pages["average_speed_of_a_drone_page"], 
    text="AVERAGE SPEED OF A DRONE", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#55ffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title7.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input7 = ctk.CTkFrame(
    pages["average_speed_of_a_drone_page"],
    width=600, height=170,
    border_color="#55ffff",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input7.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input7 = ctk.CTkLabel(
    frame_input7, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input7.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_speed = ctk.CTkLabel(
    frame_input7, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_speed.place(relx=0.80, rely=0.34, anchor=tk.CENTER)

# Orders
order_speed1 = ctk.CTkLabel(
    frame_input7, 
    text="Enter the distance traveled (km):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_speed1.place(relx=0.23, rely=0.33, anchor=tk.CENTER)
order_speed2 = ctk.CTkLabel(
    frame_input7, 
    text="Enter the time taken (hours):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_speed2.place(relx=0.21, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_speed1 = ctk.CTkEntry(
    frame_input7, 
    placeholder_text="0.0",
    width=60,
    fg_color="#113333",                 
    text_color="#ffffff",               
    border_color="#55ffff",             
    placeholder_text_color="#ffffff")
entry_speed1.place(relx=0.51, rely=0.33, anchor=tk.CENTER)
entry_speed2 = ctk.CTkEntry(
    frame_input7, 
    placeholder_text="0.0",
    width=60,
    fg_color="#113333",                 
    text_color="#ffffff",               
    border_color="#55ffff",             
    placeholder_text_color="#ffffff")
entry_speed2.place(relx=0.51, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_speed = ctk.CTkButton(
    frame_input7,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#55ffff",
    bg_color="#1a1a2e",
    hover_color="#a2ffff",
    command=calculate_speed)
button_calculate_speed.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean7 = ctk.CTkButton(
    frame_input7,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_speed)
button_clean7.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results7 = ctk.CTkFrame(
    pages["average_speed_of_a_drone_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results7.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_speed = ctk.CTkLabel(
    frame_results7, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_speed.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Average speed km/h results
kmh = ctk.CTkLabel(
    frame_results7, 
    text="Average speed in km/h:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
kmh.place(relx=0.18, rely=0.43, anchor=tk.CENTER)

kmh_results = ctk.CTkLabel(
    frame_results7,
    text="00.00km/h",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#55ffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
kmh_results.place(relx=0.50, rely=0.43, anchor=tk.CENTER)

button_copy_speed = ctk.CTkButton(
    frame_results7,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#55ffff",
    bg_color="#1a1a2e",
    hover_color="#a2ffff",
    command=copy_results_speed1)
button_copy_speed.place(relx=0.8, rely=0.43, anchor=tk.CENTER)

# Average speed in m/s results
ms = ctk.CTkLabel(
    frame_results7, 
    text="Average speed in m/s:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=200,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
ms.place(relx=0.19, rely=0.80, anchor=tk.CENTER)

ms_results = ctk.CTkLabel(
    frame_results7,
    text="00.00m/s",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#55ffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
ms_results.place(relx=0.50, rely=0.80, anchor=tk.CENTER)

button_copy_speed2 = ctk.CTkButton(
    frame_results7,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_speed2)
button_copy_speed2.place(relx=0.8, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button7 = ctk.CTkButton(
    pages["average_speed_of_a_drone_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#55ffff",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#55ffff",
    command=lambda: show_page("menu_page"))
return_button7.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# BODY MASS INDEX CALCULATOR PAGE CONTENT-----------------------
# Functions
import body_mass_index_calculator
def calculate_index():
    try:
        p = float(entry_index1.get())
        h = float(entry_index2.get())
    except ValueError as v:
        errors_index.configure(text="")
        errors_index.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_index.configure(text=""))
        return
    
    if not 15 <= p <= 635:
        errors_index.configure(text="Error: Weight must be between 15 and 635 kg")
        app.after(3000, lambda:errors_index.configure(text=""))
        return
    
    if not 0.5 <= h <= 2.72:
        errors_index.configure(text="Height must be between 0.5 and 2.72 m")
        app.after(3000, lambda:errors_index.configure(text=""))
        return
    
    l = ["Underweight",  "Normal Weight", "Overweight", "Obesity"]
    
    imc = body_mass_index_calculator.calculate_imc(p, h)
    results = body_mass_index_calculator.results_imc(l, imc)
    
    bodymi_results.configure(text=f"{imc:.2f} | {results}")
    
def clean_text_index():
    entry_index1.delete(0, "end")
    entry_index2.delete(0, "end")
    entry_index1.focus()
    bodymi_results.configure(text="00.00 | Category")
    
def copy_results_index1():
    copy = bodymi_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_index1.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_index1.configure(text="COPY"))
    
def copy_results_index2():
    copy = table_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_index2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_index2.configure(text="COPY"))

# Title
title8 = ctk.CTkLabel(
    pages["body_mass_index_calculator_page"], 
    text="BODY MASS INDEX CALCULATOR", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#5555ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title8.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input8 = ctk.CTkFrame(
    pages["body_mass_index_calculator_page"],
    width=600, height=170,
    border_color="#5555ff",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input8.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input8 = ctk.CTkLabel(
    frame_input8, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input8.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_index = ctk.CTkLabel(
    frame_input8, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#e6e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_index.place(relx=0.80, rely=0.34, anchor=tk.CENTER)

# Orders
order_index1 = ctk.CTkLabel(
    frame_input8, 
    text="Enter the weight in kilograms(kg):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_index1.place(relx=0.23, rely=0.33, anchor=tk.CENTER)
order_index2 = ctk.CTkLabel(
    frame_input8, 
    text="Enter the height in meters(m):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_index2.place(relx=0.21, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_index1 = ctk.CTkEntry(
    frame_input8, 
    placeholder_text="0.0",
    width=60,
    fg_color="#111144",                 
    text_color="#e6e6ff",               
    border_color="#5555ff",             
    placeholder_text_color="#e6e6ff")
entry_index1.place(relx=0.51, rely=0.33, anchor=tk.CENTER)
entry_index2 = ctk.CTkEntry(
    frame_input8, 
    placeholder_text="0.0",
    width=60,
    fg_color="#111144",                 
    text_color="#e6e6ff",               
    border_color="#5555ff",             
    placeholder_text_color="#e6e6ff")
entry_index2.place(relx=0.51, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_index = ctk.CTkButton(
    frame_input8,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#5555ff",
    bg_color="#1a1a2e",
    hover_color="#9999ff",
    command=calculate_index)
button_calculate_index.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean8 = ctk.CTkButton(
    frame_input8,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#e6e6ff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_index)
button_clean8.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results8 = ctk.CTkFrame(
    pages["body_mass_index_calculator_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results8.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_index = ctk.CTkLabel(
    frame_results8, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#e6e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_index.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# IMC km/h results
bodymi = ctk.CTkLabel(
    frame_results8, 
    text="The Body Mass Index is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#e6e6ff",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
bodymi.place(relx=0.17, rely=0.43, anchor=tk.CENTER)

bodymi_results = ctk.CTkLabel(
    frame_results8,
    text="00.00 | Category",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#5555ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
bodymi_results.place(relx=0.49, rely=0.43, anchor=tk.CENTER)

button_copy_index1 = ctk.CTkButton(
    frame_results8,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#5555ff",
    bg_color="#1a1a2e",
    hover_color="#9999ff",
    command=copy_results_index1)
button_copy_index1.place(relx=0.82, rely=0.43, anchor=tk.CENTER)

# Table results
table_results = ctk.CTkLabel(
    frame_results8,
    text=f"IMC Table: \nUnderweight: < 18.5 | Normal weight: 18.5 - 24.9 Overweight: 25.0 - 29.9 | Obesity: ≥ 30.0",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    wraplength=340,
    justify="left",
    text_color="#e6e6ff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
table_results.place(relx=0.31, rely=0.79, anchor=tk.CENTER)

button_copy_index2 = ctk.CTkButton(
    frame_results8,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#e6e6ff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_index2)
button_copy_index2.place(relx=0.82, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button8 = ctk.CTkButton(
    pages["body_mass_index_calculator_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#5555ff",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#5555ff",
    command=lambda: show_page("menu_page"))
return_button8.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# CALCULATOR ENERGY CONSUMPTION OF A COMPUTER PAGE CONTENT-----------------------
# Functions
import calculator_energy_consumption_of_a_computer
def calculate_energy():
    try:
        h = float(entry_energy1.get())
        p = float(entry_energy2.get())
    except ValueError as v:
        errors_energy.configure(text="")
        errors_energy.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_energy.configure(text=""))
        return
    
    if not 0 < h <= 24:
        errors_energy.configure(text="Error: Hours must be between 0 and 24")
        app.after(3000, lambda:errors_energy.configure(text=""))
        return
    
    if not 0 < p <= 2500:
        errors_energy.configure(text="Error: Enter a realistic power value (between 1W and 2500W)")
        app.after(3000, lambda:errors_energy.configure(text=""))
        return
    
    dailyp_results.configure(text=f"{h}h | {p}W")
    consumption_results.configure(text=f"{calculator_energy_consumption_of_a_computer.energy_consumption(p, h):.2f}kWh")
    
def clean_text_energy():
    entry_energy1.delete(0, "end")
    entry_energy2.delete(0, "end")
    entry_energy1.focus()
    dailyp_results.configure(text="00.00h | 00.00W")
    consumption_results.configure(text="00.00kWh")
    
def copy_results_energy1():
    copy = dailyp_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_energy1.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_energy1.configure(text="COPY"))
    
def copy_results_energy2():
    copy = consumption_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_energy2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_energy2.configure(text="COPY"))

# Title
title9 = ctk.CTkLabel(
    pages["energy_consumption_page"], 
    text="ENERGY CONSUMPTION OF A COMPUTER", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=26, weight="bold"), 
    text_color="#aaff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title9.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input9 = ctk.CTkFrame(
    pages["energy_consumption_page"],
    width=600, height=170,
    border_color="#aaff55",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input9.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input9 = ctk.CTkLabel(
    frame_input9, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input9.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_energy = ctk.CTkLabel(
    frame_input9, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_energy.place(relx=0.86, rely=0.34, anchor=tk.CENTER)

# Orders
order_energy1 = ctk.CTkLabel(
    frame_input9, 
    text="Enter the hours of the computer operates a day:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_energy1.place(relx=0.31, rely=0.33, anchor=tk.CENTER)
order_energy2 = ctk.CTkLabel(
    frame_input9, 
    text="Enter the value of the power of the computer (W):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_energy2.place(relx=0.32, rely=0.53, anchor=tk.CENTER)
# Entrys orders
entry_energy1 = ctk.CTkEntry(
    frame_input9, 
    placeholder_text="0.0",
    width=60,
    fg_color="#223311",                 
    text_color="#ffffff",               
    border_color="#aaff55",             
    placeholder_text_color="#ffffff")
entry_energy1.place(relx=0.67, rely=0.33, anchor=tk.CENTER)
entry_energy2 = ctk.CTkEntry(
    frame_input9, 
    placeholder_text="0.0",
    width=60,
    fg_color="#223311",                 
    text_color="#ffffff",               
    border_color="#aaff55",             
    placeholder_text_color="#ffffff")
entry_energy2.place(relx=0.68, rely=0.53, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_energy = ctk.CTkButton(
    frame_input9,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#0a0a2a",
    corner_radius=25,
    fg_color="#aaff55",
    bg_color="#1a1a2e",
    hover_color="#ccff99",
    command=calculate_energy)
button_calculate_energy.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean9 = ctk.CTkButton(
    frame_input9,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_energy)
button_clean9.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results9 = ctk.CTkFrame(
    pages["energy_consumption_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results9.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_energy = ctk.CTkLabel(
    frame_results9, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_energy.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Daily usage and Power consumption results
dailyp = ctk.CTkLabel(
    frame_results9, 
    text="Daily usage | Power consumption:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=160,
    wraplength=150,
    justify="left",
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
dailyp.place(relx=0.15, rely=0.43, anchor=tk.CENTER)

dailyp_results = ctk.CTkLabel(
    frame_results9,
    text="00.00h | 00.00W",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#aaff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
dailyp_results.place(relx=0.47, rely=0.43, anchor=tk.CENTER)

button_copy_energy1 = ctk.CTkButton(
    frame_results9,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#aaff55",
    bg_color="#1a1a2e",
    hover_color="#ccff99",
    command=copy_results_energy1)
button_copy_energy1.place(relx=0.82, rely=0.43, anchor=tk.CENTER)

# Monthly consumption results
consumption = ctk.CTkLabel(
    frame_results9, 
    text="The monthly consumption is:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
consumption.place(relx=0.20, rely=0.80, anchor=tk.CENTER)

consumption_results = ctk.CTkLabel(
    frame_results9,
    text="00.00kWh",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"),
    text_color="#aaff55", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
consumption_results.place(relx=0.52, rely=0.79, anchor=tk.CENTER)

button_copy_energy2 = ctk.CTkButton(
    frame_results9,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_energy2)
button_copy_energy2.place(relx=0.82, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button9 = ctk.CTkButton(
    pages["energy_consumption_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#aaff55",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#aaff55",
    command=lambda: show_page("menu_page"))
return_button9.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# CURRENCY CONVERSION PAGE CONTENT-----------------------
# Functions
import currency_conversion
def calculate_currency():
    try:
        m = float(entry_currency1.get())
        t_usd = float(entry_currency2.get())
        t_eur = float(entry_currency3.get())
    except ValueError as v:
        errors_currency.configure(text="")
        errors_currency.configure(text=f"Error: {v}")
        app.after(3000, lambda:errors_currency.configure(text=""))
        return
    
    if m <= 0 or t_usd <= 0 or t_eur <= 0:
        errors_currency.configure(text="Error: All values must be greater than zero")
        app.after(3000, lambda:errors_currency.configure(text=""))
        return
    
    if t_usd > 10 or t_eur > 10:
        errors_currency.configure(text="Warning: Exchange rates seem unusually high (> 10)")
        app.after(3000, lambda:errors_currency.configure(text=""))
        return
    
    local_results.configure(text=f"{m:.2f}")
    dollaeur_results.configure(text=f"{currency_conversion.calculate_usd(m, t_usd):.2f}$ | {currency_conversion.calculate_eur(m, t_eur):.2f}€")
    
def clean_text_currency():
    entry_currency1.delete(0, "end")
    entry_currency2.delete(0, "end")
    entry_currency3.delete(0, "end")
    entry_currency1.focus()
    local_results.configure(text="00.00")
    dollaeur_results.configure(text="00.00$ | 00.00€")
    
def copy_results_currency1():
    copy = local_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_currency1.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_currency1.configure(text="COPY"))
    
def copy_results_currency2():
    copy = dollaeur_results.cget("text")
    app.clipboard_clear()
    app.clipboard_append(copy)
    app.update()
    button_copy_currency2.configure(text="COPIED TEXT")
    app.after(2000, lambda:button_copy_currency2.configure(text="COPY"))

# Title
title10 = ctk.CTkLabel(
    pages["currency_conversion_page"], 
    text="CURRENCY CONVERSION", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=28, weight="bold"), 
    text_color="#aaff00", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title10.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

# Input Section
frame_input10 = ctk.CTkFrame(
    pages["currency_conversion_page"],
    width=600, height=170,
    border_color="#aaff00",
    border_width=3,
    corner_radius=10,
    fg_color="#1a1a2e"
)
frame_input10.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Title
title_input10 = ctk.CTkLabel(
    frame_input10, 
    text="Input Section", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_input10.place(relx=0.5, rely=0.13,anchor=tk.CENTER)

# Label for errors
errors_currency = ctk.CTkLabel(
    frame_input10, 
    text="",
    width=150, height=100,
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"),
    wraplength=140,
    justify=tk.LEFT,
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=10)
errors_currency.place(relx=0.86, rely=0.34, anchor=tk.CENTER)

# Orders
order_currency1 = ctk.CTkLabel(
    frame_input10, 
    text="Local currency:", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_currency1.place(relx=0.12, rely=0.33, anchor=tk.CENTER)
order_currency2 = ctk.CTkLabel(
    frame_input10, 
    text="USD rate(e.g., 0.05):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_currency2.place(relx=0.15, rely=0.53, anchor=tk.CENTER)
order_currency3 = ctk.CTkLabel(
    frame_input10, 
    text="EUR rate(e.g., 0.045):", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
order_currency3.place(relx=0.48, rely=0.33, anchor=tk.CENTER)
# Entrys orders
entry_currency1 = ctk.CTkEntry(
    frame_input10, 
    placeholder_text="0.0",
    width=60,
    fg_color="#223300",                 
    text_color="#ffffff",               
    border_color="#aaff00",             
    placeholder_text_color="#ffffff")
entry_currency1.place(relx=0.28, rely=0.33, anchor=tk.CENTER)
entry_currency2 = ctk.CTkEntry(
    frame_input10, 
    placeholder_text="0.0",
    width=60,
    fg_color="#223311",                 
    text_color="#ffffff",               
    border_color="#aaff00",             
    placeholder_text_color="#ffffff")
entry_currency2.place(relx=0.34, rely=0.53, anchor=tk.CENTER)
entry_currency3 = ctk.CTkEntry(
    frame_input10, 
    placeholder_text="0.0",
    width=60,
    fg_color="#223311",                 
    text_color="#ffffff",               
    border_color="#aaff00",             
    placeholder_text_color="#ffffff")
entry_currency3.place(relx=0.68, rely=0.33, anchor=tk.CENTER)
# Button calculate and clean
button_calculate_currency = ctk.CTkButton(
    frame_input10,
    text="CALCULATE",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#0a0a2a",
    corner_radius=25,
    fg_color="#aaff00",
    bg_color="#1a1a2e",
    hover_color="#ccff66",
    command=calculate_currency)
button_calculate_currency.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
button_clean10 = ctk.CTkButton(
    frame_input10,
    text="CLEAN",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=clean_text_currency)
button_clean10.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

# Results panel
frame_results10 = ctk.CTkFrame(
    pages["currency_conversion_page"], 
    width=600, height=150,
    fg_color="#1a1a2e",
    border_color="#555577",
    border_width=3,
    corner_radius=10)
frame_results10.place(relx=0.5, rely=0.66, anchor=tk.CENTER)
# Title
title_results_currency = ctk.CTkLabel(
    frame_results10, 
    text="Results Panel", 
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#ffffff", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
title_results_currency.place(relx=0.5, rely=0.15,anchor=tk.CENTER)

# Local amount results
local = ctk.CTkLabel(
    frame_results10, 
    text="Local Amount:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=160,
    wraplength=150,
    justify="left",
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
local.place(relx=0.15, rely=0.43, anchor=tk.CENTER)

local_results = ctk.CTkLabel(
    frame_results10,
    text="00.00",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"), 
    text_color="#aaff00", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
local_results.place(relx=0.47, rely=0.43, anchor=tk.CENTER)

button_copy_currency1 = ctk.CTkButton(
    frame_results10,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#1a1a2e",
    corner_radius=25,
    fg_color="#aaff00",
    bg_color="#1a1a2e",
    hover_color="#ccff66",
    command=copy_results_currency1)
button_copy_currency1.place(relx=0.82, rely=0.43, anchor=tk.CENTER)

# Dollars and Euros results
dollaeur = ctk.CTkLabel(
    frame_results10, 
    text="Dollars | Euros:", 
    font=ctk.CTkFont(family="OCR A Extended", size=12, weight="bold"), 
    text_color="#ffffff",
    width=160,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
dollaeur.place(relx=0.15, rely=0.80, anchor=tk.CENTER)

dollaeur_results = ctk.CTkLabel(
    frame_results10,
    text="00.00$ | 00.00€",
    font=ctk.CTkFont(family="OCR A Extended", 
    size=12, weight="bold"),
    text_color="#aaff00", 
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    corner_radius=50)
dollaeur_results.place(relx=0.47, rely=0.79, anchor=tk.CENTER)

button_copy_currency2 = ctk.CTkButton(
    frame_results10,
    text="COPY",
    font=ctk.CTkFont(size=12, weight="bold"),
    width=200,
    height=45,
    text_color="#ffffff",
    corner_radius=25,
    fg_color="#555577",
    bg_color="#1a1a2e",
    hover_color="#444466",
    command=copy_results_currency2)
button_copy_currency2.place(relx=0.82, rely=0.80, anchor=tk.CENTER)

# Return to menu
return_button10 = ctk.CTkButton(
    pages["currency_conversion_page"],
    text="Back to menu",
    font=ctk.CTkFont(size=15, weight="bold"),
    width=195,
    height=45,
    text_color="#aaff00",
    corner_radius=25,
    fg_color="#0a0a2a",
    bg_color="#1a1a2e",
    hover_color="#0e0e3d",
    border_width=3,
    border_color="#aaff00",
    command=lambda: show_page("menu_page"))
return_button10.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

show_page("initial_page")

app.mainloop()