#!/usr/bin/env python3
import argparse
import re

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())

def shorten(text: str, max_length: int = 180) -> str:
    if len(text) <= max_length:
        return text
    snippet = text[: max_length - 1]
    last_space = snippet.rfind(" ")
    if last_space > 40:
        snippet = snippet[:last_space]
    return snippet.rstrip(" ,.-") + "…"

def build_linkedin_post(text: str) -> str:
    cleaned = clean_text(text)
    if not cleaned:
        raise ValueError("Inputteksten er tom.")
    return (
        "🚀 Kort indsigt:\n"
        f"{shorten(cleaned)}\n\n"
        "Hvad er din erfaring med dette?\n"
        "#LinkedIn #Læring #Udvikling"
    )

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="*")
    args = parser.parse_args()
    input_text = " ".join(args.text) if args.text else input("Indsæt din tekst: ")
    print(build_linkedin_post(input_text))

if __name__ == "__main__":
    main()