#!/bin/bash
# Markdown versions of the guidelines for readable diffs: tools/docx2md.sh [dir ...] (default: guidelines guidelines/proposals)
# The .docx stays the source; the .md is regenerated after every change of the .docx and committed with it.
# Tracked changes are shown accepted (the .md shows the text as proposed); images go to media/<file name>/.
set -e
cd "$(dirname "$0")/.."
dirs=("$@"); [ ${#dirs[@]} -eq 0 ] && dirs=(guidelines guidelines/proposals)
for d in "${dirs[@]}"; do
  [ -d "$d" ] || continue
  ( cd "$d"
    rm -rf media; rm -f -- *.md
    for f in *.docx; do
      [ -e "$f" ] || continue
      stem="${f%.docx}"
      { echo "<!-- Generated from \"$f\" by tools/docx2md.sh – do not edit, edit the .docx -->"; echo
        pandoc "$f" -f docx -t gfm --wrap=none --track-changes=accept --extract-media="media/$stem"; } > "$stem.md"
      # flatten media path, drop automatic alt texts
      sed -i -E 's#(\]\(media/[^)]*)/media/#\1/#g; s#!\[[^]]*\]\(#![](#g' "$stem.md"
      if [ -d "media/$stem/media" ]; then mv "media/$stem/media/"* "media/$stem/"; rmdir "media/$stem/media"; fi
    done )
done
