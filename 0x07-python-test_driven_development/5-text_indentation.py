#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Check if text is a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    """Split the text into sentences and print each one"""

    sentences = text.split(".")
    for i, sentence in enumerate(sentences):
        if "?" in sentence:
            sub_sentences = sentence.split("?")
            for j, sub_sentence in enumerate(sub_sentences):
                if sub_sentence:
                    if j == 0 and i > 0:
                        print("\n")
                    print(sub_sentence.strip())
                    print("\n")
        elif ":" in sentence:
            sub_sentences = sentence.split(":")
            for j, sub_sentence in enumerate(sub_sentences):
                if sub_sentence:
                    if j == 0 and i > 0:
                        print("\n")
                    print(sub_sentence.strip())
                    print("\n")
        else:
            if sentence:
                if i > 0:
                    print("\n")
                print(sentence.strip())
                print("\n")
