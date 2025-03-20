import { OpenAI } from 'openai';
import { NextResponse } from 'next/server';

if (!process.env.NEBIUS_API_KEY) {
  throw new Error('Missing Nebius API Key');
}

const client = new OpenAI({
  baseURL: 'https://api.studio.nebius.com/v1/',
  apiKey: process.env.NEBIUS_API_KEY,
});

export const dynamic = 'force-dynamic';

export async function POST(req: Request) {
  try {
    const { prompt } = await req.json();

    if (!prompt) {
      return NextResponse.json(
        { error: 'Prompt is required' },
        { status: 400 }
      );
    }

    const response = await client.images.generate({
      model: "black-forest-labs/flux-dev",
      response_format: "b64_json",
      extra_body: {
        response_extension: "webp",
        width: 1024,
        height: 1024,
        num_inference_steps: 28,
        negative_prompt: "",
        seed: -1
      },
      prompt: prompt,
    });

    if (!response.data?.[0]?.b64_json) {
      throw new Error('No image data received from Nebius');
    }

    // Convert base64 to data URL
    const imageUrl = `data:image/webp;base64,${response.data[0].b64_json}`;
    return NextResponse.json({ imageUrl });
  } catch (error: any) {
    console.error('Error generating image:', error);
    return NextResponse.json(
      { error: error.message || 'Failed to generate image' },
      { status: 500 }
    );
  }
}