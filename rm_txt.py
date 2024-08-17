import os

def remove_txt_suffix(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            new_filename = filename[:-4]  # Remove the last 4 characters (".txt")
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

directory = 'xxx'
remove_txt_suffix(directory)
