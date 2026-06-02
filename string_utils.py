from typing import Any


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, ignoring case and spaces."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    # Normalize by removing all whitespace and lowercasing
    normalized = "".join(ch.lower() for ch in s if not ch.isspace())
    return normalized == normalized[::-1]


def count_words(s: str) -> int:
    """Return the number of words in s (split on any whitespace)."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    stripped = s.strip()
    if stripped == "":
        return 0
    return len(stripped.split())


def truncate(s: str, n: int) -> str:
    """Return s unchanged if its length is <= n; otherwise return first n chars + '...'."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    if len(s) <= n:
        return s
    return s[:n] + "..."
