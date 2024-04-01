# YouTube Video Downloader

This is a Python script for downloading YouTube videos using the Pytube library. It allows you to store URLs in a list, select a download folder, go through the list and download each video, and select the most suitable source for downloading.

## Features

- Store URLs in a list
- Select download folder
- Download videos from YouTube
- Automatically select the most suitable source for downloading
- Exception handling for file operations and network requests
- Uses the threading library for multithreading

## Requirements

- Python 3.x
- Pytube library
- Threading library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/abhiram10199/TubeGrabber.git
    ```

2. Navigate to the project directory:

    ```bash
    cd TubeGrabber
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have a list of YouTube video URLs stored in a text file (e.g., `urls.txt`).
2. Run the script `main.py`:

    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to select the download folder and start the download process.

## File Structure

- `main.py`: Main script for downloading YouTube videos.
- `test.py`: Pytest script for testing main functions.
- `urls.txt`: List of URLs to be downloaded.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## Acknowledgments

Special thanks to the developers of Pytube for creating such a useful library for working with YouTube videos.
