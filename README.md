# NLPApp

A desktop GUI application for Natural Language Processing tasks including Sentiment Analysis, Named Entity Recognition (NER), and Intent Analysis.

## Features

After registering and logging in, users can:

- **Sentiment Analysis** – Analyze the emotional tone of any text
- **Named Entity Recognition (NER)** – Identify and search for named entities (people, places, organizations, etc.) within a piece of text
- **Intent Analysis** – Classify the intent behind a piece of text

## Tech Stack

- **GUI:** Python Tkinter
- **NLP Backend:** [NLP Cloud](https://nlpcloud.com/) API via the `nlpcloud` Python client
- **Local Storage:** JSON-based user database

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/janyaverma/nlp_app.git
   cd nlp_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your NLP Cloud API key** (see section below on how to get one)

   Open `myapi.py` and replace the placeholder with your own key:
   ```python
   self.client = nlpcloud.Client("gpt-oss-120b", "YOUR_API_KEY_HERE", gpu=True)
   ```

## Usage

Run the app with:
```bash
python app.py
```

Register a new account, then log in to access the three NLP tools.

## How to Get Your NLP Cloud API Key

1. Go to [nlpcloud.com](https://nlpcloud.com/) and click **Sign Up**
2. Create a free account using your email
3. Once logged in, go to your **Dashboard** → **API Token** section
4. Copy your API token
5. Paste it into `myapi.py` in place of `YOUR_API_KEY_HERE`

> **Note:** The free tier has a limited number of API calls per month. Check [NLP Cloud's pricing page](https://nlpcloud.com/pricing) for details.

## Project Structure

```
nlp_app/
├── app.py          # Main application and GUI logic
├── myapi.py        # NLP Cloud API wrapper (add your key here)
├── mydb.py         # JSON-based user database handler
├── db.json         # Local user database (pre-loaded with dummy data)
├── resources/
│   └── favicon.ico
└── requirements.txt
```
