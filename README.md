# 🐾 GoodSama

> Making animal rescue faster, safer, and community-driven.

GoodSama is a location-aware mobile app that connects nearby animal welfare volunteers through trusted NGO networks — helping animals in distress without exposing anyone's personal contact details.

---

## What it does

When someone finds an injured animal, they file a report. GoodSama notifies only the people who are:

1. **Within the same neighbourhood radius** as the report
2. **Linked to the same NGO** as the person filing it

No broadcast noise. No exposed phone numbers. Just a direct, trusted alert to the right people nearby.

---

## The three personas

| Persona | Role |
|---|---|
| 🐕 **The Animal** | Street dogs, cats, and wildlife who need help — the reason the app exists |
| 💛 **The Good Samaritan** | Empathetic animal lovers who want to help but lack time, resources, or confidence |
| 🏡 **The NGO** | Welfare organisations with expertise, shelter, and the ability to coordinate response |

---

## Key design decisions

- **Privacy by design** — no personal contact details shared between users
- **Two-way NGO link** — both the user and NGO must accept the connection
- **Active/inactive state** — alerts only reach people physically positioned to help
- **One-on-one feel** — reduces diffusion of responsibility vs. broadcast group messages

---

## Brand

- **Palette:** Action Orange `#E8610A` · Deep Charcoal `#1A1A1A` · Warm Cream `#F0EDE8`
- **Type:** DM Serif Display (headlines) · DM Sans (UI)
- **Tone:** Urgent but warm. Direct. Community-rooted. Action-oriented.

See [`brand.md`](brand.md) for full guidelines.

---

## Files

| File | Status | Description |
|---|---|---|
| `index.html` | Built | Desktop landing page |
| `login.html` | Built | Mobile login — phone, OTP, role selection |
| `setup.html` | Next | Radius zone registration |
| `home.html` | Next | Dashboard |

---

## Build plan

4-week prototype (~28 hours total, 1 hr/day).

| Week | Focus |
|---|---|
| 1 | Auth & location — phone login, radius zone, active/inactive state |
| 2 | Report & notify — animal report form, notification + accept/decline flow |
| 3 | NGO linking — two-way link request, user profile, settings |
| 4 | Polish & test — visual refinement, user testing with 3–5 real people |

---

## MVP scope

~20 self-selected helpers in Dehradun, linked to one NGO. People already doing this work — the app makes them faster, safer, and more reachable.

---

*GoodSama · May 2026*
