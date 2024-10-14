# GPT-4 Chatbot

A simple command line chatbot with GPT-4.

## Setup

You need to create a virtual env and install the packages listed in `requirements.txt`. You can then run Jupyter Notebooks in VS Code.


You need to create a `.env` file with your `OPENAI_API_KEY`.

## Usage

To run the CLI:

```
cd ChatBot
python main.py
```

You can define the personality of your chatbot, it is friendly and helpful by default:

```
python chatbot.py --personality "kind"
```

You can quit by typing `ctrl + C` (Mac) or `cmd + C` (Windows).

## Features

- writing the basic chatbot structure.
- persisting messages accross requests.
- adding optional personalities.
- colorizing the chatbot output.

Based on [Mastering OpenAI Python APIs: Unleash the Power of GPT4](https://www.udemy.com/course/mastering-openai/) by Colt Steele (2023).
