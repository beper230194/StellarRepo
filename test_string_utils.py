import pytest
from string_utils import is_palindrome, count_words, truncate

class TestIsPalindrome:
    def test_simple_true(self):
        assert is_palindrome("madam") is True
    def test_simple_false(self):
        assert is_palindrome("hello") is False
    def test_case_insensitive(self):
        assert is_palindrome("Racecar") is True
    def test_spaces_ignored(self):
        assert is_palindrome("A man a plan a canal Panama") is True
    def test_empty_string(self):
        assert is_palindrome("") is True
    def test_non_string_raises(self):
        with pytest.raises(TypeError):
            is_palindrome(123)

class TestCountWords:
    def test_simple(self):
        assert count_words("hello world") == 2
    def test_extra_spaces(self):
        assert count_words(" hello world ") == 2
    def test_empty(self):
        assert count_words("") == 0

class TestTruncate:
    def test_short_unchanged(self):
        assert truncate("hello", 10) == "hello"
    def test_long_truncated(self):
        assert truncate("hello world", 5) == "hello..."
    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            truncate("hello", -1)