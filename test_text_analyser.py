import pytest
from text_analyser import TextAnalyser

@pytest.fixture
def analyser():
	return TextAnalyser()

class TestWordCount:
	def test_simple(self, analyser):
		assert analyser.word_count("hello world") == 2

	def test_extra_whitespace(self, analyser):
		assert analyser.word_count(" hello world ") == 2

	def test_empty(self, analyser):
		assert analyser.word_count("") == 0

	def test_single_word(self, analyser):
		assert analyser.word_count("hello") == 1

class TestSentenceCount:
	def test_period(self, analyser):
		assert analyser.sentence_count("Hello world. Goodbye.") == 2

	def test_mixed_terminators(self, analyser):
		assert analyser.sentence_count("Really? Yes! Okay.") == 3

	def test_no_terminator(self, analyser):
		assert analyser.sentence_count("hello world") == 1

	def test_empty(self, analyser):
		assert analyser.sentence_count("") == 0

class TestAverageWordLength:
	def test_simple(self, analyser):
		assert analyser.average_word_length("cat dog") == pytest.approx(3.0)

	def test_empty_raises(self, analyser):
		with pytest.raises(ValueError):
			analyser.average_word_length("")

	def test_strips_punctuation(self, analyser):
		result = analyser.average_word_length("hello, world.")
		assert result == pytest.approx(5.0)

class TestMostFrequentWord:
	def test_basic(self, analyser):
		assert analyser.most_frequent_word("the cat sat on the mat") == "the"

	def test_case_insensitive(self, analyser):
		assert analyser.most_frequent_word("Cat cat CAT") == "cat"

	def test_empty_raises(self, analyser):
		with pytest.raises(ValueError):
			analyser.most_frequent_word("")