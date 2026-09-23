# BSA2

BSA2 is a 2022 Flask project I initially built for my Boy Scout troop's website. It served as the troop's primary RSVP flow for trips: scouts and families submitted whether they were attending, and organizers reviewed separate going and not-going lists.

**Working project demo:** [ches.dev/BSA2](https://ches.dev/BSA2/)

## Try the original workflow

1. Open **Next Trip** and submit an RSVP using fictional details.
2. Use the public demo login (`demo` / `troop55`).
3. See the response in the organizer roster, add another response, or reset the samples.

The public demo preserves the original Nicepage-era frontend and recreates the original Flask/Replit data flow in browser-local storage. Nothing is sent to a server. The visible login is a walkthrough device, not real authentication.

## Original implementation

- Flask routes and server-rendered templates
- A trip-specific RSVP form
- Replit's key/value database for responses
- An organizer-facing roster grouped into going and not going
- A black, gray, and orange visual system over outdoor photography

## Historical context

The Flask source remains an early-project snapshot, not a maintained production service. It has limited validation, incomplete authentication, and dependencies tied to the former Replit environment. Do not deploy the historical server unchanged or use it to collect personal information.

The static public demo intentionally has no live troop calendar, real member data, server database, or production authentication.
