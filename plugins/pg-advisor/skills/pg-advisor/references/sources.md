# Finding and checking sources

All paths here are relative to the pg-advisor skill's own folder (its base directory). The advisor ships summaries and links, not Graham's essay text; essay text is read from paulgraham.com and cached on the user's machine.

## What ships with the advisor

- **`references/knowledge/index.md`**: every essay, newest first, with year, title linked to paulgraham.com, slug, and main concept.
- **`references/knowledge/atlas-data.json`**: for each essay, `slug`, `title`, `year`, `url`, `thesis`, `summary`, `key_ideas`, `coined_terms`, and `primary`/`secondary` concepts, all paraphrased. Use it to find candidate essays fast, e.g.:

  ```bash
  python3 -I -c "import json,sys;[print(e['year'],e['slug'],e['title']) for e in json.load(open(sys.argv[1]))['essays'] if 'fundraising' in [e['primary']]+e['secondary']]" references/knowledge/atlas-data.json
  ```

- **`references/knowledge/claims.json`**: 1,215 paraphrased claims, each tagged with the assumption id (P1–P22) it rests on. Useful when you need every claim that depends on, say, P2.

## Reading an essay

Use the bundled script. It reads from the user's cache and otherwise fetches from paulgraham.com and caches the result:

```bash
python3 -I scripts/essays.py find aord "default alive"   # lines containing a phrase
python3 -I scripts/essays.py get aord                      # the whole essay
python3 -I scripts/essays.py search "increasingly irrelevant" # every essay; downloads them all the first time (a few minutes)
```

If the script can't reach the web, use your own web-fetch tool on the essay's URL from the index. If neither works, cite from the summary and tell the founder the citation wasn't checked against the essay.

## Before citing

Summaries can drift from the essay. Before you attribute a specific point or number to Graham, confirm it in the essay text with `find`. Cite as: essay title (year). Paraphrase. Short coined phrases ("default alive", "schlep blindness") can be quoted; sentences cannot.
