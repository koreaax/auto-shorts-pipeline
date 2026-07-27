import React from 'react';
import { Check } from 'lucide-react';

const plans = [
  {
    name: 'Hobby',
    price: '$9',
    description: 'Perfect for side projects and small AI experiments.',
    features: ['10,000 AI Credits / mo', 'GPT-4o Mini Access', 'Community Support', 'Basic Analytics'],
    cta: 'Get Started',
    popular: false,
  },
  {
    name: 'Pro',
    price: '$29',
    description: 'For creators & developers launching commercial SaaS.',
    features: [
      '100,000 AI Credits / mo',
      'GPT-4o & Claude 3.5 Access',
      'Priority Email Support',
      'Advanced Analytics',
      'Custom System Prompts',
    ],
    cta: 'Start 7-Day Free Trial',
    popular: true,
  },
  {
    name: 'Enterprise',
    price: '$99',
    description: 'Unlimited capacity for teams and scaling apps.',
    features: [
      'Unlimited AI Credits',
      'Custom Model Fine-tuning',
      '24/7 Dedicated Support',
      'Custom Domain Support',
      'SLA Guarantee',
    ],
    cta: 'Contact Sales',
    popular: false,
  },
];

export function PricingTable() {
  return (
    <section id="pricing" className="py-20 bg-slate-950 text-white relative">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-5xl font-extrabold tracking-tight mb-4">
            Simple, Transparent Pricing
          </h2>
          <p className="text-slate-400 text-lg max-w-xl mx-auto">
            Choose the plan that fits your AI SaaS needs. Upgrade or cancel anytime.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {plans.map((plan, idx) => (
            <div
              key={idx}
              className={`relative p-8 rounded-3xl border transition-all duration-200 flex flex-col justify-between ${
                plan.popular
                  ? 'bg-slate-900 border-violet-500/50 shadow-xl shadow-violet-500/10 ring-1 ring-violet-500'
                  : 'bg-slate-900/40 border-slate-800'
              }`}
            >
              {plan.popular && (
                <div className="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-violet-600 text-white text-xs font-semibold uppercase tracking-wider">
                  Most Popular
                </div>
              )}

              <div>
                <h3 className="text-xl font-bold mb-2">{plan.name}</h3>
                <p className="text-sm text-slate-400 mb-6">{plan.description}</p>
                <div className="mb-6">
                  <span className="text-4xl font-extrabold">{plan.price}</span>
                  <span className="text-slate-400 font-medium"> / month</span>
                </div>

                <ul className="space-y-3 mb-8">
                  {plan.features.map((feature, fIdx) => (
                    <li key={fIdx} className="flex items-center gap-3 text-sm text-slate-300">
                      <Check className="w-4 h-4 text-violet-400 flex-shrink-0" />
                      <span>{feature}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <button
                className={`w-full py-3.5 rounded-xl font-semibold transition-all ${
                  plan.popular
                    ? 'bg-violet-600 hover:bg-violet-500 text-white shadow-lg shadow-violet-600/20'
                    : 'bg-slate-800 hover:bg-slate-700 text-slate-200'
                }`}
              >
                {plan.cta}
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
