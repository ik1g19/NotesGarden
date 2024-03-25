import os

def replace_phrase_in_files(directory_path, old_phrase, new_phrase):
    # Get list of files in the directory
    files = os.listdir(directory_path)
    
    for file in files:
        # Check if the current file is a regular file
        if os.path.isfile(os.path.join(directory_path, file)):
            # Read content of the file
            with open(os.path.join(directory_path, file), 'r') as f:
                content = f.read()
            
            # Replace the old phrase with the new phrase
            new_content = content.replace(old_phrase, new_phrase)
            
            # Write the modified content back to the file
            with open(os.path.join(directory_path, file), 'w') as f:
                f.write(new_content)

# Specify the directory path
directory_path = '.'  # Current directory

# Specify the old and new phrases
old_phrase = 'Paper Note PNGs/Programming II PNGs/'
new_phrase = 'Paper Note PNGs/Programming II PNGs/'

# Call the function to replace the phrases in files
replace_phrase_in_files(directory_path, old_phrase, new_phrase)

print("Replacement completed successfully.")
