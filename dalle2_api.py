import openai
import requests

openai.api_key = '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' # E Dalle2

response = openai.Image.create(
  prompt="A baby's infectious laughter fills the room as she plays with a brightly colored toy.",
  n=1,
  size="512x512"
)

# assuming the response contains a URL of the generated image
image_url = response['data'][0]['url']
# download the image and save it locally
img_data = requests.get(image_url).content
with open('output_image.jpg', 'wb') as handler:
    handler.write(img_data)