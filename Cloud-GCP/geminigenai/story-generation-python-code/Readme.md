
## app.py code 
```
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API key for generative AI
genai.configure(api_key=os.getenv("API_KEY"))

# Use the generative model
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
```

## setup .env 
API_KEY=<key>

## setup env 
sudo python3 -m venv .venv
source .venv/bin/activate

## install packages 
pip install python-dotenv
pip install -U google-generativeai
 
 
 
## run app 
python app.py 

## output:
python app.py
Twelve-year-old Lily clutched the worn leather backpack, its frayed straps digging into her small shoulders. It wasn't the backpack itself that was special, though. It was what resided within. A gift from her eccentric grandmother, the backpack was said to be enchanted, able to hold anything Lily could imagine, as long as she believed.

Lily, a dreamer at heart, believed wholeheartedly. She’d already tested the backpack’s magic. One day, she’d envisioned a perfect chocolate cake, and the next, it materialized, complete with frosting and sprinkles. Another time, a fluffy white kitten appeared, purring contentedly in her lap. It was a world of endless possibilities, a secret she kept hidden from everyone but her best friend, Max.

Their lives in the dusty, forgotten town of Willow Creek were dull. Days were spent in the same, monotonous routine, and the only excitement came from their shared dreams of escaping their mundane lives. They yearned for adventure, for a world beyond the dusty streets and faded buildings.

One day, Max confessed, "I wish I could have a pirate ship. A real one, with sails billowing in the wind and cannons roaring."

Lily, eyes sparkling, said, "Then you will! We can sail the seven seas, find buried treasure, and fight off pirates ourselves!" She grinned, a mischievous glint in her eyes.

That night, under the watchful gaze of the moon, they stood before the backpack. "Pirate ship, complete with cannons, sails, and treasure!" Lily commanded, her voice filled with conviction.

The next morning, a gasp escaped Max's lips. In their backyard stood a magnificent pirate ship, sails billowing in the morning breeze.

"It's real!" Max shouted, his voice filled with disbelief and excitement. "It's real!"

For days, they lived on their own pirate ship, braving storms, battling phantom foes, and searching for hidden treasures.  They sailed the seas of their imagination, their laughter echoing across the waves.

The magic of the backpack didn't just offer adventures; it also brought them closer, strengthening their bond with each other. They shared their dreams, their fears, and their hopes, their friendship growing stronger with each shared adventure.

One evening, as the sun dipped below the horizon, painting the sky in hues of orange and purple, Max turned to Lily. "This is the best," he said, his voice filled with a contentment Lily had never heard before. "This is better than anything I could have ever imagined."

Lily smiled, knowing that their adventures were just beginning. The magic backpack, a symbol of their friendship and their shared dreams, would forever remain a constant in their lives, a reminder that even in the most mundane of worlds, extraordinary adventures awaited them, if only they dared to dream.
