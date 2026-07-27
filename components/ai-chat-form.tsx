'use client';

import React from 'react';
import { useChat } from 'ai/react';
import { Send, Bot, User, Sparkles } from 'lucide-react';

export function AIChatForm() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
    api: '/api/chat',
  });

  return (
    <div className="w-full max-w-3xl mx-auto bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden flex flex-col h-[600px]">
      {/* Header */}
      <div className="px-6 py-4 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="p-2 rounded-xl bg-violet-600/20 border border-violet-500/30 text-violet-400">
            <Sparkles className="w-5 h-5" />
          </div>
          <div>
            <h2 className="font-semibold text-white">AI Assistant Demo</h2>
            <p className="text-xs text-slate-400">Powered by GPT-4o-mini & Vercel AI SDK</p>
          </div>
        </div>
      </div>

      {/* Messages Area */}
      <div className="flex-1 p-6 overflow-y-auto space-y-4">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center text-slate-500">
            <Bot className="w-12 h-12 mb-3 text-slate-600" />
            <p className="font-medium text-slate-400">Ask me anything to test the streaming response!</p>
            <p className="text-xs text-slate-600 mt-1">Try: "Write a short poem about code" or "Explain SaaS in 2 sentences"</p>
          </div>
        ) : (
          messages.map((m) => (
            <div
              key={m.id}
              className={`flex gap-3 ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              {m.role !== 'user' && (
                <div className="w-8 h-8 rounded-full bg-violet-600/20 border border-violet-500/30 flex items-center justify-center text-violet-400 flex-shrink-0">
                  <Bot className="w-4 h-4" />
                </div>
              )}
              <div
                className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
                  m.role === 'user'
                    ? 'bg-violet-600 text-white rounded-br-none'
                    : 'bg-slate-800 text-slate-200 border border-slate-700/60 rounded-bl-none'
                }`}
              >
                {m.content}
              </div>
              {m.role === 'user' && (
                <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-slate-400 flex-shrink-0">
                  <User className="w-4 h-4" />
                </div>
              )}
            </div>
          ))
        )}
      </div>

      {/* Input Form */}
      <form onSubmit={handleSubmit} className="p-4 bg-slate-950/80 border-t border-slate-800 flex gap-2">
        <input
          value={input}
          onChange={handleInputChange}
          placeholder="Type your prompt..."
          disabled={isLoading}
          className="flex-1 bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-violet-500 transition"
        />
        <button
          type="submit"
          disabled={isLoading || !input.trim()}
          className="px-5 py-3 rounded-xl bg-violet-600 hover:bg-violet-500 disabled:opacity-50 text-white font-medium flex items-center gap-2 transition"
        >
          <span>Send</span>
          <Send className="w-4 h-4" />
        </button>
      </form>
    </div>
  );
}
