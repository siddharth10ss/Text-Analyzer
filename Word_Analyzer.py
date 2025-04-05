import string
from collections import Counter

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Sentence splitting (basic using period, question mark, exclamation)
    sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s]
    
    # Remove punctuation for word analysis
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.split()
    
    word_count = len(words)
    char_count = len(text)
    avg_word_len = sum(len(word) for word in words) / word_count if word_count else 0
    longest_word = max(words, key=len) if words else ''
    
    word_freq = Counter([word.lower() for word in words])
    most_common_word, most_common_count = word_freq.most_common(1)[0] if word_freq else ("", 0)

    print("\n📊 TEXT ANALYSIS RESULTS:")
    print(f"Total Words            : {word_count}")
    print(f"Total Characters       : {char_count}")
    print(f"Average Word Length    : {avg_word_len:.2f}")
    print(f"Number of Sentences    : {len(sentences)}")
    print(f"Most Frequent Word     : '{most_common_word}' (appears {most_common_count} times)")
    print(f"Longest Word           : '{longest_word}'")

# Example usage
file_path = "sample_text.txt"  # Replace with your actual file
analyze_text(file_path)
