# BSA2 public demo UX contract

## Primary path

Home → Next Trip RSVP → confirmation at demo login → organizer roster → add another response or reset.

## State and data

- RSVP records use `localStorage` under `bsa2-demo-rsvps-v1`.
- The demo login uses `sessionStorage` under `bsa2-demo-admin-v1`.
- First visit and reset show two explicitly fictional sample records.
- No form data, credentials, analytics, or calendar requests are sent to a backend.

## Feedback and recovery

- Invalid forms retain entered values and identify the need to complete fields.
- A successful RSVP announces that it was saved locally before moving to login.
- Incorrect demo credentials produce an inline error.
- Reset requires a second explicit action and can be cancelled.
- Direct roster access without the demo session returns to login.

## Keyboard and small screens

All actions use native links, buttons, inputs, and radio controls. Focus is visible. A skip link bypasses repeated navigation. The mobile menu reports expanded state. Tables scroll within their own container rather than widening the page.

## No-JavaScript baseline

All explanatory pages and navigation remain readable. The roster HTML includes fictional samples and a notice explaining that interactive persistence requires JavaScript. The historical workflow is never mistaken for a live server form.
