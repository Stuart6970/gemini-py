import PIL.Image
import google.generativeai as genai

def main():
    api_key = "AIzaSyDcv5ZHqOhMG1dkn1Gi7spNIiEHGVCEv08"
    genai.configure(api_key=api_key)
    
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
