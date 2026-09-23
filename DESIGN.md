---
version: beta
colors:
  header: "#292929"
  panel: "#404040"
  action: "#f29a2e"
  notice: "#f6bf26"
  text: "#ffffff"
typography:
  display:
    fontFamily: "Montserrat, Arial, sans-serif"
  body:
    fontFamily: "Open Sans, Arial, sans-serif"
rounded:
  legacyPanel: "34px"
  input: "6px"
omitted:
  - section: spacing
    reason: "Legacy Nicepage styles own the original section geometry; demo.css adds only responsive workflow layout."
---

## Overview

The public site is a working, safety-adapted demonstration of the original 2022 Troop 55 website—not a replacement visual concept. The original Nicepage-generated homepage, outdoor photography, dark header and footer, orange actions, trip signup card, simple login, and roster structure remain the visual and interaction source of truth.

## Durable decisions

- A yellow notice above every page clearly separates the public demo from an operating troop service.
- The original Flask → Replit database → organizer roster flow is reproduced with browser-local storage so no visitor information reaches a server.
- Demo credentials are visible and explicitly described as non-production authentication.
- The calendar is an archived visual preview rather than a connection to an operational troop calendar.
- Roster tables contain fictional names, example.com addresses, and 555 phone numbers only.
- The main content remains readable without JavaScript; JavaScript adds local form persistence, demo authentication, menu behavior, and reset controls.

## Accessibility and responsive behavior

Native form controls, table headings, landmarks, visible keyboard focus, live status messages, and a skip link are required. Mobile pages use one-column forms and horizontally scrollable roster tables. Reduced-motion preferences disable animation and fixed-background effects.

## Do's and don'ts

- Preserve the historical interface and explain adaptations plainly.
- Keep all demo data local and fictional.
- Maintain a complete keyboard path through RSVP, login, roster, and reset.
- Do not imply the old Flask service, calendar, authentication, or troop inbox is active.
