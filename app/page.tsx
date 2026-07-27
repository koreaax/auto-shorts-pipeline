import React from 'react';
import { LandingHero } from '@/components/landing-hero';
import { PricingTable } from '@/components/pricing-table';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950">
      <LandingHero />
      <PricingTable />
      <footer className="py-8 border-t border-slate-800 text-center text-xs text-slate-500">
        © 2026 Next-AI-SaaS-Starter. Ready to ship.
      </footer>
    </main>
  );
}
