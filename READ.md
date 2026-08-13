# Rule-Based AI Chatbot 🤖

A deterministic rule-based AI chatbot built using Python control flow and dictionary-based intent matching. Developed as part of the **DecodeLabs Industrial Training Kit (Project 1)**.

## Features
- **Input Sanitization:** Automatically strips whitespace and normalizes text to lowercase.
- **Infinite Cycle:** Runs in a continuous loop until a termination command is given.
- **Atomic Operations:** Uses Python dictionary `.get()` method for O(1) lookup efficiency.
- **Fallback Guardrails:** Gracefully handles unknown commands.

## How to Run
```bash
python chatbot.py