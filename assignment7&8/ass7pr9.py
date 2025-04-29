'''Create  a tokenizer  for your own language (mother tongue you speak). The tokenizer should 
tokenize  punctuations,  dates,  urls,  emails,  numbers  (in  all  different  forms  such  as  “33.15”, 
“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design 
this. [Hint: Use unicode blocks for your language, check wikipedia pages] '''

import re

def gujarati_tokenizer(text):
    # Unicode range for Gujarati: \u0A80-\u0AFF

    patterns = {
        "url": r'(https?://[^\s]+|www\.[^\s]+)',  # URLs
        "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',  # Emails
        "date": r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',  # Dates
        "fraction": r'\d+/\d+',  # 313/77
        "number": r'\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b',  # (e.g., 3,22,243.50)
        "handle": r'@[a-zA-Z0-9_]+',  # (e.g., @username)
        "punctuation": r'[!\"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~।]',  # Punctuation including '।' used in Indian scripts
        "word": r'[\u0A80-\u0AFF]+',  # Gujarati words
        "other": r'\S'  # Catch any non-space character
    }
    combined_pattern = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in patterns.items())

    # Compile the regex
    tokenizer_re = re.compile(combined_pattern)

    # Tokenize the input text
    tokens = []
    for match in tokenizer_re.finditer(text):
        for key in patterns.keys():
            if match.group(key):
                tokens.append((key, match.group(key)))
                break

    return tokens

if __name__ == "__main__":
    # Sample Gujarati sentence with mixed elements
    text = "મારું ઈમેલ abc123@gmail.com છે અને હું @gujarati_user ને 25-12-2024 ના રોજ મળ્યો. ₹12,34,567.89 નો ખર્ચ થયો! વધુ માહિતી માટે https://gujaratiexample.com મુલાકાત લો. ગુણોત્તર 144/12 છે।"
    tokens = gujarati_tokenizer(text)
    for token_type, token in tokens:
        print(f"{token_type}: {token}")
