import { openai } from '@ai-sdk/openai';

/**
 * OpenAI Model Configuration
 * You can switch models easily (e.g., 'gpt-4o-mini', 'gpt-4o', 'gpt-4-turbo')
 */
export const defaultModel = openai('gpt-4o-mini');

export const customModel = (modelName: string) => {
  return openai(modelName);
};
