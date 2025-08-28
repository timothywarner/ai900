# Repository Guidelines

## Project Structure & Module Organization
- `demos/`: Primary learning content organized by AI‑900 domains (e.g., `01-ai-overview`, `02-machine-learning`, `03-computer-vision`, `04-nlp`, `05-generative-ai`). See `docs/repo-organization.md` for details.
- `apps/`: Small runnable samples (Node.js bots, Computer Vision quickstart, REST samples). Examples: `azure_bots/my-chat-bot`, `compvision-js-sdk`, `analyze-image-node-rest`.
- `docs/`, `lessons/`, `exam-metadata/`: Course docs and lesson materials.
- Assets and datasets: `images/`, `Audio-Video/`, `CSV/`, `OCR/`, `People/`, `Places/`, `Things/` (tracked via Git LFS, see `.gitattributes`).

## Build, Test, and Development Commands
- Git LFS: `git lfs install` then clone; large files are LFS‑tracked.
- Node samples (example – Computer Vision):
  - `cd apps/compvision-js-sdk && npm install`
  - Configure keys (see Security below), then `node ComputerVisionQuickstart.js`
- Bot sample:
  - `cd apps/azure_bots/my-chat-bot && npm install`
  - Run: `npm start`; Dev: `npm run watch`; Lint: `npm run lint`
- REST sample: `cd apps/analyze-image-node-rest && node analyze-image.js` (replace hardcoded key/endpoint or use env vars).
- Tests: Most samples have placeholder `npm test`; add focused smoke tests as needed.

## Coding Style & Naming Conventions
- Demos: keep folder naming `NN-topic` (e.g., `03-computer-vision`). Use lowercase kebab‑case for files/folders.
- Markdown: H1 for titles, H2 for sections, fenced code blocks with language.
- Node (bot): ESLint Standard with tweaks (`.eslintrc.js`): 4‑space indent, semicolons, no space before function paren. Run `npm run lint`.

## Testing Guidelines
- Framework: none enforced. Prefer lightweight smoke tests and runnable examples.
- Naming: colocate with sample (e.g., `example.test.js`).
- Goal: keep demos fast, deterministic, and free of external secrets.

## Commit & Pull Request Guidelines
- Commits: present‑tense imperative (“Add CV quickstart”, “Fix README”) and reference issues when applicable.
- PRs: follow `.github/PULL_REQUEST_TEMPLATE.md` (type, behavior change, breaking change, screenshots for docs/UI). Target `main` and keep scope focused.

## Security & Configuration Tips (Important)
- Never commit secrets. Prefer `.env` + `dotenv` in samples (`COGNITIVE_ENDPOINT`, `COGNITIVE_KEY`, etc.). Example: `cp .env.example .env` then update values (create if missing).
- Replace any hardcoded keys in `apps/analyze-image-node-rest/analyze-image.js` before running. Consider reading from `process.env`.
- Keep large media under Git LFS; avoid adding binaries outside patterns in `.gitattributes`.

## Env Usage Examples
- Computer Vision quickstart:
  - `cd apps/compvision-js-sdk && cp .env.example .env`
  - Set `COMPUTER_VISION_ENDPOINT` and `COMPUTER_VISION_SUBSCRIPTION_KEY`
  - Run: `node ComputerVisionQuickstart.js`
- REST analyze image:
  - `cd apps/analyze-image-node-rest && cp .env.example .env`
  - Set `COGNITIVE_ENDPOINT` and `COGNITIVE_KEY`
  - Run: `node analyze-image.js`
- Bot (local dev):
  - `cd apps/azure_bots/my-chat-bot && cp .env.example .env`
  - Optionally set `MicrosoftAppId`/`MicrosoftAppPassword` for cloud channels; Emulator works without
  - Run: `npm start` (visit `http://localhost:3978` with Bot Framework Emulator)

## Quick Start Checklist
- Clone with LFS: `git lfs install` then `git clone <repo>`.
- 1) CV SDK sample: set `.env`, `npm install`, run. Expect console lines like: `This may be ... (0.xx confidence)`.
- 2) REST sample: set `.env`, `npm init -y && npm install request dotenv`, run. Expect pretty‑printed JSON response.
- 3) Bot: set `.env`, `npm install`, `npm start`. Expect Restify server log with localhost URL; echo replies in Emulator.
- Missing deps behavior: samples print clear install hints instead of stack traces.
