import logging
import google.generativeai as genai


def main():
    # Get the API key from environment variable
    api_key = "AIzaSyDcv5ZHqOhMG1dkn1Gi7spNIiEHGVCEv08"
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Write a story about a magic backpack.")
    try:
        print(response.text)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

if __name__ == "__main__":
    main()
