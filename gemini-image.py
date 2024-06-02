import os
import PIL.Image
import google.generativeai as genai

def main():
    # Get the API key from environment variable
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    
    img = PIL.Image.open('food.jpg')

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)
    response.resolve()

    try:
        print(response.text)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

if __name__ == "__main__":
    main()
