import openai

# Set your OpenAI GPT-3.5 Turbo API key
openai.api_key = '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'

# Your input prompt
prompt = "Translate the following English text to French: '{}'"
text_to_translate = "Hello, how are you?"

# New API call using ChatCompletion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.format(text_to_translate)}
    ],
    max_tokens=60
)

# Extract the generated text from the response
translated_text = response['choices'][0]['message']['content']

# Print the translated text
print(translated_text)



#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