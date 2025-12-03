# Bubble Sorting Algorithm - Makeup Sorting Edition

## Demo video


https://github.com/user-attachments/assets/e6062c7a-c733-4532-94a9-4b644339534a



## Problem Breakdown & Computational Thinking
  ## Decomposition: What smaller steps form your chosen algorithm?
        •Recieve the input of makeup products stored as a dictionary with its step number in the routine.
        •Take two two adjacent products in the list and compare them.
        •If the product's step number is greater than the one next to it, swap them.
        •Look at the next paits and repeat until the end of the list.
        •Repeat until no swaps occur.
      
  
  ## Pattern Recognition: How does it repeatedly reach, compare, or swap values?
        •Bubble sort repeatdely compares adjacent elements and swaps them if they are in the wrong order.
        •Each pass sends the highest value to the correct position at the end.
        •The sorting algorithm stops when there are no more swaps.
  
  ## Abstraction: Which details of the process should be shown to the user and how to show it,and which details should be discarded (i.e., not shown)?
        •Shown:
              •A check-box to choose the makeup products to sort
              •The makeup products being sorted
              •A sound that concurs that it has been sorted
        •Not-shown:
              •The back end parts such as converting the sorting steps/photos from the product names
              into file paths to display them
              
              
  
  ## Algorithm Design: How will input → processing → output flow to and from the user? Including the use of the graphical user interface (GUI).
  
      Input: 
        •User chooses a list of products as a tuple from a check-box list
      Processing: 
        •Implement the bubble sort on the list referencing the dictionary as a key
        •Compare the two adjacent elements
          • If a swap is needed, swap them.
        •Animate the swap necessary
        •Repeat until no swaps are needed
      Output:
        •Display an animation of the sorting process. 
        •A sounds will appear once the makeup products are sorted.
      
  
  <img width="728" height="1091" alt="flowchart bubble drawio" src="https://github.com/user-attachments/assets/04431a6f-fb83-46a4-aacc-e00923132cd9" />


## Testing and Verification
## Test One: Correct Input
            Input: [primer, concealer]
            Correct Output: [primer, cocnealer]
    
https://github.com/user-attachments/assets/f9cbcf09-8c1d-4f22-bc2e-ae4dfb0d8ce3

  ## Test Two: Reverse List
              Input:  ["setting-spray", "brow gel", "mascara", "eye-lash curler", "glitter",
              "eyeliner", "eyeshadow", "loose-powder","setting-powder", "blush", "foundation",
              "concealer", "primer", "moisturizer", "serum", "face wash"]
              Output: ["face wash", "serum", "moisturizer", "primer", "concealer", "foundation", "blush", 
              "setting-powder", "loose-powder", "eyeshadow", "eyeliner", "glitter", "eye-lash curler",
              "mascara", "brow gel", "setting-spray"]
              
https://github.com/naveiniv/CISC-121-Final-Project/issues/3#issue-3691399511


  




## Steps to Run
    1. Clone the repository and navigate into it:
    https://github.com/naveiniv/CISC-121-Final-Project.git
    cd CISC-121-Final-Projec
    2. Install dependencies:
    pip install -r requirements.txt
    3. Run the app
    python app.py
    4. Select at least two products and press the "Start Sorting" button
             


## Hugging Face Link
    https://huggingface.co/spaces/naveini/makeup-classifcation


## Author & Acknowledgment
Author: Naveini Vasikaran
Ackowledgment: This acknowledgment are towards resources provided to me from CISC121.
