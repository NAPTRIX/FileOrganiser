import os
import shutil
import datetime

source_directory = '/path/to/source_directory'  # Replace with your source directory
destination_directory = '/path/to/destination_directory'  # Replace with your destination directory

file_categories = {
    'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.ico'),
    'Documents': ('.doc', '.docx', '.pdf', '.txt', '.rtf', '.xlsx', '.pptx', '.odt'),
    'Videos': ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'),
    'Music': ('.mp3', '.wav', '.flac', '.aac', '.ogg'),
}

# Create folders for each category in the destination directory
for folder_name in file_categories.keys():
    folder_path = os.path.join(destination_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# get the category of a file based on its extension
def get_file_category(file_extension):
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:
            return category
    return 'Other'

# organize files by moving them to the appropriate folders
def organize_files():
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        
        if os.path.isdir(file_path) or filename == os.path.basename(__file__):
            continue

        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        file_stats = os.stat(file_path)
        creation_date = datetime.datetime.fromtimestamp(file_stats.st_ctime)

        # Create a subfolder based on the creation date (YYYY-MM)
        subfolder_name = creation_date.strftime('%Y-%m')
        subfolder_path = os.path.join(destination_directory, subfolder_name)

        # Create the subfolder if it doesn't exist
        os.makedirs(subfolder_path, exist_ok=True)

        # Determine the category of the file
        file_category = get_file_category(file_extension)

        # Move the file to the appropriate category folder
        destination_path = os.path.join(subfolder_path, file_category)
        shutil.move(file_path, os.path.join(destination_path, filename))

if __name__ == '__main__':
    organize_files()
    print("Files organized successfully.")
