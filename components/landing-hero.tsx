import React from 'react';
import { ArrowRight, Sparkles, Zap, Shield, Rocket } from 'lucide-react';

export function LandingHero() {
  return (
    <section className="relative overflow-hidden pt-24 pb-16 md:pt-32 md:pb-24 bg-slate-950 text-white">
      {/* Background Gradient Effect */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-gradient-to-tr from-violet-600/30 via-fuchsia-600/20 to-transparent blur-3xl rounded-full pointer-events-none" />

      <div className="max-w-6xl mx-auto px-4 sm:px-6 text-center relative z-10">
        {/* Badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-violet-500/10 border border-violet-500/20 text-violet-400 text-sm font-medium mb-8">
          <Sparkles className="w-4 h-4 text-violet-400" />
          <span>Next.js 15 & Vercel AI SDK Ready</span>
        </div>

        {/* Main Title */}
        <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight mb-6 bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">
          Ship Your AI SaaS <br />
          <span className="bg-gradient-to-r from-violet-400 via-fuchsia-400 to-pink-400 bg-clip-text text-transparent">
            In Hours, Not Weeks.
          </span>
        </h1>

        {/* Subtitle */}
        <p className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed">
          The ultimate boilerplate with Next.js 15, Streaming AI responses, Supabase Auth, 
          and Lemon Squeezy payment integration pre-configured.
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <a
            href="/dashboard"
            className="w-full sm:w-auto px-8 py-4 rounded-xl bg-violet-600 hover:bg-violet-500 text-white font-semibold flex items-center justify-center gap-2 shadow-lg shadow-violet-600/25 transition-all duration-200"
          >
            <span>Try AI Dashboard</span>
            <ArrowRight className="w-5 h-5" />
          </a>
          <a
            href="#pricing"
            className="w-full sm:w-auto px-8 py-4 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 font-semibold transition-all duration-200"
          >
            View Pricing
          </a>
        </div>

        {/* Feature Icons */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-20 pt-10 border-t border-slate-800/60 text-left">
          <div className="p-6 rounded-2xl bg-slate-900/50 border border-slate-800/80">
            <Zap className="w-8 h-8 text-amber-400 mb-4" />
            <h3 className="text-lg font-bold text-white mb-2">Lightning Fast AI</h3>
            <p className="text-sm text-slate-400">Stream GPT-4o & Claude responses in real-time with zero lag.</p>
          </div>
          <div className="p-6 rounded-2xl bg-slate-900/50 border border-slate-800/80">
            <Shield className="w-8 h-8 text-emerald-400 mb-4" />
            <h3 className="text-lg font-bold text-white mb-2">Supabase Auth</h3>
            <p className="text-sm text-slate-400">Secure user management and database pre-configured with RLS.</p>
          </div>
          <div className="p-6 rounded-2xl bg-slate-900/50 border border-slate-800/80">
            <Rocket className="w-8 h-8 text-fuchsia-400 mb-4" />
            <h3 className="text-lg font-bold text-white mb-2">Instant Monetization</h3>
            <p className="text-sm text-slate-400">Lemon Squeezy & Stripe webhooks ready for subscription payments.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
