import os

def merge_files(input_dir, output_file):
    with open(output_file, 'wb') as output:
        part_number = 0
        while True:
            part_file = os.path.join(input_dir, f"trained_model.tar.gz.part{part_number}")
            if not os.path.exists(part_file):
                break
            with open(part_file, 'rb') as part:
                output.write(part.read())
            part_number += 1

input_dir = 'xxx'
output_file = 'xxx'
merge_files(input_dir, output_file)
