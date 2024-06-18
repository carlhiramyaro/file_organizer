import os
import shutil

# Define your paths
downloads_path = os.path.expanduser('~/Downloads')
documents_path = os.path.expanduser('~/Documents')
music_path = os.path.expanduser('~/Music')
videos_path = os.path.expanduser('~/Videos')
pictures_path = os.path.expanduser('~/Pictures')
others_path = os.path.expanduser('~/Others')

# Define file type categories
file_types = {
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'music': ['.mp3', '.wav', '.aac'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
}

def move_files():
    # Create destination directories if they do not exist
    for path in [documents_path, music_path, videos_path, pictures_path, others_path]:
        if not os.path.exists(path):
            os.makedirs(path)
    
    # Iterate over all files in the Downloads directory
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file's destination based on its extension
        file_extension = os.path.splitext(filename)[1].lower()
        destination_path = None

        for category, extensions in file_types.items():
            if file_extension in extensions:
                if category == 'documents':
                    destination_path = documents_path
                elif category == 'music':
                    destination_path = music_path
                elif category == 'videos':
                    destination_path = videos_path
                elif category == 'pictures':
                    destination_path = pictures_path
                break

        # If no matching category, move to 'Others'
        if destination_path is None:
            destination_path = others_path

        # Move the file
        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename} to {destination_path}")
        except Exception as e:
            print(f"Error moving file {filename}: {e}")

if __name__ == "__main__":
    move_files()