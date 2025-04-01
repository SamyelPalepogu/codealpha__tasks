import os
import shutil
from datetime import datetime

def organize_by_extension(directory):
    """Organizes files into subfolders based on their file extensions."""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = filename.split('.')[-1].lower()
            folder_name = file_extension.upper() + "_Files"
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(filepath, os.path.join(folder_path, filename))
            log_action(f"Moved {filename} to {folder_name}")

def organize_by_date(directory):
    """Organizes files into subfolders based on their creation or modification dates."""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            creation_time = os.path.getctime(filepath)
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            folder_path = os.path.join(directory, date_folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(filepath, os.path.join(folder_path, filename))
            log_action(f"Moved {filename} to {date_folder}")

def organize_by_size(directory):
    """Organizes files into subfolders based on their size."""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            if file_size < 1_000_000:  # Less than 1MB
                folder_name = "Small_Files"
            elif file_size < 10_000_000:  # Between 1MB and 10MB
                folder_name = "Medium_Files"
            else:  # Greater than 10MB
                folder_name = "Large_Files"
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(filepath, os.path.join(folder_path, filename))
            log_action(f"Moved {filename} to {folder_name}")

def log_action(action):
    """Logs actions to a log.txt file."""
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {action}\n")

def main():
    print("File Organizer")
    print("1. Organize by File Extension")
    print("2. Organize by Date")
    print("3. Organize by File Size")
    choice = input("Choose an option (1/2/3): ").strip()

    directory = input("Enter the directory to organize: ").strip()
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    if choice == "1":
        organize_by_extension(directory)
    elif choice == "2":
        organize_by_date(directory)
    elif choice == "3":
        organize_by_size(directory)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    print(f"Files in '{directory}' have been organized. Check 'log.txt' for details.")

if __name__ == "__main__":
    main()