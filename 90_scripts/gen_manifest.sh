#!/usr/bin/env bash
set -euo pipefail
out="VCAT_Evidence_Integrity_Manifest.csv"
echo "path,sha256,bytes,date_modified" > "$out"
while IFS= read -r -d '' f; do
  h=$(sha256sum "$f" | awk '{print $1}')
  b=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f")
  d=$(stat -c%y "$f" 2>/dev/null || stat -f%Sm "$f")
  echo "$f,$h,$b,$d" >> "$out"
done < <(find VCAT_SUBMISSION_PACKAGE VCAT_NON_GMAIL_EVIDENCE -type f -name '*.pdf' -print0 | sort -z)
echo "Manifest written to $out"