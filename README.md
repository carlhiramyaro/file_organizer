# file_organizer

# Automate Downloads

This Python script automates the organization of files in your Downloads directory. It sorts files into predefined categories and moves them to their respective directories.

## Features

- Moves files from the Downloads directory to specific folders based on file type:
  - Documents (e.g., .pdf, .docx, .txt, .xlsx, .pptx)
  - Music (e.g., .mp3, .wav, .aac)
  - Videos (e.g., .mp4, .avi, .mov, .mkv)
  - Pictures (e.g., .jpg, .jpeg, .png, .gif, .bmp)
  - Others (files that do not fit into the above categories)

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the script using Python:

   ```sh
   python automate_downloads.py
   ```

## File Structure

The script will create the following directories in your home directory if they do not already exist:

- `Documents`
- `Music`
- `Videos`
- `Pictures`
- `Others`

## How It Works

- The script scans the `~/Downloads` directory for files.
- It checks the file extension and matches it with predefined categories.
- It moves the files to the appropriate directories based on their file type.
- If a file does not match any predefined categories, it moves the file to the `Others` directory.

## Requirements

- Python 3.x
- The `os` and `shutil` modules (included in the Python Standard Library)

## Customization

You can customize the script by modifying the `file_types` dictionary to include more file extensions or categories as needed.

```python
file_types = {
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'music': ['.mp3', '.wav', '.aac'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
}
```
