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
  console.log(result.response.text());
}

// Run the async function
generateStory().catch(console.error);
