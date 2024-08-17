import os

def split_file(file_path, output_dir, chunk_size=24*1024*1024):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(file_path, 'rb') as f:
        chunk_number = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            with open(os.path.join(output_dir, f"{os.path.basename(file_path)}.part{chunk_number}"), 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_number += 1

split_file('file_path', 'output_dir')
