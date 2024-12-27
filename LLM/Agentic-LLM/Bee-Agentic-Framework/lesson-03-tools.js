import "dotenv/config";
import {GroqChatLLM} from 'bee-agent-framework/adapters/groq/chat';
import {BaseMessage, Role } from 'bee-agent-framework/llms/primitives/message';
import readline from "readline/promises";
import {BeeAgent} from 'bee-agent-framework/agents/bee/agent';
import {TokenMemory} from 'bee-agent-framework/memory/tokenMemory';
import {DuckDuckGoSearchTool} from 'bee-agent-framework/tools/search/duckDuckGoSearch';
import {OpenMeteoTool} from 'bee-agent-framework/tools/weather/openMeteo'


const llm = new GroqChatLLM({
    modelId: 'llama-3.3-70b-specdec'
});

const rl = new readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const tools = [
    new DuckDuckGoSearchTool(),
    new OpenMeteoTool()
    ];
    
const memory = new TokenMemory( {llm} );

const agent = new BeeAgent({
    llm, 
    memory, 
    tools,
});
    


const processMessage = async (message) => {
   const response = await agent
   .run({
       prompt: message,
   })
   .observe((emitter) => {
    emitter.on("update", ({data, update, meta})=> {
        console.log(`Agent ${update.key}: ${update.value}`)

    });
   });
   console.log("Assistant: ", response.result.text);
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