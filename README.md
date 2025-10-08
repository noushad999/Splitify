# Splitify

Splitify is a modern web application to split expenses and manage group
payments. This repository contains the Next.js frontend, Convex server
functions, and integration with Clerk for authentication.

This README provides a professional-level guide to understand, run, develop, and
deploy the project.

## Table of contents

- Project overview
- Architecture and folders
- Tech stack
- Environment variables
- Local development
- Convex functions (local & cloud)
- Clerk authentication
- Deployment
- Troubleshooting (common errors)
- Contributing
- Contact

## Project overview

Splitify helps groups track shared expenses, payments, and settlements. The
project uses Next.js for the frontend and Convex for serverless functions and
data storage. Clerk handles user authentication and issues JWTs that Convex
validates.

## Architecture and folders

- `app/` — Next.js App Router pages and layouts (React 19 server components and
  client components).
- `components/` — Reusable UI components and the Convex client provider.
- `convex/` — Convex functions, schema, and auth configuration (server-side
  business logic executed by Convex).
- `lib/` — Utility libraries (e.g., background jobs/integrations with Inngest,
  email builders).
- `hooks/` — React hooks used across the app.
- `public/` — Static assets (images, logos).
- `convex/_generated/` — Generated Convex client/server bindings (do not edit
  manually).

Key files:

- `convex/auth.config.js` — Convex auth configuration (OIDC issuers). Must be
  configured for Clerk.
- `convex/schema.js` — Convex schema definitions for tables like `users`,
  `groups`, `expenses`, etc.
- `components/convex-client-provider.jsx` — Wraps the app with Convex provider
  and Clerk integration.
- `app/layout.js` — App root layout where `ClerkProvider` and Convex client
  provider are mounted.

## Tech stack

- Next.js 15 (App Router)
- React 19
- Convex (serverless functions & database)
- Clerk (authentication)
- Tailwind CSS
- Inngest (background jobs)

## Environment variables

Store runtime secrets in environment variables. Typical local variables (example
located in `.env.local`):

- CONVEX_DEPLOYMENT=dev:rightful-ox-164
- NEXT_PUBLIC_CONVEX_URL=https://rightful-ox-164.convex.cloud
- NEXT*PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test*...
- CLERK*SECRET_KEY=sk_test*...
- NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
- NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
- CLERK_JWT_ISSUER_DOMAIN=https://your-clerk-issuer.accounts.dev
- RESEND_API_KEY=... (if using Resend for emails)

Important notes:

- `NEXT_PUBLIC_*` variables are exposed to the browser; secrets (e.g.,
  `CLERK_SECRET_KEY`) must not be prefixed with NEXT_PUBLIC.
- Convex must be able to read `CLERK_JWT_ISSUER_DOMAIN` when running Convex
  functions (either locally via a shell where the var is set or set in Convex
  Cloud environment variables). If Convex does not see the issuer, it will
  respond with:
  `No auth provider found matching the given token (no providers configured).`

## Local development

1. Install dependencies

   npm install

2. Copy `.env.local.example` (or create `.env.local`) and set the required env
   vars (see Environment variables above).

3. Start Convex (local functions)

   In the shell where `CLERK_JWT_ISSUER_DOMAIN` is available, run:

   CLERK_JWT_ISSUER_DOMAIN=https://pretty-wren-31.clerk.accounts.dev npx convex
   dev

   Note: Convex must load the issuer env var so it can validate Clerk JWTs.

4. Start Next.js

   npm run dev

5. Open http://localhost:3000

## Convex functions (local & cloud)

- Place Convex function files in `convex/`. These files run within Convex's
  runtime and can use `ctx.runQuery`, `ctx.db`, etc.
- Do not define Convex `query`/`mutation` handlers inside Next.js `app/` routes
  — doing so will run them in the Next runtime and `ctx` will be missing
  Convex-specific functions (e.g., `ctx.runQuery`) which causes runtime errors.
- To call Convex functions from the Next server (SSR) environment, use the
  Convex HTTP client:

  ```js
  import { ConvexHttpClient } from 'convex/browser';
  import { api } from '@/convex/_generated/api';

  const convex = new ConvexHttpClient(process.env.NEXT_PUBLIC_CONVEX_URL);
  const data = await convex.query(api.groups.getGroupOrMembers, {});
  ```

## Clerk authentication

- Clerk handles user authentication in the frontend. The app uses
  `ClerkProvider` in `app/layout.js` and `ConvexProviderWithClerk` in
  `components/convex-client-provider.jsx` to integrate Clerk with Convex client.
- Convex validates JWTs using the OIDC issuer configured in
  `convex/auth.config.js` (see file). Ensure the issuer environment variable is
  set for the Convex runtime.

## Deployment

- Deploy Next.js using your preferred provider (Vercel, Netlify, etc.). Ensure
  environment variables are set in the hosting environment.
- For Convex Cloud, set the `CLERK_JWT_ISSUER_DOMAIN` in the Convex project
  settings so Convex functions can validate Clerk tokens.

## Troubleshooting (common errors)

- Error:
  `Failed to authenticate: "No auth provider found matching the given token (no providers configured)."`
  - Cause: Convex could not find any configured auth providers because the
    issuer env var was not available at runtime.
  - Fix: Make sure `CLERK_JWT_ISSUER_DOMAIN` (or the name you use) is set in the
    environment used by the Convex runtime (the shell running `npx convex dev`
    or the Convex Cloud environment variables) and restart Convex.

- Error: `ctx.runQuery is not a function`
  - Cause: Convex `query` handlers executed inside Next.js server runtime
    (instead of running inside Convex). `ctx.runQuery` exists only in Convex
    function runtime.
  - Fix: Move Convex function definitions to the `convex/` directory, and call
    them remotely from Next using the Convex client.

- Error:
  `ArgumentValidationError: Found ID <id> from table 'users', which does not match the table name in validator v.id("groups")`
  - Cause: A user id was passed as a `groupId` argument validated as
    `v.id('groups')`.
  - Fix: Pass the correct id type (ensure the argument type matches
    `v.id('<table>')`) or call the function without the mismatched id.

## Testing

- Unit tests: none included by default. If you add tests, include them under
  `__tests__` and add scripts to `package.json`.

## Contributing

- Use feature branches and open PRs against `main`.
- Keep Convex functions inside the `convex/` folder. Use the generated bindings
  under `convex/_generated/` to reference functions and values.

## Contact

If you need help with deployment or auth configuration, provide the environment
(local/dev/convex cloud) and any error logs and I can help troubleshoot further.

---

If you want this README translated to Bengali or tailored to internal company
standards (branding, templates), tell me which sections to emphasize and I will
update it. This is a [Next.js](https://nextjs.org) project bootstrapped with
[`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the
result.

You can start editing the page by modifying `app/page.js`. The page auto-updates
as you edit the file.

This project uses
[`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)
to automatically optimize and load [Geist](https://vercel.com/font), a new font
family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js
  features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out
[the Next.js GitHub repository](https://github.com/vercel/next.js) - your
feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the
[Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme)
from the creators of Next.js.

Check out our
[Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying)
for more details.
