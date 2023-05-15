import openai
import requests

openai.api_key = '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' # E Dalle2 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

i = 0
center_word = 'apple'
response = openai.Image.create(
  prompt="A single apple rests on a table, its glossy skin reflecting the morning sunlight",
  n=1,
  size="512x512"
)

# assuming the response contains a URL of the generated image
image_url = response['data'][0]['url']
# download the image and save it locally
img_data = requests.get(image_url).content
with open(center_word + str(i)+ '.jpg', 'wb') as handler:
    handler.write(img_data)