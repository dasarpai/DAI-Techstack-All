// app/api/agent/route.ts
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import { TokenMemory } from "bee-agent-framework/memory/tokenMemory";
import { DuckDuckGoSearchTool } from "bee-agent-framework/tools/search/duckDuckGoSearch";
import { OpenMeteoTool } from "bee-agent-framework/tools/weather/openMeteo";
import { GroqChatLLM } from "bee-agent-framework/adapters/groq/chat";
import { NextResponse } from "next/server";

// Initialize agent
const llm = new GroqChatLLM({
  modelId: "llama-3.1-70b-versatile",
});

const agent = new BeeAgent({
  llm,
  memory: new TokenMemory({ llm }),
  tools: [new DuckDuckGoSearchTool(), new OpenMeteoTool()],
});

export async function POST(request: Request) {
  try {
    const { prompt } = await request.json();

    const updates: any[] = [];
    const response = await agent.run({ prompt }).observe((emitter) => {
      emitter.on("update", async ({ data, update, meta }) => {
        updates.push({
          type: update.key,
          content: update.value,
        });
      });
    });

    return NextResponse.json({
      result: response.result.text,
      updates,
    });
  } catch (error) {
    console.error("Error during agent execution:", error);
    return NextResponse.json(
      { error: "Failed to process agent request" },
      { status: 500 }
    );
  }
}
