---
version: alpha
colors:
  primary: "#e1ae52"
  forest: "#10251c"
  forest-deep: "#091710"
  moss: "#687967"
  paper: "#f3efe3"
  paper-muted: "#d9d7ca"
  amber: "#e1ae52"
typography:
  display:
    fontFamily: "Georgia, 'Times New Roman', serif"
  sans:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
rounded:
  control: "0px"
omitted:
  - section: spacing
    reason: "Responsive spacing is owned by archive.css through clamp values and the --page token."
  - section: components
    reason: "This is a single static archive page; shared components are represented by semantic CSS classes."
---

## Overview

The public BSA2 page is a historical project exhibit, not a reactivation of the troop website. It should feel like a field notebook translated into a restrained digital archive: wooded photography, paper forms, and precise roster labels. The signature is the static RSVP card that explains the former workflow without presenting a false live form.

## Colors

`archive.css` is the runtime owner for the tokens above. Forest colors establish the outdoor context; paper is reserved for the RSVP artifact; amber marks links, labels, and focus. The palette must remain readable and must not imitate current Boy Scouts of America branding.

## Typography

Georgia supplies the archival, editorial display voice. Helvetica Neue and system fallbacks carry navigation, labels, and body copy. Uppercase text is reserved for compact metadata and actions.

## Layout

The page moves from project context to workflow to implementation evidence. Desktop uses offset two-column compositions; below 800px every section becomes a single reading column. Content uses natural height and remains complete without JavaScript.

## Elevation & Depth

Depth is limited to the paper RSVP artifact and the offset frame around the original landscape image. Other surfaces remain flat and separated by hairline rules.

## Shapes

The archive uses square corners to evoke printed rosters and forms. The only circular shapes are status and selection marks.

## Components

Links remain native anchors with visible focus. The illustrated RSVP card contains no inputs or buttons because the service is archived and must not imply that information can still be submitted.

## Do's and Don'ts

- State clearly that the project is archived and no form is active.
- Keep the original project history separate from present-day production claims.
- Preserve keyboard focus, reduced-motion behavior, and readable mobile layouts.
- Do not publish troop member information, operational calendars, or functional-looking data-entry controls.
