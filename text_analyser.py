"""Text analyser utilities for week3 lab."""
from typing import List
import string


class TextAnalyser:
    """Class providing simple text analysis utilities."""

    def word_count(self, text: str) -> int:
        """Return the number of words in text."""
        if text is None:
            return 0
        # split on whitespace; this naturally handles extra spaces
        words = [w for w in text.split() if w]
        return len(words)

    def sentence_count(self, text: str) -> int:
        """Return the number of sentences in text based on .!? terminators."""
        if text is None:
            return 0
        text = text.strip()
        if not text:
            return 0
        terminators = set('.!?')
        count = 0
        prev_was_term = False
        for ch in text:
            if ch in terminators:
                if not prev_was_term:
                    count += 1
                    prev_was_term = True
            else:
                prev_was_term = False
        # If no terminators found but non-empty text, it's one sentence
        if count == 0:
            return 1
        return count

    def average_word_length(self, text: str) -> float:
        """Return the average length of words in text, stripping surrounding punctuation."""
        if text is None:
            raise ValueError("empty input")
        words = []
        for w in text.split():
            cleaned = w.strip(string.punctuation)
            if cleaned:
                words.append(cleaned)
        if not words:
            raise ValueError("empty input")
        total = sum(len(w) for w in words)
        return total / len(words)

    def most_frequent_word(self, text: str) -> str:
        """Return the most frequent word in text (case-insensitive, punctuation stripped)."""
        if text is None:
            raise ValueError("empty input")
        cleaned_words: List[str] = []
        for w in text.split():
            cleaned = w.strip(string.punctuation).lower()
            if cleaned:
                cleaned_words.append(cleaned)
        if not cleaned_words:
            raise ValueError("empty input")
        counts = {}
        for w in cleaned_words:
            counts[w] = counts.get(w, 0) + 1
        max_count = max(counts.values())
        # return the first word in original order that has max_count
        for w in cleaned_words:
            if counts[w] == max_count:
                return w
        # fallback (shouldn't happen)
        raise ValueError("no words found")
