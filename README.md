

# Splitify

> A modern, AI‑powered expense app for effortless group splitting and settlements.

<div align="center">

[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=white)](https://react.dev/)
[![Convex](https://img.shields.io/badge/Convex-Realtime%20DB-orange)](https://convex.dev/)
[![Clerk](https://img.shields.io/badge/Clerk-Auth-6C47FF)](https://clerk.com/)

[![Gemini](https://img.shields.io/badge/Gemini-AI-4285F4)](https://ai.google.dev/)
[![Inngest](https://img.shields.io/badge/Inngest-Jobs-0EA5E9)](https://www.inngest.com/)
[![Resend](https://img.shields.io/badge/Resend-Email-111111)](https://resend.com/)
[![MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>


UI inspired by RoadsideCoder — thanks for the clean UX direction.

## Overview

Splitify helps groups track shared expenses, manage settlements, and get AI insights into monthly spending. It uses:
- Next.js App Router + React Server Components
- Convex for real-time data and serverless functions
- Clerk for authentication
- Gemini API for monthly expense analysis and insights
- Inngest for background workflows
- Resend for transactional emails

## Features

- Individual and group expenses
- Multiple split methods (equal, percentage, exact)
- Real-time balances and settlements
- AI monthly insights (Gemini): category breakdowns, trends, suggestions
- Group management and invitations
- Email notifications (Resend)
- Background jobs for reports/reminders (Inngest)
- Secure auth (Clerk), responsive UI (Tailwind + shadcn/ui)

## Tech Stack

- App: Next.js 15, React 19, TypeScript, Tailwind CSS, shadcn/ui
- Backend: Convex (DB + functions)
- Auth: Clerk (JWT, OIDC)
- AI: Google Gemini API
- Jobs: Inngest
- Email: Resend
- Deploy: Vercel (Edge-ready)

## Project Structure

```
app/                     # Next.js routes (App Router)
components/              # UI and providers (incl. Convex+Clerk)
convex/                  # Convex schema & functions
  _generated/            # Auto-generated bindings (do not edit)
  auth.config.js         # OIDC issuer config for Clerk
  schema.js              # Tables: users, groups, expenses, etc.
lib/                     # Utils, inngest workflows, email builders
hooks/                   # Shared React hooks
public/                  # Static assets
```

## Environment Variables

Create .env.local

```
# Convex
CONVEX_DEPLOYMENT=dev:your-deploy
NEXT_PUBLIC_CONVEX_URL=https://<your>.convex.cloud

# Clerk
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
CLERK_JWT_ISSUER_DOMAIN=https://<your>.clerk.accounts.dev

# AI
GEMINI_API_KEY=...

# Emails
RESEND_API_KEY=re_...

# Background jobs
INNGEST_EVENT_KEY=...
INNGEST_SIGNING_KEY=...
```

Notes:
- NEXT_PUBLIC_* is browser-exposed; keep secrets without this prefix.
- Convex must see CLERK_JWT_ISSUER_DOMAIN (locally and in Convex Cloud).

## Local Development

1) Install
- npm install

2) Configure env
- copy .env.local and fill values

3) Start Convex (ensure issuer is in env)
- CLERK_JWT_ISSUER_DOMAIN=... npx convex dev

4) Start app
- npm run dev

5) Open
- http://localhost:3000

## Convex Functions

- Define queries/mutations in convex/ only (not in app/).
- Call from client via useQuery/useMutation.
- Call from server (SSR) using ConvexHttpClient:

```ts
import { ConvexHttpClient } from 'convex/browser';
import { api } from '@/convex/_generated/api';

const convex = new ConvexHttpClient(process.env.NEXT_PUBLIC_CONVEX_URL!);
const data = await convex.query(api.groups.getGroupOrMembers, {});
```

## Authentication

- ClerkProvider in app/layout.tsx
- ConvexProviderWithClerk in components/convex-client-provider
- OIDC issuer configured in convex/auth.config.js using CLERK_JWT_ISSUER_DOMAIN

## Deployment

- Next.js → Vercel
- Convex → npx convex deploy
- Set env vars in both Vercel and Convex Cloud
- Use production Clerk keys and issuer

Post-deploy checklist:
- Issuer set in Convex Cloud
- NEXT_PUBLIC_CONVEX_URL updated
- AI/Resend/Inngest keys added

## Troubleshooting

- “No auth provider found matching the given token”
  - Cause: Issuer not present in Convex runtime
  - Fix: Set CLERK_JWT_ISSUER_DOMAIN for convex dev/prod and restart

- ctx.runQuery is not a function
  - Cause: Function ran in Next.js runtime
  - Fix: Move handlers to convex/, call via Convex client

- ArgumentValidationError with v.id(...)
  - Cause: Mismatched table id type
  - Fix: Pass correct id type (e.g., v.id('groups') for groupId)

## Scripts

- npm run dev — Next.js dev server
- npx convex dev — Convex local runtime
- npm run build — Build app
- npm run start — Start production build
- npx convex deploy — Deploy Convex

## Testing

- E2E automation via Selenium (Python)
- Covers auth, individual/group expenses, settlements, AI insights
- ~130s full run, screenshots on failure

Optional layout:
testing/
- main.py
- requirements.txt

## Credits

- UI inspiration: RoadsideCoder (Piyush Garg)
- Components: shadcn/ui
- Icons: Lucide

## License

MIT — see LICENSE

