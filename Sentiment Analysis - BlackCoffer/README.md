## Instructions for Use

### 1. Approach to the Solution:

The script performs sentiment analysis and readability analysis on text data extracted from URLs. Here's the approach:

- **Data Extraction:** The script extracts text data from URLs using web scraping techniques (BeautifulSoup (bs4) library).
- **Text Preprocessing:** The extracted text is pre-processed by tokenizing, removing stopwords, and cleaning the text.
- **Sentiment Analysis:** It calculates sentiment scores (positive, negative, polarity, subjectivity) based on provided positive and negative word lists.
- **Readability Analysis:** It computes various readability metrics such as average sentence length, percentage of complex words, FOG index, etc.
- **Output Generation:** Results are stored in a DataFrame and then saved to an Excel file.

### 2. How to Run the .py File to Generate Output:

To run the provided Python script and generate the output, follow these steps:

1. **Install Dependencies:** Make sure you have all the required dependencies installed. You can install them using pip:

    ```
    pip install bs4
    pip install requests
    pip install pandas
    pip install openpyxl
    pip install pyarrow
    pip install nltk
    pip install syllapy
    pip install tqdm
    ```

    If after installing the above dependencies, any error related to imports occurs, update the following using the pip command:

    ```
    pip install --upgrade --force-reinstall -q syllapy
    pip install --upgrade --force-reinstall -q setuptools
    ```

2. **Prepare Input Files:**
   - Prepare a text file containing positive words. `[positive_words.txt]`
   - Prepare a text file containing negative words. `[negative_words.txt]`
   - Prepare an Excel file (.xlsx) containing two columns: "URL_ID" and "URL", which specify the unique ID and the corresponding URL to scrape, respectively. `[input_data.xlsx]`

   *NOTE: `[ ]` represents any valid file path.*

3. **Run the Script:** Execute the Python script using the command line, passing the paths to the positive words file, negative words file, and input Excel file as arguments:

   ```
   python main.py [positive_words.txt] [negative_words.txt] [input_data.xlsx]
   ```

   Replace `positive_words.txt` and `negative_words.txt` with the paths to your positive and negative words files, and `input_data.xlsx` with the path to your input Excel file.

4. **Output:** After successful execution, the script will generate an Excel file named "Output Data Structure.xlsx" containing the analysis results.

### 3. Dependencies Required:

Ensure you have the following dependencies installed:

- `beautifulsoup4`
- `pandas`
- `nltk`
- `syllapy`
- `tqdm`

You can install these dependencies using pip as mentioned in step 1 above.

Following these instructions should allow you to run the provided Python script and generate the desired output successfully.
