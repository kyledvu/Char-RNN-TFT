import re
from tft_vocab import tft_vocab
import demoji

import demoji

def remove_emojis(text):
    return demoji.replace_with_desc(text, '')

def replace_incorrect_with_correct(text, corrections):

    text = text.lower()

    # Create a regex pattern to match anything within square brackets
    pattern = r'\[.*?\]'
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Replace all occurrences of the pattern with an empty string
    text_without_brackets = re.sub(regex, '', text)
    
    # Split the text into lines
    lines = text_without_brackets.splitlines()
    
    # Initialize an empty list to store corrected lines
    corrected_lines = []
    
    # Iterate through each line in the text
    for line in lines:
        # Split the line into words
        words = line.split()
        corrected_words = []
        # Iterate through each word in the line
        for word in words:
            # Check if the word is in the corrections dictionary
            if word in corrections:
                # If yes, replace the word with its corrected form
                corrected_words.append(corrections[word])
            else:
                # If no correction is needed, keep the original word
                corrected_words.append(word)
        
        # Join the corrected words back into a single line
        corrected_line = ' '.join(corrected_words)
        corrected_lines.append(corrected_line)
    
    # Join the corrected lines back into a single text with newlines
    corrected_text = '\n'.join(corrected_lines)
    
    return corrected_text

def process_text_file(input_file, output_file, corrections):
    try:
        # Open the input file for reading
        with open(input_file, 'r', encoding='utf-8') as f:
            # Read the entire content of the file
            text = f.read()
        
        # Process the text: remove brackets content and replace incorrect words
        corrected_text = remove_emojis(text)
        
        # Open the output file for writing
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write the corrected text to the output file
            f.write(corrected_text)
        
        print(f"Processed text written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

# Define the corrections dictionary
corrections = tft_vocab

# Input and output file paths
input_file = "data/tweets.txt"
output_file = "data/tweets.txt"

# Process the text file with corrections
process_text_file(input_file, output_file, corrections)
