Readme by Hari Thaplyal

.env file with
``` 
export API_KEY=<YOUR_API_KEY>
```

package.json file with
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

app.js file with
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

from wsl shell installed
```
npm install @google/generative-ai
npm install dotenv
```


run the code
```
node app.js
```

