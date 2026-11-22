#!/bin/bash
# Make an isolated working copy of this kit for one coder, so coders share no files.
#
#   scripts/make_agent_copy.sh <coder-name> <parent folder>
#
# Creates <parent>/facets-r2-kit-<coder-name>/ with everything a coder needs and nothing from other coders
# (no hand-ins/), plus an empty hand-in folder inside it: my-hand-in/facets-r2-<coder-name>-<YYYYMMDD>/.
# Put the parent OUTSIDE the project folder that holds this kit, so an agent in its copy can't browse earlier
# codes or other coders' work.
set -euo pipefail
name="${1:?coder name, for example sonnet-5-5 or ta1}"
parent="${2:?parent folder for the copy}"
case "$name" in *[!a-z0-9.-]*) echo "use lowercase letters, digits, dots and hyphens in the coder name" >&2; exit 2;; esac
kit="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$parent"
parent="$(cd "$parent" && pwd)"
project="$(dirname "$kit")"
case "$parent/" in "$project"/*) echo "warning: $parent is inside $project; an agent there could reach earlier codes" >&2;; esac
dest="$parent/facets-r2-kit-$name"
[ -e "$dest" ] && { echo "$dest already exists" >&2; exit 1; }
mkdir -p "$dest"
for f in README.md INSTRUCTIONS.md CODER-GUIDE.md DATA-NOTICES.md LICENSE postings.tsv prompts schema scripts handout-private; do
  cp -R "$kit/$f" "$dest/"
done
rm -rf "$dest/scripts/__pycache__"
handin="$dest/my-hand-in/facets-r2-$name-$(date +%Y%m%d)"
mkdir -p "$handin/replies"
echo "copy: $dest"
echo "hand-in folder: $handin"
