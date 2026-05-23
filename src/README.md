# 🐾 GoodSama

**Making animal rescue faster, safer, and community-driven.**

GoodSama is a location-aware mobile app that connects nearby animal welfare volunteers through trusted NGO networks — so when someone finds an animal in distress, the right people get notified instantly, without exposing anyone's personal contact details.

---

## What it does

When a Good Samaritan spots an injured or distressed animal, they file a report through GoodSama. The app then:

1. **Matches by location** — only volunteers registered within the same neighbourhood radius receive the alert
2. **Filters by trust network** — only users linked to the same NGO as the reporter are notified, replacing noisy WhatsApp broadcasts with a direct, personal ping
3. **Protects privacy** — no phone numbers or contact details are ever shared between users

The result is a closed, high-signal rescue network where alerts feel personal, responsibility doesn't diffuse, and helpers are always positioned to act.

---

## Who it's for

| Persona | Role |
|---|---|
| **Good Samaritans** | Animal lovers who want to help but lack resources, contacts, or confidence in the moment |
| **NGOs** | Animal welfare organisations who want a reliable, low-noise channel to mobilise their trusted volunteers |
| **Animals** | Street dogs, cats, and wildlife in distress — the reason the app exists |

The MVP targets roughly 20 self-selected helpers in Dehradun, all linked to one NGO — people already doing the work, who need a faster and safer way to coordinate.

---

## Running it locally

No build step or server needed — this is a static HTML project.

```bash
# Clone or download the project files
git clone <your-repo-url>
cd goodsama

# Open in browser
open index.html
```

Or just open `index.html` directly in any modern browser. All screens are self-contained HTML files that link to each other.

### File structure

```
goodsama/
├── index.html       # Landing page (desktop)
├── login.html       # Mobile login — phone number + OTP flow
├── setup.html       # Radius registration (coming next)
└── home.html        # Dashboard (coming next)
```

> **Fonts**: The UI uses Google Fonts (DM Sans + DM Serif Display). An internet connection is needed for these to load correctly. They degrade gracefully to system serif/sans-serif without one.

---

## What's coming next

The project is being built in four weekly sprints (~1 hour/day):

| Week | Focus | Status |
|---|---|---|
| 1 | Auth & Location — phone login, OTP, radius zone registration, active/inactive toggle | 🔄 In progress |
| 2 | Report & Notify — animal report form, notification screen, accept/decline flow | ⏳ Upcoming |
| 3 | NGO Linking — two-way link request and acceptance, profile screen, settings | ⏳ Upcoming |
| 4 | Polish & Test — visual refinement, realistic copy, user testing with 3–5 real people | ⏳ Upcoming |

The goal is a **clickable working prototype** by end of week 4 — not a production app, but something real people can test.

---

## Design principles

- **One-on-one, not broadcast** — alerts feel direct and personal, reducing diffusion of responsibility
- **Privacy by design** — personal contact details are never shared between users
- **Relevance over reach** — you only get notified if you're physically close enough to help
- **Closed network for trust** — the NGO link requirement keeps the network high-quality and accountable

---

*Built with care for the animals of Dehradun. 🐕*
