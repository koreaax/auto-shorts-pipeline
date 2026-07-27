import React from 'react';
import { AIChatForm } from '@/components/ai-chat-form';
import { ArrowLeft } from 'lucide-react';
import Link from 'next/link';

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-slate-950 p-6 md:p-12">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center justify-between mb-8">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-white transition"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back to Home</span>
          </Link>
          <div className="text-xs text-slate-500 font-mono">Demo Mode (No Auth Required)</div>
        </div>

        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-white mb-2">AI Dashboard Preview</h1>
          <p className="text-slate-400 text-sm">
            Test the real-time Vercel AI SDK streaming response below.
          </p>
        </div>

        <AIChatForm />
      </div>
    </div>
  );
}
