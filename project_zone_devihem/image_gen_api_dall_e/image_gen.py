# Library from OpenAI
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
openai.api_key = "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"


# Main - Function - Activated by button "Generate"
def render_image():
    try:
        image_url = get_image_url()
        # Making input_field to clear the text after entry
        input_field.delete(0, tkinter.END)
    except openai.error.InvalidRequestError:
        error_label = tkinter.Label(window, text="Prompt cannot be empty", fg='red')
        error_label.place(x=100, y=670)
    else:
        display_image(image_url)


# Handling the data to image visualisation , first to image , then to imageTK
def display_image(img_url):
    with urllib.request.urlopen(img_url) as image_link:
        image_data = image_link.read()

    image_stream = BytesIO(image_data)
    pil_image = Image.open(image_stream)
    photo_image = ImageTk.PhotoImage(pil_image)

    # Loading the real image in image_label , then taking the data out of the function with .image
    image_label.configure(image=photo_image)
    image_label.image = photo_image


# Function for API , script from OpenAI , prompt = "Text" or Windows panel box for text entry
def get_image_url():
    response = openai.Image.create(
        prompt=input_field.get(),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
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

# Crating button - named Generate with specific size. 'place' - selecting place in the window
# Adding - Command ( for adding function to our button without - () ! )
button_send = tkinter.Button(window, text=" Generate", height=2, width=10, command=render_image)
button_send.place(x=120, y=630)

image_label = tkinter.Label(window)
image_label.place(x=220, y=5)

window.mainloop()
