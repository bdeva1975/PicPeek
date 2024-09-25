# PicPeek

PicPeek is an intelligent image analysis companion that harnesses the power of GPT-4 vision to decode and understand images. This Streamlit-based web application offers a user-friendly interface for exploring AI-powered visual understanding.

## Features

- **Image Caption Generation**: Get concise captions for your images.
- **Detailed Description**: Receive thorough, detailed descriptions of image content.
- **Image Classification**: Categorize images into predefined categories.
- **Object Recognition**: Identify multiple objects within an image.
- **Subject Identification**: Determine the primary subject of an image.
- **Creative Writing**: Generate short stories based on image content.
- **Emotion Analysis**: Interpret emotions displayed by people in images.
- **Text Transcription**: Extract and transcribe text found in images.
- **Text Translation**: Translate text in images to different languages.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/picpeek.git
   cd picpeek
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run image_understanding_app.py
   ```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`).

3. Select an image from the provided examples or upload your own.

4. Choose a prompt type or enter a custom prompt.

5. Click "Go" to generate the analysis.

## Project Structure

- `image_understanding_app.py`: Main Streamlit application file.
- `image_understanding_lib.py`: Library containing helper functions for image processing and API interactions.
- `images/`: Directory containing example images.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- streamlit
- openai
- Pillow

## Contributing

Contributions to PicPeek are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the OpenAI GPT-4 vision model for image analysis.
- Streamlit for the web application framework.

## Disclaimer

This application is for educational and demonstration purposes only. Please ensure you comply with OpenAI's use-case policies when using this application.
