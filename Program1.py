import re
from collections import Counter

def word_frequency_analyzer(text):
    """
    Analyzes the frequency of words in a given text.

    Args:
        text (str): Input text to analyze.

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    
    text = text.lower()

    
    text = re.sub(r'[^\w\s]', '', text)

    
    words = text.split()

    
    word_frequencies = Counter(words)

    return word_frequencies


if __name__ == "__main__":
    input_text = (
        "The mysterious manuscript appeared on the detective's desk. "
        "The detective examined the curious document with growing interest."
    )
    
    
    result = word_frequency_analyzer(input_text)

    
    for word, count in result.items():
        print(f"{word}: {count}")


def test_word_frequency_analyzer():
    """Test the word_frequency_analyzer function with various test cases."""
    
    
    assert word_frequency_analyzer("Hello hello world!") == {'hello': 2, 'world': 1}

    
    assert word_frequency_analyzer("Wow, such an amazing book! Wow!") == {'wow': 2, 'such': 1, 'an': 1, 'amazing': 1, 'book': 1}

    
    assert word_frequency_analyzer("   Python    is great    ") == {'python': 1, 'is': 1, 'great': 1}

    
    assert word_frequency_analyzer("") == {}

    
    long_text = "a " * 1000 + "b " * 500 + "c " * 250
    expected_result = {'a': 1000, 'b': 500, 'c': 250}
    assert word_frequency_analyzer(long_text.strip()) == expected_result

    print("All tests passed!")


test_word_frequency_analyzer()
