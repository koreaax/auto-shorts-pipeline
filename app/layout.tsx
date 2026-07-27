import type { Metadata } from 'next';
import React from 'react';
import './globals.css';

export const metadata: Metadata = {
  title: 'Next-AI-SaaS-Starter | Launch Your AI Micro-SaaS',
  description: 'Production-ready boilerplate with Next.js 15, Vercel AI SDK, Supabase, and Lemon Squeezy.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-slate-950 text-slate-100 antialiased font-sans">
        {children}
      </body>
    </html>
  );
}
