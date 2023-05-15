# import openai
# import os

# openai.api_key = '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' # E prompts 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

# # categories = ['apple', 'aquarium_fish', 'baby', 'bear']  # Add your categories here
# categories = ['bed', 'bee', 'beetle', 'bicycle']  # Add your categories here

# output = {}

# for category in categories:
#     responses = openai.Completion.create(
#       engine="text-davinci-002",  # Use the latest available version
#       prompt=f"Generate 10 sentences about {category}:\n. I will use those sentences to generate images. You can decide the style.",
#       temperature=0.5,
#       max_tokens=150,
#       n=10  # Generate 10 completions
#     )

#     output[category] = [response['choices'][0]['text'].strip() for response in responses['choices']]

# print(output)

import openai
import os

openai.api_key = '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'

categories = ['whale', 'willow_tree', 'wolf', 'woman', 'worm']

# categories = ['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'car', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']

output = {}

for category in categories:
    response = openai.Completion.create(
      engine="text-davinci-002",  
      prompt=f"Generate 10 sentences about {category}:\n. I will use those sentences to generate images. You can decide the style.",
      temperature=0.5,
      max_tokens=150,
      n=1
    )

    output[category] = [choice['text'].strip() for choice in response['choices']]

print(output)

