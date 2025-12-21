from google import genai
from google.genai import types
from decouple import config

TOKEN=config("GEMINI")

def get_solution(sub) -> str:
    try:
        with open("ex.png","rb") as r_ex:
            result = r_ex.read()
            mt = "image/png"
    except:
        try:
            with open("ex.jpg","rb") as r_ex:
                result = r_ex.read()
                mt = "image/jpeg"
        except:
            with open("ex.jpeg","rb") as r_ex:
                result = r_ex.read()
                mt = "image/jpeg"
    if sub == "Геометрія":
        user_request = "Виріши мені задачу з геометрії. Намалюй мені схематично фігуру текстовими символами.Оформи рішення стисло,покроково з такими пунктами: Дано,знайти,рішення. "
    elif sub == "Алгебра":
        user_request = "Виріши мені задачу з алгебри. Якщо задача потребує намалюй мені схематично текстовими символами. Оформи рішення максимально стисло та покроково. "
    elif sub == "Хімія":
        user_request = "Виріши мені задачу з хімії. Оформи рішення максимально стисло ."
    elif sub == "Фізика":
        user_request = "Виріши мені задачу з фізики. Оформи рішення максимально стисло за правилами оформлення з фізики, якщо це потрібно.Якщо потрібні формули зкроби щоб вони нормально відображалися в текстовому форматі(коли дивлюся в браузері вони нормальні  коли копіюю текстовий файл вони вигляда як набір слешів.)"
    client = genai.Client(api_key=TOKEN)
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents = [
            user_request,
            types.Part.from_bytes(
                data=result,
                mime_type=mt
            )
        ]
    )
    return response.text