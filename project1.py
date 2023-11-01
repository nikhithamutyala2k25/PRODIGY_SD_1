from tkinter import *

def open_result_window():
    temp = temp_input.get()
    choice = choice_var.get()

    if temp and choice:
        temp = float(temp)
        choice = int(choice)

        if choice == 1:
            fahrenheit = (temp * 9.0 / 5) + 32
            kelvin = temp + 273.15
            result_text = f"Temperature in Fahrenheit: {fahrenheit:.2f}\nTemperature in Kelvin: {kelvin:.2f}"
        elif choice == 2:
            celsius = (temp - 32) * 5.0 / 9
            kelvin = (temp - 32) * 5.0 / 9 + 273.15
            result_text = f"Temperature in Celsius: {celsius:.2f}\nTemperature in Kelvin: {kelvin:.2f}"
        elif choice == 3:
            celsius = temp - 273.15
            fahrenheit = (temp - 273.15) * 9.0 / 5 + 32
            result_text = f"Temperature in Celsius: {celsius:.2f}\nTemperature in Fahrenheit: {fahrenheit:.2f}"
        else:
            result_text = "Invalid choice. Please select a valid option (1-3)."
    else:
        result_text = "Invalid input. Please enter both temperature and select a unit."

    result_label.config(text=result_text)

# Create a Tkinter window
root = Tk()
root.title("Temperature Converter")

# Set background color to black and window size
root.configure(bg='black')
root.geometry("700x700")  # Set the window size

# Temperature input and unit selection
temp_label = Label(root, text="Enter the temperature value", fg="red", bg='black', font=("Arial", 12))
temp_label.pack(pady=(20, 5))

temp_input = Entry(root, width=50)
temp_input.pack(ipady=6, pady=(1, 15), padx=10)  # Increase input field size

choice_label = Label(root, text="Select Unit of Measurement", fg="red", bg='black', font=("Arial", 12))
choice_label.pack(pady=(20, 5))

choice_var = IntVar()
Radiobutton(root, text="Celsius", variable=choice_var, value=1, fg="red", bg='black', font=("Arial", 12)).pack()
Radiobutton(root, text="Fahrenheit", variable=choice_var, value=2, fg="red", bg='black', font=("Arial", 12)).pack()
Radiobutton(root, text="Kelvin", variable=choice_var, value=3, fg="red", bg='black', font=("Arial", 12)).pack()

# Convert button
convert_button = Button(root, text="Convert", command=open_result_window, fg='white', bg='green', font=("Arial", 12))
convert_button.pack(pady=10)

result_label = Label(root, text="", fg="white", bg='black', font=("Arial", 12))
result_label.pack()

root.mainloop()

