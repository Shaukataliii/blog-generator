# Blog Generator Web App

This project is a **Blog Generator** web application built using **Streamlit** and **LangChain**. The app uses the **Ollama LLM** (Large Language Model) to generate professional, informative blogs based on the user's input.

## Features
- Generate blogs for different target audiences such as:
  - Common people
  - Data Scientists
  - Software Engineers
  - Teachers
  - Body Builders
- Customizable blog topics and word counts.
- Professional and informative tone with no invalid references or links.
- Simple and clean UI built with Streamlit.
- Fast response time with real-time blog generation.

## How it Works
1. Enter a **blog topic**.
2. Specify the **number of words**.
3. Choose the **target audience** from the options.
4. Click **Generate** to create a blog in seconds.
5. The app shows the blog along with the **time taken** for generation.

## Tech Stack
- **Streamlit** for building the user interface.
- **LangChain** for managing language model prompts.
- **Ollama LLM** (`gemma2:2b` model) for blog generation.
- **Python** for backend logic and integration.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/blog-generator.git
    cd blog-generator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download Ollama setup from [Ollama's Github](https://github.com/ollama/ollama), install it and then download a model (if not already installed). I used the gemma2:2b model for this application. The model size is 1.6GB.

If you've downloaded any other model, make sure to change the line no: 18 of the main.py file to:
llm = load_ollama_llm(YOUR_DOWNLOADED_MODEL_NAME_HERE)

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## Project Structure
- **app.py**: Main application logic and Streamlit UI.
- **src/module.py**: Contains the `generate_blog` function that handles the blog generation process.
- **requirements.txt**: List of dependencies to run the project.

## Future Enhancements
- Allow users to select different writing styles.
- Improve customization for blog tone and structure.
- Add more audience options.

## License
This project is licensed under the MIT License.