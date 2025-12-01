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




## Steps to Run


## Hugging Face Link
    https://huggingface.co/spaces/naveini/makeup-classifcation




## Author & Acknowledgment
