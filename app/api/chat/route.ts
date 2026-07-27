import { streamText } from 'ai';
import { defaultModel } from '@/lib/ai';

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

export async function POST(req: Request) {
  try {
    const { messages } = await req.json();

    const result = streamText({
      model: defaultModel,
      system: 'You are a helpful, brilliant AI assistant powered by Next-AI-SaaS-Starter.',
      messages,
    });

    return result.toDataStreamResponse();
  } catch (error) {
    console.error('AI Streaming Error:', error);
    return new Response(
      JSON.stringify({ error: 'Failed to process AI response' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
