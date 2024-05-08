Instructions for Use

Step 1: Generate Input Strings
a. Execute the script `input_generator.py`. This will create 1000 pairs of strings for each characteristic equation.
b. The generated pairs will be saved into two separate text files: `input_strings1.txt` for characteristic equation 1 and `input_strings2.txt` for characteristic equation 2.

Step 2: Generate Output Ciphertext
a. Run the script `output_generator.py`. It will process the previously generated text files to extract the corresponding ciphertext.
b. The ciphertext will be saved into two separate text files: `output_strings1.txt` and `output_strings2.txt`, corresponding to `input_strings1.txt` and `input_strings2.txt`, respectively.

Step 3: Decrypt the Key
a. Open and execute all cells within the `DES_Breaking.ipynb` notebook to determine the final decryption key.
