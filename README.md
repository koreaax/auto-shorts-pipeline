# ⚡ Next.js AI SaaS Starter Kit

> **Launch your AI Micro-SaaS in hours, not weeks.**  
> A production-ready, batteries-included boilerplate built with Next.js 15, Vercel AI SDK, Supabase, Tailwind CSS, and Lemon Squeezy / Stripe.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Next.js](https://img.shields.io/badge/Next.js-15-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![TailwindCSS](https://img.shields.io/badge/Tailwind-v3.4-38bdf8)

---

## 🔥 Features

- ⚡ **Next.js 15 (App Router)** - Server Components, Server Actions, & Route Handlers.
- 🤖 **Vercel AI SDK** - Streaming responses with OpenAI (GPT-4o / GPT-4o-mini) and Claude out-of-the-box.
- 🎨 **Modern Dark UI** - Premium design built with Tailwind CSS & Lucide Icons.
- 🔐 **Authentication & Database** - Powered by Supabase (Social Logins & User Management).
- 💳 **Payments & Subscriptions** - Webhook-ready integration with **Lemon Squeezy** & **Stripe**.
- 📱 **Fully Responsive** - Mobile-first UI for landing page, auth, and dashboard.
- 🚀 **1-Click Deployment** - Vercel & Netlify ready.

---

## 📁 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Framework** | Next.js 15 (React 19 / App Router) |
| **Language** | TypeScript |
| **Styling** | Tailwind CSS + Lucide React Icons |
| **AI Engine** | Vercel AI SDK (`ai`) + `@ai-sdk/openai` |
| **Database & Auth** | Supabase (`@supabase/ssr`) |
| **Payments** | Lemon Squeezy / Stripe Webhooks |

---

## ⚡ Quick Start

### 1. Clone the repository & Install dependencies

```bash
git clone https://github.com/your-username/next-ai-saas-starter.git
cd next-ai-saas-starter
npm install
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env.local` and fill in your credentials:

```bash
cp .env.example .env.local
```

### 3. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

---

## 📂 Project Structure

```text
├── app/
│   ├── api/
│   │   ├── chat/route.ts      # Vercel AI SDK Streaming Endpoint
│   │   └── webhook/route.ts   # Payment Webhook Handler
│   ├── dashboard/page.tsx     # Main AI Dashboard UI
│   ├── login/page.tsx         # Supabase Auth Login Page
│   ├── layout.tsx             # Root Layout with Font & Theme Providers
│   └── page.tsx               # High-Converting Landing Page
├── components/
│   ├── ai-chat-form.tsx       # Interactive AI Streaming Form
│   ├── landing-hero.tsx       # Hero Section with CTA
│   └── pricing-table.tsx      # Subscription Pricing Cards
├── lib/
│   ├── ai.ts                  # OpenAI / Claude Config
│   └── supabase.ts            # Supabase Server/Client Setup
└── .env.example               # Environment Variables Template
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
