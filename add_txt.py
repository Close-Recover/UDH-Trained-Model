import os

def add_txt_suffix(directory):
    for filename in os.listdir(directory):
        if not filename.endswith('.txt'):
            new_filename = filename + '.txt'
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

directory = 'xxx'
add_txt_suffix(directory)
