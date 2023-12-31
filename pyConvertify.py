import os

import subprocess

def convert_file(input_file, output_file, output_format):
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-c:a', 'copy', output_file], check=True)
        print(f"Conversion successful! Output file saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print("Conversion failed.")
        print(e)

def prompt_output_format():
    print("Select the output format:")
    print("1. MP4")
    print("2. AVI")
    print("3. MKV")
    print("4. WebM")
    choice = input("Enter your choice (1-4): ")

    formats = {
        '1': 'mp4',
        '2': 'avi',
        '3': 'mkv',
        '4': 'webm'
    }

    if choice in formats:
        return formats[choice]
    else:
        print("Invalid choice. Defaulting to MP4.")
        return 'mp4'

def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return False
    return True

def check_dir_exists(dir_path):
    if not os.path.isdir(dir_path):
        print(f"Error: The directory {dir_path} does not exist.")
        return False
    return True

def check_filename_valid(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    if any(char in filename for char in invalid_chars):
        print(f"Error: The filename {filename} contains invalid characters.")
        return False
    return True

def prompt_input_file():
    while True:
        input_file = input("Enter the input file name: ")
        if check_file_exists(input_file):
            return input_file

def prompt_output_file():
    while True:
        output_dir = input("Enter the output directory path: ")
        if not check_dir_exists(output_dir):
            continue
        output_file = input("Enter the output filename (without extension): ")
        if not check_filename_valid(output_file):
            continue
        output_format = prompt_output_format()
        output_file_path = f"{output_dir}/{output_file}.{output_format}"
        return output_file_path

def main():
    input_file = prompt_input_file()
    input_file_path = os.path.join(os.getcwd(), input_file)  # Assume file is in the current directory
    output_file = prompt_output_file()
    output_format = output_file.split('.')[-1]  # Extract the output format from the file name
    convert_file(input_file_path, output_file, output_format)

if __name__ == '__main__':
    main()
