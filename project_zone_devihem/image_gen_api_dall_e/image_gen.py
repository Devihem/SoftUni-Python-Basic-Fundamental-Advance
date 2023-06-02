# Library from OpenAI
import os.path

import openai
# Built-in for visualisation
import tkinter
# Built-in taking ulr to data
import urllib.request
# Storing data in temporary storage ( ram ? )
from io import BytesIO
# Library for image visualisation from stored data. Pillow
from PIL import Image, ImageTk

# OpenAI - API-KEY DELL-E
openai.api_key = ""

# Saving Files - Folder
MEDIA_FOLDER = 'images/'


# Main - Function - Activated by button "Generate"
def render_image():

    global save_button

    try:
        save_button.destroy()
        image_url = get_image_url()
        image_name = '_'.join(input_field.get().split()) + '.jpg'
        # Making input_field to clear the text after entry
        input_field.delete(0, tkinter.END)
        image = convert_to_image_object(image_url)
        display_image(image)
        save_button = tkinter.Button(window, text='Save', height=2, width=10,
                                     command=lambda: save_image(image, os.path.join(MEDIA_FOLDER, image_name)))
        save_button.place(x=170, y=630)

    except openai.error.InvalidRequestError as error:
        error_label = tkinter.Label(window, text=f'{error}', fg='red')
        error_label.place(x=100, y=670)


def convert_to_image_object(image_url):
    with urllib.request.urlopen(image_url) as image_link:
        image_data = image_link.read()

    image_stream = BytesIO(image_data)
    image = Image.open(image_stream)

    return image


# Handling the data to image visualisation , first to image , then to imageTK
def display_image(image):
    tk_photo_image = ImageTk.PhotoImage(image)

    # Loading the real image in image_label , then taking the data out of the function with .image
    image_label.configure(image=tk_photo_image)
    image_label.image = tk_photo_image


def save_image(image, path):
    image.save(path)


# Function for API , script from OpenAI , prompt = "Text" or Windows panel box for text entry
def get_image_url():

    # This part is from OpenAI - API - WORK ONLY WITH CORRECT API KEY AND HAVING BALANCE CREDITS +
    # response = openai.Image.create(
    #     prompt=input_field.get(),
    #     n=1,
    #     size="256x256"
    # )
    # image_url = response['data'][0]['url']


    # Set Custom Banana image for Demo mode
    image_url = 'https://images.unsplash.com/photo-1481349518771-20055b2a7b24?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1239&q=80'
    print(image_url)
    return image_url


# Main - Window Frame
window = tkinter.Tk()

# Process / Window  - name
window.title('Image Generator: DALL-E')

# Window size WxH
window.geometry("1680x1050")

# Creating input panel/box and selecting over witch windows/widget to go."place" - selecting place in the window
input_field = tkinter.Entry(window, width=50)
input_field.place(x=20, y=600)
print('After ENtry Print')
# Creating button - named Generate with specific size. 'place' - selecting place in the window
# Adding - Command ( for adding function to our button without - () ! )
button_send = tkinter.Button(window, text='Generate', height=2, width=10, command=render_image)
button_send.place(x=80, y=630)

# Creating button - for save files
save_button = tkinter.Button(window, text='Save', height=2, width=10)

# The place where to be visualised the generated image frame
image_label = tkinter.Label(window)
image_label.place(x=220, y=5)

window.mainloop()
