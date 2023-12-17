import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model

model = load_model('Age_Sex_detection.h5')

# Initializing GUI
top = tk.Tk()
top.geometry('800x600')  # Use lowercase 'x' for the size
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

label1 = Label(top, text='Age:', background='#CDCDCD', font=('arial', 15, 'bold'))
label2 = Label(top, text='Gender:', background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

# Defining Detect function which detect the age and gender from the image
def Detect(file_path):
    try:
        image = Image.open(file_path)
        image = image.resize((48, 48))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        # Make predictions
        predictions = model.predict(image)
        
        # Print debugging information
        print("Raw Predictions:", predictions)

        # Extract predicted age and sex
        age = int(np.round(predictions[0][0]))
        sex_prob = predictions[1][0]
        sex = 0 if sex_prob < 0.5 else 1  # Adjust the threshold as needed

        # Display results
        print("Predicted age is:", age)
        print("Predicted gender is:", "Male" if sex == 0 else "Female")

        # Update labels
        label1.configure(foreground="#011638", text=f'Age: {age}')
        label2.configure(foreground="#011638", text=f'Gender: {"Male" if sex == 0 else "Female"}')

    except Exception as e:
        print(f"Error during detection: {e}")


    except Exception as e:
        print(f"Error during detection: {e}")


# Defining Show detect button function
def show_detect_button(file_path):
    Detect_b = Button(top, text="Detect Image", command=lambda: Detect(file_path), padx=10, pady=5)
    Detect_b.configure(background='#364156', foreground='white', font=('arial', 20, 'bold'))
    Detect_b.place(relx=0.79, rely=0.46)
# Defining upload image function
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail((top.winfo_width() / 2.25, (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text='')
        label2.configure(text='')
        show_detect_button(file_path)
    except:
        pass

upload = Button(top, text="Upload an Image", command=upload_image, padx=10, pady=5)
upload.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
upload.pack(side='bottom', pady=50,)
sign_image.pack(side='bottom', expand =True, )

label1.pack(side="bottom", expand = True)
label2.pack(side="bottom", expand = True)
heading= Label(top, text="Age and Gender Detector", pady=20,font=('arial',20,'bold'))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()