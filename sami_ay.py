import requests

def sami_ai(text):
    dev = ["Sami", "المطور", "Dev", "dev", "المبرمج", "من برمجك", "سبايدر", "SaMi", "Mr.SaMi", "قناة", "قناة","sami"]

    if text is None or text == "":
        error_message = "You must enter text. You have not entered text"
        return {"response": error_message}
    else:
        if text not in dev:
            headers = {
                'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/16.3.1 hw/iPhone12_5',
                'Accept-Language': 'ar',
                'Content-Type': 'application/json;charset=UTF-8'
            }
            data = {'data': {'message': text}}
            response = requests.post('https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta', json=data, headers=headers)
            result = response.json()["result"]["choices"][0]["text"]
            sami = f"""
{result}

● Api By : @SaMi_ye
            """
            return {"response":sami}
        else:
            dev_ye = """
I was programmed by Sami from Yemen in advanced programming languages ​​to implement all your requests in programming, hacking, or education. You can join the developer channel via the following link: t.me/SaMi_ye
            """
            return {"response": dev_ye}
