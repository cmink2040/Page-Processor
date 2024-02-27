# Project
Page Word Processor is a web-based word processor with a very niche use case.

## Why?
As per new guidelines for my projects in 2024 all project must provide ample 
reason for existence.

This project's use case is for creating and managing any document that severely relies on paging.
This includes things such as

- Notes
- Book pages
- Blog post pages

What current software exist for such?

- OneNote
- Obsidian
- Word/Docs

Why not use one of the above instead of creating?

- Most do not think of each page as an individual document, and lack features for pages (e.g, word count per page)
- Peformance issues on those with individual pages. (not good for >300 pages)
- Propertiary Software that may require payment and have a very crappy extension API.

## Current Status
MVP state. Do not use in production unless in a private network with a firewall for local users such as family, friends, etc, whom you have a trustful relationship.

Very unsecure.

- Createusers endpoint can be spammed to flood database and prevent normal users
- Pages may be returned to people who don't own them by modifying front end (haven't confirmed, but this problem has appeareed in many of the APIs during testing).
- Bucket and page endpoints can be flooded to waste storage

Other problems

- GUI is not in any good shape.
- DELETE buttons are not implemented, nor is the DELETE API functional.
- Many skeletons in the API.
- Documententation of code subpar. 
- Code has many illogically structured APIs, and needs plenty of refactoring.

## Toolchain and framework
All new projects must have their toolchain and framework defined before the project starts.

If new tools need to be added during project, they must have a good reason.

- Python with FastAPI.
- Database with SQLite/PostgreSQL
- TinyMCE for frontend editing.
- HTMX (if needed), or a mightier frontend (React, Svelte)
