import openai
openai.api_key = ""

class Chat:
    def response(self, str):
        api_result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": str},
            ]
        )
        return api_result['choices'][0]['message']['content']

if __name__ == '__main__':
    chat = Chat()
    sys_response = chat.response(input("Input:"))