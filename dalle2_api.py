import openai
import requests

openai.api_key = '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' # E Dalle2 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
center_word = 'baby'
# apple_sentences = [
#     "An apple tree stands tall in a verdant orchard, its branches laden with shiny, red apples.",
#     "A single apple rests on a table, its glossy skin reflecting the morning sunlight.",
#     "An apple pie cooling on a windowsill, its golden crust dusted with sugar crystals.",
#     "A child reaches up, his small hand grasping for a ripe apple hanging from a low branch.",
#     "A basket filled with a variety of apples; red, green, and golden, freshly harvested from the orchard.",
#     "A hand holding a bitten apple, its juicy interior exposed.",
#     "A sliced apple on a cutting board, its crisp white flesh contrasting with the vibrant red skin.",
#     "Apple blossoms in full bloom, signaling the arrival of spring.",
#     "A jug of apple cider on a rustic wooden table, surrounded by fallen autumn leaves.",
#     "An old-fashioned apple press, ready to transform the season's harvest into delicious juice."
# ]
baby_sentences = [
    "A baby's infectious laughter fills the room as she plays with a brightly colored toy.",
    "The baby is sleeping soundly in her crib, wrapped snugly in a soft, pink blanket.",
    "A baby takes her first tentative steps, her wide eyes filled with determination and wonder.",
    "A mother cradles her baby, humming a gentle lullaby that echoes softly through the room.",
    "The baby grabs a spoon and attempts to feed himself, getting more food on his face than in his mouth.",
    "A baby reaches out to touch her father's face, her tiny fingers tracing his features.",
    "The baby's eyes light up at the sight of the family pet, a curious giggle escaping her lips.",
    "Wrapped in a warm towel, the baby coos contentedly after her bath.",
    "The baby kicks her legs in excitement as she watches colorful mobile spinning above her crib.",
    "A father lifts his baby high into the air, causing her to squeal with delight."
]

for i in list(range(10)):
  
  response = openai.Image.create(
    prompt=baby_sentences[i],
    n=1,
    size="512x512"
  )

  # assuming the response contains a URL of the generated image
  image_url = response['data'][0]['url']
  # download the image and save it locally
  img_data = requests.get(image_url).content
  with open(center_word + str(i)+ '.jpg', 'wb') as handler:
      handler.write(img_data)