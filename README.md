# pyConvertify
terminal based python video converter using ffmpeg


pyConvertify is a Python-based file conversion utility that leverages the power of FFmpeg to convert media files from one format to another. The script provides a simple command-line interface for users to specify the input file, output directory, output filename, and desired output format.
Modules

The script uses the following Python modules:

- os: Provides functions for interacting with the operating system.
- subprocess: Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

#Functions

The script contains the following functions:
`convert_file(input_file, output_file, output_format)`

This function takes in three parameters: input_file, output_file, and output_format. It uses the subprocess module to run the FFmpeg command for converting the input_file to the specified output_format. The converted file is saved as output_file. If the conversion is successful, a success message is printed; otherwise, an error message is printed.
`prompt_output_format()`

This function prompts the user to select the desired output format from a list of options (MP4, AVI, MKV, WebM). It returns the selected format. If the user enters an invalid choice, it defaults to MP4.
`check_file_exists(file_path)`

This function checks if the file at file_path exists. It returns True if the file exists, False otherwise.
`check_dir_exists(dir_path)`

This function checks if the directory at dir_path exists. It returns True if the directory exists, False otherwise.
`check_filename_valid(filename)`

This function checks if the filename is valid (i.e., it does not contain any invalid characters). It returns True if the filename is valid, False otherwise.
`prompt_input_file()`

This function prompts the user to enter the name of the input file to be converted. It keeps prompting until a valid file is entered. It returns the name of the input file.
`prompt_output_file()`

This function prompts the user to enter the output directory path and the output filename (without extension). It keeps prompting until valid inputs are entered. It then calls the `prompt_output_format()` function to get the desired output format. It constructs the output file path by joining the output directory, output filename, and output format, and returns this path.
`main()`

This function is the main driver function. It calls the `prompt_input_file()` function to get the input file, constructs the full path of the input file, calls the `prompt_output_file()` function to get the output file path, extracts the output format from the output file name, and finally calls the `convert_file()` function to convert the input file to the desired format.


#Usage
To use the script, simply run it from the command line. It will prompt you to enter the necessary information (input file, output directory, output filename, output format). The script assumes that the input file is in the current directory.
<pre>
    python pyConvertify.py
</pre>
#Dependencies

This script requires FFmpeg to be installed on your system. You can install FFmpeg using the package manager of your operating system. For example, on Ubuntu, you can install FFmpeg using the following command:

<pre>
    sudo apt-get install ffmpeg
</pre>

#Note

This script performs error checking on the input file, output directory, and output filename. It is assumed that the user will provide valid inputs. If the user provides an invalid input, the script will keep prompting until a valid input is entered.
