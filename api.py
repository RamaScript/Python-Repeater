import google.generativeai as genai
import time


def gemini(q):
    genai.configure(api_key="AIzaSyCm79FWDaAaftqAftv3GoXG6kP1cxX1Yho")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(q)
    print(response.text)
    time.sleep(2000)

qu = input("Ask anything : ")  
gemini(qu) 