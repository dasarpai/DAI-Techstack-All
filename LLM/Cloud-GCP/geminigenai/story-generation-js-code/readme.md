# Readme by Hari Thaplyal

Create API Key from 
https://aistudio.google.com/app/apikey

## .env file with
``` 
export API_KEY=<YOUR_API_KEY>
```

## package.json file with
```
{
  "name": "geminigenai-js",
  "type": "module",
  "dependencies": {
    "@google/generative-ai": "^0.21.0",
    "dotenv": "^16.4.5"
  }
}

```

## app.js file with
```
// Import required packages
import { GoogleGenerativeAI } from "@google/generative-ai";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

async function generateStory() {
  const genAI = new GoogleGenerativeAI(process.env.API_KEY);
  const model = await genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

  const prompt = "Write a story about a magic backpack.";
  const result = await model.generateContent(prompt);
  console.log(result.response.text);
}

// Run the async function
generateStory().catch(console.error);

```

## from wsl shell installed
```
npm install @google/generative-ai
npm install dotenv
```


## run the code
```
node app.js
```

## Output
The rain hammered on the attic window, mimicking the frantic beat of 12-year-old Finn's heart. He clutched the dusty, leather backpack, his only inheritance from his eccentric Great-Aunt Agatha, who had vanished mysteriously a year ago. Whispers of magic surrounded her, whispers Finn now understood to be true.

He'd always loved exploring the attic, its dusty shelves overflowing with odd trinkets and forgotten stories. Today, he was finally opening the backpack.  He unbuckled the leather straps, revealing a worn brass lock. Inside, nestled between layers of worn velvet, lay a single, shimmering pearl.

As Finn reached for it, the pearl pulsed with light, the attic filling with a strange, ethereal hum. Suddenly, the backpack sprang to life, unzipping itself with a metallic click.  Inside, swirling mist materialized into a miniature, fantastical landscape. Tiny houses nestled amongst glowing mushrooms, and a winding river flowed with a liquid that shimmered like starlight.

A miniature figure, no bigger than Finn's thumb, materialized in the backpack, her wings shimmering with the colours of a thousand sunsets. "Greetings, young adventurer," she chirped, her voice echoing in Finn's head. "I am Celeste, guardian of the Magic Pack."

Finn blinked, stunned. "Magic Pack?"

Celeste chuckled, her tiny form bouncing excitedly. "This backpack is no ordinary thing, young one. It's a gateway to endless possibilities! Within it lies the power to travel to fantastical realms, learn ancient languages, and even shape your own destiny!"

Finn, his heart pounding with excitement, was quickly swept up in Celeste's enthusiasm. He spent hours exploring the miniature world, learning about its history and its magic. He learned about the other fantastical realms the backpack could take him to, from underwater cities to soaring cloud kingdoms.

Over the next few months, Finn found himself venturing into these realms, each one more fantastical than the last. He befriended a mischievous talking squirrel in the Whispering Woods, helped a grumpy dragon mend his broken wing in the Firelands, and learned the secrets of the ocean from a wise sea turtle in the Coral Reefs.

But with each adventure, Finn realised that the magic pack wasn't just about escape, it was about understanding himself. It taught him about courage, kindness, and the importance of embracing the unknown. He learned to use the magic within himself, to find his own strength and imagination.

As Finn grew older, the backpack became more than just a magical portal; it became a symbol of his journey, a reminder that even the most ordinary objects can hold extraordinary secrets, and that within us all, there is the power to create our own magic. And so, with a backpack on his back and a heart full of wonder, Finn continued to explore the world, embracing every adventure, every challenge, and every bit of magic that life offered.
