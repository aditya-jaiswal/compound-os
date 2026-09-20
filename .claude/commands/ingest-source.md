# /ingest-source

Ingest one or more raw uploaded files into the OS and refresh the distilled context. The "ingest one artifact → update many systems" pattern. Run ALL steps; report a diff at the end.

For each uploaded file:

1. **Classify** → pick the target domain (product, competitive, customers, engineering, etc.) from its content.
2. **File the raw original** into `<domain>/sources/` with a clean, dated, kebab-case name. Never edit the raw.
3. **Distill** → create or update the domain's curated context doc(s) (e.g. `product/product-context/<x>.md`, `positioning.md`, `pricing.md`). For a large file, use a subagent to read it so it doesn't bloat context; the subagent returns the distilled markdown.
4. **Provenance** → every distilled doc starts with `> Source: <path to raw> · distilled <date>`. Each fact must be traceable to its source.
5. **Memory** → add durable facts to the domain `knowledge.md`; add forward-looking/unproven claims to `hypotheses.md` (with confirmation count 0).
6. **Conflict check** → if the new doc contradicts an existing rule or fact, DO NOT silently overwrite. Flag it: show the old vs new and ask me to resolve (context-rot guard).
7. **Register** → update the domain `INDEX.md` (and `feature-index.yaml` if the file is feature-specific).
8. **Shard if needed** → apply the auto-shard thresholds from root CLAUDE.md.
9. **Report a diff** → list raw files filed, distilled docs created/updated, new knowledge/hypotheses entries, and any conflicts to resolve.

Do not edit the root `CLAUDE.md`.
