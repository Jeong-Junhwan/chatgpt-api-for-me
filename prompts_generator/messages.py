messages = [
    {"role": "system", "content": open("prompts_generator/system_content.txt").read()},
    {
        "role": "user",
        "content": f"Here are the good examples for prompt. you can create a prompt by referring to the following examples. \n{open('prompts_generator/python_example.txt').read()}",
    },
    {"role": "assistant", "content": "I understood. Give me your topic."},
]
