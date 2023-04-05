import openai

openai.api_key_path = "api_key.txt"

model = "gpt-3.5-turbo"
temperature = 0.1

print(
    """원하는 기능 선택
[0]: Python을 위한 Prompt 생성"""
)

option = int(input())
if option == 0:
    from prompts_generator.messages import messages
else:
    raise ValueError("범위 밖!")

query = input()
messages.append({"role": "user", "content": query})

response = openai.ChatCompletion.create(
    model=model, temperature=temperature, messages=messages
)

print(response["choices"][0]["message"]["content"])
