import gradio as gr
import time

#Store the product with its photos
product_pics = {
    "primer": "images/primer.jpeg",
    "concealer": "images/concealer.jpeg",
    "foundation": "images/foundation.jpeg",
    "blush": "images/blush.jpeg",
    "setting-powder": "images/powder.jpeg",
    "setting-spray": "images/settingspray.jpeg",
    "brow gel": "images/browgel.jpeg",
    "face wash": "images/cleanser.jpeg",
    "glitter": "images/eyeglitter.jpeg",
    "eye-lash curler": "images/eyelashcurler.jpeg",
    "eyeliner": "images/eyeliner.jpeg",
    "eyeshadow": "images/eyeshadow.jpeg",
    "mascara": "images/mascara.jpeg",
    "moisturizer": "images/moisturizer.jpeg",
    "loose-powder": "images/loosepowder.jpeg",
    "serum": "images/serum.jpeg",
    "setting-spray": "images/spray.jpeg"
}

#Store the order of the products
products = {
    "brow gel": 15,
    "glitter": 12,
    "foundation": 6,
    "concealer": 5,
    "setting-spray": 16,
    "eyeliner": 11,
    "serum": 2,
    "primer": 4,
    "eyeshadow": 10,
    "loose-powder": 9,
    "face wash": 1,
    "mascara": 14,
    "setting-powder": 8,
    "moisturizer": 3,
    "eye-lash curler": 13,
    "blush": 7
}


def bubble_sort_steps(chosen_products):
    """
    This function performs bubble sort on the chosen products and returns every step in the process.
    Parameters:
    ----------------------------------------------------------------------------------------------------
    chosen_products : list of str
                      The products chosen by the user in the order they chose them

    Returns
    -----------------------------------------------------------------------------------------------------
    list of str
        a list where each element is a list of product names
    
    """
    #Create a copy so we do not modify the original list
    names2 = chosen_products.copy()
    #Stores each version of the list during sorting
    steps = [names2.copy()]
    #Stores the number of items in the list
    n = len(names2)
    #Keeps track if any swap occurs during a pass
    swapped = True
    #Loop through the list until no swaps occur
    while swapped:
        swapped = False #Reset for each pass
        #Initalize the index that we will use to compare values in the list to
        i = 0
        #Compare items until the end of the list
        while i < n - 1:
            #Compare the adjacent elements to see of the one before it is bigger
            if products[names2[i]] > products[names2[i + 1]]:
                #If they are out of order swap them
                names2[i], names2[i + 1] = names2[i + 1], names2[i]
                swapped = True
                #Add the new list after the swap to steps
                steps.append(names2.copy())
            #Increment the index
            i += 1
        #After each pass, reduce the length of the list
        n -= 1
    #Return the steps
    return steps


def steps_to_photos(steps):
    """
    This function converts the sorting steps from the products name into file paths to display them
    Parameters:
    ----------------------------------------------------------------------------------------------------
    steps : a list where each element is a list of product names

    Returns
    -----------------------------------------------------------------------------------------------------
    list of str
        a list where each steps contains the image paths for the products
    """
    #Initialize a list to store the steps converted to image paths    
    image_steps = []  
    #Iterate through the steps to sort the list
    for step in steps:
        #Initalize a list to store the image path for the current step
        row = []
        #Loop through the product name for each step
        for name in step:
            #store the image path for the product after searching it
            image_path = product_pics[name]
            #Add the path to the current row
            row.append(image_path)
        #Add all the image steps to the full list of image steps
        image_steps.append(row)
    #Return the list of all converted steps
    return image_steps



def animate_sort(selected_products):
    """
    This function displays the frames for the sorting algorithm
    Parameters:
    ----------------------------------------------------------------------------------------------------
    selected_products : list of str
                        the makeup products chosen by the user

    Returns
    -----------------------------------------------------------------------------------------------------
    list of str
        a list of the image paths that represent a bubble sort swap
    """        
    #Base case: if less than two products are chosen it can not run
    if len(selected_products) < 2:
        yield ["Select at least two products!"]
        return
    #Bubble sort through the steps
    steps = bubble_sort_steps(selected_products)
    #Convert each step to its image file paths
    frames = steps_to_photos(steps)

    #Iterate through each frame 
    for frame in frames:
        time.sleep(0.6) #iterate at this speed to create an animation
        yield frame #output each frame to Gradio

def sorted_sound(selected_products):
    """
    This function returns the path to a sound file which plays once sorting is finished
    Parameters:
    ----------------------------------------------------------------------------------------------------
    selected_products : list of str
                        the makeup products chosen by the user

    Returns
    -----------------------------------------------------------------------------------------------------
    str
        The path to the sound file
    """   
    #Return the sound once the list is sorted
    return "sounds/sorted_sound.mp3"

#The Gradio Theme
theme = gr.themes.Monochrome(
    primary_hue="pink",
    secondary_hue="violet",
    neutral_hue="pink",
)


#The layout for the interface
with gr.Blocks() as demo:

    #Displays the title at the top
    gr.Markdown("<h2 style='text-align:center; color:pink;'>Makeup Product Sorting Animation</h2>")

    #Creates a checkbox for the user to selects which products they want to sort
    product_selector = gr.CheckboxGroup(
        choices=list(products.keys()),
        label="Select makeup products to sort"
    )
    #A button to start the bubble sort animation
    sort_button = gr.Button("Start Sorting")
    #A gallery to display the photos
    gallery = gr.Gallery(
        columns=6,
        height=400,
        label="Sorting Animation"
    )
    #Ouput to play a sound once the sorting is complete
    audio_output = gr.Audio(label="Sorted Sound")

    #When the button is pressed, run the animate_sort function and then the sorted_sound function to play the sound
    sort_button.click(
        fn=animate_sort,
        inputs=product_selector,
        outputs=gallery
    ).then(
        fn=sorted_sound,
        inputs=product_selector,
        outputs=audio_output
    )

#Launch the Gradio interface with the theme I created
demo.launch(theme= theme)

