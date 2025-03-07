import "dotenv/config";
import {GroqChatLLM} from 'bee-agent-framework/adapters/groq/chat';
import {BaseMessage, Role } from 'bee-agent-framework/llms/primitives/message';
import readline from "readline/promises";

const rl = new readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const llm = new GroqChatLLM({
    modelId: 'llama-3.2-3b-preview'
});

const processMessage = async (message) => {
      
const response = await llm.generate([
    BaseMessage.of({
        role: Role.USER,
        text:  message,
    }),
]);

console.log("Assistant:", response.getTextContent());
};


const startChat = async () => {
    while (true) {
        const message = await rl.question('You: ');
        
        if (message.toLowerCase() === 'bye') {
            console.log("Assistant: Goodbye!")
            rl.close();
            break;
        }

        await processMessage(message)
    }
}

startChat();