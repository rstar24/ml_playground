response = ollama.chat(model = 'llama32',messages=[
    {
        'role': 'user',
        'content': 'why is the sky blue',

    },
])

print(response['messages']['content'])