#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VOWELS = "aeiouy"


def count_syllables(word: str) -> int:
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0
    count = 0
    prev_is_vowel = False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_is_vowel:
            count += 1
        prev_is_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in VOWELS:
        count += 1
    return max(1, count)


def tokenize(text: str) -> tuple[int, int, int]:
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len([s for s in sentences if s.strip()])
    words = re.findall(r"\b[\w']+\b", text)
    word_count = len(words)
    syllable_count = sum(count_syllables(word) for word in words)
    return sentence_count, word_count, syllable_count


def compute_scores(sentences: int, words: int, syllables: int) -> dict[str, float]:
    if sentences == 0 or words == 0:
        return {"reading_ease": 0.0, "grade_level": 0.0}
    asl = words / sentences
    asw = syllables / words
    reading_ease = 206.835 - (1.015 * asl) - (84.6 * asw)
    grade_level = (0.39 * asl) + (11.8 * asw) - 15.59
    return {"reading_ease": reading_ease, "grade_level": grade_level}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--stdin", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    texts = []
    if args.stdin:
        texts.append(sys.stdin.read())
    for raw in args.paths:
        path = Path(raw)
        if path.is_file():
            texts.append(path.read_text(encoding="utf-8", errors="ignore"))

    combined = "\n".join(texts)
    sentences, words, syllables = tokenize(combined)
    scores = compute_scores(sentences, words, syllables)
    result = {
        "sentences": sentences,
        "words": words,
        "syllables": syllables,
        "reading_ease": round(scores["reading_ease"], 2),
        "grade_level": round(scores["grade_level"], 2),
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=True))
    else:
        print(f"Reading Ease: {result['reading_ease']}")
        print(f"Grade Level: {result['grade_level']}")


if __name__ == "__main__":
    main()
