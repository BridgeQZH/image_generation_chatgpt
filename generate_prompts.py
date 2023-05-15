import openai
import os

openai.api_key = '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'

# categories = ['apple', 'aquarium_fish', 'baby', 'bear']  # Add your categories here
categories = ['bed', 'bee', 'beetle', 'bicycle']  # Add your categories here

output = {}

for category in categories:
    responses = openai.Completion.create(
      engine="text-davinci-002",  # Use the latest available version
      prompt=f"Generate 10 sentences about {category}:\n. I will use those sentences to generate images. You can decide the style.",
      temperature=0.5,
      max_tokens=150,
      n=10  # Generate 10 completions
    )

    output[category] = [response['choices'][0]['text'].strip() for response in responses]

print(output)
