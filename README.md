## main.py Documentation

### Description

The `main.py` file serves as the main entry point for the program. It reads input from a text file, performs sentiment analysis using a model deployed in another file, and displays the results.

### Usage

1. Ensure you have an API key and a text file named `input.txt` with the reviews you want to analyze.
2. Update the `input.txt` file with the desired reviews.
3. Run the `main.py` file to start the sentiment analysis process.

### Code Explanation

1. The necessary modules and functions are imported, including `Markdown` from `IPython.display`, `os`, `load_dotenv` from `dotenv`, and `sentiment_analyser` from `model`.
2. The `load_dotenv()` function is called to load environment variables, which likely includes the API key.
3. The `main()` function is defined, which is the entry point of the program.
4. Inside `main()`, the `input.txt` file is opened, and its contents are read into the `reviews` variable.
5. The `sentiment_analyser()` function from `model.py` is called with `reviews` as an argument, and the response is stored in the `response` variable.
6. The string "starting the process" is printed to the console.
7. The `Markdown()` function is used to display the `response` in Markdown format.
8. The `if __name__ == "__main__":` block ensures that the `main()` function is only executed when the script is run directly (not imported as a module).

## model.py Documentation

### Description

The `model.py` file contains the `sentiment_analyser` function used for sentiment analysis. It utilizes a language model to analyze the sentiment of input text based on predefined prompts.

### Usage

1. Ensure you have the necessary dependencies installed and configured.
2. Update the `prompt` variable in the file with the desired sentiment analysis task description.
3. Call the `sentiment_analyser` function with the input text to perform sentiment analysis.

### Code Explanation

1. The required modules are imported, including `completion` from `litellm` and `os`.
2. The `prompt` variable is defined, which contains the instructions and examples for the sentiment analysis task.
3. The `sentiment_analyser` function is defined, taking `input_file` as an argument.
4. Inside the function, the `completion` function from `litellm` is called with the following parameters:
   - `model`: The language model to be used for sentiment analysis (in this case, 'gpt-4o').
   - `messages`: A list of dictionaries representing the conversation between the user and the system. The system message contains the `prompt`, and the user message contains the `input_file`.
   - `api_key`: The API key for the language model, retrieved from the environment variables using `os.getenv`.
   - `max_tokens`: The maximum number of tokens to generate in the response (set to 10 in this example).
5. The response from the `completion` function is returned by the `sentiment_analyser` function.

### Additional Notes

- Ensure you have the necessary API key and text file for input to run the sentiment analysis successfully.
- Follow the provided examples and guidelines for accurate sentiment analysis results.
- Make sure to handle any errors or exceptions that may occur during the execution of the program.
