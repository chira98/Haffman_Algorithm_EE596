# Haffman_Algorithm_EE596
Huffman coding uses a greedy algorithm to build a prefix tree that optimizes the encoding scheme so that the most frequently used symbols have the shortest encoding

Following image is used for apply the haffman Algorthim,
![Parrots-680x680](https://github.com/chira98/Haffman_Algorithm_EE596/assets/55477322/edf185be-9434-4344-97ac-1b914b37e796)

Steps Followed,
Step 1: Read the original image into a Matrix.   

Step 2: Select 16×16 cropped sub-image from your input at step2. Note that the starting point of 
the cropping window will depend on your Registration number. (Instructor will provide these 
details at the lab.)    

Step 3: Quantize the output at Step 3 into 8 levels (level 0-7) using uniform quantization.    

Step 4: Find the probability of each symbol distribution of the output at Step 4.     

Step 5: Construct the Huffman coding algorithm for cropped image at Step 4.( Do not use inbuilt 
algorithms.)      

Step 6: Compress both cropped and original images using the algorithm and the codebook
generated at step 6. You may round any intensity values outside the codebook, to the nearest 
intensity value in the codebook, where necessary.      

Step 7: Save the compressed image into a text file.      

Step 8: Compress the original image using Huffman encoding function in the Matlab tool box and 
save it into another text file.      

Step 9: Decompress the outputs at Step 8 and 9, by reading in the text files.      

Step 10: Calculate the entropy of the Source      

Step 11: Evaluate the PSNR of,     
         i. The original images         
         ii. The decompressed images        
      


