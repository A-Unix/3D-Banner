#!/usr/bin/python3

import sys
import os
import subprocess
import time

print("Checking if Colorama has been installed already or not!")

time.sleep(2)

# Check if Colorama has been already installed or not
try:
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Colorama has been already installed, We have initialized it for you :)")
    time.sleep(2)
except ImportError:
    print(Fore.RED + "Colorama has not been installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore
    print(Fore.LIGHTMAGENTA_EX + "Done, Colorama has been installed.")
    time.sleep(2)

# Initialize colorama
init(autoreset=True)

# Clear the terminal screen
os.system("clear")
time.sleep(1)

# Create 3D banner for showcase
def create_3d_banner1():
    # Banner text
    banner_text = "   3D-BANNER"

    try:
        # Use figlet to create ASCII art with mono9 font
        figlet_process = subprocess.Popen(
            ["figlet", "-w", "100", "-f", "mono9", banner_text],
            stdout=subprocess.PIPE
        )
        figlet_output, _ = figlet_process.communicate()

        # Use lolcat to add color to the ASCII art
        lolcat_process = subprocess.Popen(["lolcat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        banner_output, _ = lolcat_process.communicate(input=figlet_output)

        # Print the result
        print(banner_output.decode("utf-8"))

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Error: Make sure 'figlet' and 'lolcat' are installed on your system.(Hint: Run ./setup.sh)")
        time.sleep(2)

if __name__ == "__main__":
    create_3d_banner1()

print(Fore.LIGHTMAGENTA_EX + "Hit 'CTRL+C' to exit anytime.")
# Create functions to create 3D banner
def create_3d_banner():
    # Take input from the user for the banner text
    banner_text = input(Fore.LIGHTYELLOW_EX + "Enter the text for the 3D banner (type 'exit' to end): ")

    # Check if the user wants to exit
    if banner_text.lower() == 'exit':
        print(Fore.CYAN + "Don't forget to follow me on GitHub :)")
        return True

    # Take input from the user for the file path to save the banner
    file_path = input(Fore.LIGHTCYAN_EX + "Enter the file path to save the banner (e.g., /path/to/banners/my_banner): ")

    # Add a default file extension (e.g., ".txt")
    file_path_with_extension = f"{file_path}.txt"

    try:
        # Use figlet to create ASCII art with mono9 font
        figlet_process = subprocess.Popen(
            ["figlet", "-w", "100", "-f", "mono9", banner_text],
            stdout=subprocess.PIPE
        )
        figlet_output, _ = figlet_process.communicate()

        # Use lolcat to add color to the ASCII art
        lolcat_process = subprocess.Popen(["lolcat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        banner_output, _ = lolcat_process.communicate(input=figlet_output)

        # Save the banner to the specified file
        with open(file_path_with_extension, "w") as file:
            file.write(banner_output.decode("utf-8"))

        print(Fore.LIGHTMAGENTA_EX + f"Banner saved successfully to: {file_path_with_extension}")

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Error: Make sure 'figlet' and 'lolcat' are installed on your system.")

    return False

if __name__ == "__main__":
    while not create_3d_banner():
        pass
