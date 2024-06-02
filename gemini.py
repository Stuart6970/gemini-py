import os
import google.generativeai as genai


def main():
    # Get the API key from environment variable
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Write a story about a magic backpack.")
    try:
        print(response.text)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

if __name__ == "__main__":
    main()
