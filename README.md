# Concordance

This Python script, `concord.py`, serves as a concordance generator, a tool commonly used in literature to create an alphabetical list of words along with their frequencies and contextual usage within a given text or set of texts. The generated concordance can be insightful for researchers and readers, providing a deeper understanding of an author's language, style, and recurring themes.

# Functions

### `concord(input, output)`

- **Parameters:**
  - `input`: Path to the input text file.
  - `output`: (Optional) Path to the output file for the concordance.

- **Description:**
  - Initializes the Concordance Generator.

### `__toOut()`

- **Description:**
  - Called when an output file is provided. Writes the generated concordance to the specified output file.

### `__Exclusion(file)`

- **Parameters:**
  - `file`: Content of the input file.

- **Description:**
  - Removes exclusion words from the file content and returns them as a string.

### `__TupleCreater(capi_word, sente)`

- **Parameters:**
  - `capi_word`: Keyword to create tuples for.
  - `sente`: List of sentences from the input file.

- **Description:**
  - Creates tuples of (keyword, start_index_of_keyword, sentence) and returns a list of tuples.

### `__getSentences(file)`

- **Parameters:**
  - `file`: Content of the input file.

- **Description:**
  - Extracts sentences from the file content and returns them as a list.

### `__getKeys(s, excl)`

- **Parameters:**
  - `s`: String to extract keys from.
  - `excl`: Exclusion words.

- **Description:**
  - Extracts keys from the string, excluding specified words.

### `__appendright(word, i, sentence)`

- **Parameters:**
  - `word`: Keyword.
  - `i`: Index of the keyword in the sentence.
  - `sentence`: Sentence containing the keyword.

- **Description:**
  - Returns the sentence that fits within the range of 30 characters.

### `__appendleft(word, i, sentence)`

- **Parameters:**
  - `word`: Keyword.
  - `i`: Index of the keyword in the sentence.
  - `sentence`: Sentence containing the keyword.

- **Description:**
  - Returns the sentence that fits within the range of 20 characters.

### `__concordance_output(word, index, sent)`

- **Parameters:**
  - `word`: Keyword.
  - `index`: Index of the keyword in the sentence.
  - `sent`: Sentence containing the keyword.

- **Description:**
  - Generates the concordance output for a given keyword, index, and sentence.

### `full_concordance()`

- **Description:**
  - Calls all the helper functions to generate the full concordance.

---

## Clone the repository:

```bash
git clone https://github.com/your-username/concordance-generator.git
cd concordance-generator


