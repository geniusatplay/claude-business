# Claude Business — operating rules

This repo is the work archive for Randy's AI-run businesses. Live dashboard: Empire HQ (https://claude.ai/artifact/Coyc2hTUDkShdMvqEMQ5r2).

## Models per role
- CEO session: set by the session.
- Managers / desk leads, Research Lab researchers, Reviewer Lab reviewers: Opus 5.5, medium effort (`.claude/agents/manager.md`, `researcher.md`, `reviewer.md`).
- Employees and studio helpers: Opus 5.5, low effort (`.claude/agents/worker.md`).

## Rules
- Startup cost cap: $50 per business, lower preferred. No spending or sign-ups by agents; Randy does those.
- Reviews: panels of 3; accept at 95+, revise 85–94 (max 5 rounds), re-assess under 85.
- No gambling, no deception, respect every platform's terms. Prediction markets: CFTC-regulated venues, non-sports only, demo first.
- Every agent appends to its own log.md (UTC timestamps); lessons go in playbook.md; reviews in reviews.md.
- Secrets live only in `.secrets/.env` on the 4090 PC, never in this repo or in chat.
