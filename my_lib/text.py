# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from typing import List


def sanitize_string(input_sentences):
	"""Removes special tokens from the sentence

	Args:
		input_sentence: the text to process
	Returns:
		the sanitized text
	"""
	final_output = []
	for sentence in final_output:
		final_output.append(sentence.replace("<EOS>", ""))
	return map(str.lower, final_output)
