import os
import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_qr():
    name_text = name_entry.get()
    id_text = id_entry.get()
    mobile_text = mobile_entry.get()
    email_text = email_entry.get()
    blood_group_text = blood_group_entry.get()

    data = f"Name: {name_text}\nID: {id_text}\nPhone No.: {mobile_text}\nMail: {email_text}\nBlood Group: {blood_group_text}"

    # Create qrcode folder if not exists
    if not os.path.exists("ID"):
        os.makedirs("ID")

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=7, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = Image.new("RGB", (380, 500), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Add text to the image
    text_lines = data.split('\n')
    y_offset = 10  # Starting y-offset for text
    for line in text_lines:
        draw.text((10, y_offset), line, fill="black", font=font)
        y_offset += 20  # Adjust as needed

    # Paste the QR code onto the image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    img.paste(qr_img, (10, y_offset + 20))

    img_path = os.path.join("ID", f"{name_text}_{id_text}_qr.png")
    img.save(img_path)

    status_label.config(text=f"QR Code generated successfully at {img_path}")

# Create main window
window = tk.Tk()
window.title("ID Card Generator")

# Name Entry
name_label = ttk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
name_entry = ttk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# ID Entry
id_label = ttk.Label(window, text="ID:")
id_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
id_entry = ttk.Entry(window)
id_entry.grid(row=1, column=1, padx=10, pady=10)

# Mobile Entry
mobile_label = ttk.Label(window, text="Mobile:")
mobile_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
mobile_entry = ttk.Entry(window)
mobile_entry.grid(row=2, column=1, padx=10, pady=10)

# Email Entry
email_label = ttk.Label(window, text="Email:")
email_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
email_entry = ttk.Entry(window)
email_entry.grid(row=3, column=1, padx=10, pady=10)

# Blood Group Entry
blood_group_label = ttk.Label(window, text="Blood Group:")
blood_group_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
blood_group_entry = ttk.Entry(window)
blood_group_entry.grid(row=4, column=1, padx=10, pady=10)

# Generate QR Button
generate_button = ttk.Button(window, text="Generate QR", command=generate_qr)
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

# Status Label
status_label = ttk.Label(window, text="")
status_label.grid(row=6, column=0, columnspan=2)

# Run the application
window.mainloop()
