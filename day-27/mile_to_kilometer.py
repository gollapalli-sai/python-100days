import tkinter as tk

def convert_miles_to_km():
    try:
        miles = float(entry_miles.get())
        km = miles * 1.60934
        label_result.config(text=f"{km:.2f} kilometers")
    except ValueError:
        label_result.config(text="Please enter a valid number")

window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.geometry("300x150")
window.resizable(False, False)

label_miles = tk.Label(window, text="Miles:")
label_miles.pack(pady=5)
entry_miles = tk.Entry(window)
entry_miles.pack(pady=5)

button_convert = tk.Button(window, text="Convert", command=convert_miles_to_km)
button_convert.pack(pady=5)

label_result = tk.Label(window, text="")
label_result.pack(pady=5)

window.mainloop()
