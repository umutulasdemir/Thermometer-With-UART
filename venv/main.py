import tkinter as tk
from PIL import Image, ImageTk
# import serial
# import threading

# Set the serial port and baud rate
# ser = serial.Serial('COM3', 115200)

# def read_temperature():
#     while True:
#         try:
#             # Read temperature data from UART
#             temperature_data = ser.readline().decode('utf-8').strip()
#             # Display the temperature on the screen
#             temperature_label.config(text=f"Temperature: {temperature_data} °C")
#         except UnicodeDecodeError:
#             pass  # Ignore characters that cannot be decoded

# Function to exit the application
def exit_application():
    # You can add cleanup or additional actions before exiting here
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Thermometer")

# Set the initial size of the window
window_width = 300
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set background color to gray scale
root.configure(bg="#4F6F7E")

# Load and resize the image
image_path = "venv/thermometer.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((75, 75), Image.BILINEAR)  
new_image = Image.new("RGBA", resized_image.size, "#4F6F7E")
new_image.paste(resized_image.convert("RGBA"), (0, 0), resized_image.convert("RGBA"))
thermometer_image = ImageTk.PhotoImage(new_image)

# Create the temperature label with image
temperature_label = tk.Label(root, text="       Temperature: - °C     ", font=("Montserrat", 19), compound='right', image=thermometer_image, bg="#4F6F7E")
temperature_label.pack(pady=10, padx=10, side='top')


# Create an Exit button with yellow background and increased width
exit_button = tk.Button(root, text="Exit", command=exit_application, font=("Montserrat", 12), highlightbackground="#4F6F7E", background="#FFD700", width=25, height= 1)
exit_button.pack(pady=10, side='bottom')

# # Start the UART reading thread
# uart_thread = threading.Thread(target=read_temperature, daemon=True)
# uart_thread.start()

# Run the window
root.mainloop()

