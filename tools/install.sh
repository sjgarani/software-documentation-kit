#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: bash tools/install.sh /path/to/project" >&2
  exit 2
fi

kit_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target_dir="$(mkdir -p "$1" && cd "$1" && pwd)"
docs_dir="$target_dir/docs"
mkdir -p "$docs_dir"

for item in README.md adr specs runbooks guides; do
  cp -R "$kit_dir/$item" "$docs_dir/"
done
mkdir -p "$docs_dir/tools"
cp "$kit_dir/tools/docflow.py" "$docs_dir/tools/"

mkdir -p "$target_dir/.agents/skills"
cp -R "$kit_dir/tools/skills/documentation-workflow" "$target_dir/.agents/skills/"

instructions_file="$kit_dir/tools/agent-instructions.md"
agents_file="$target_dir/AGENTS.md"
begin_marker="<!-- software-documentation-kit:begin -->"
end_marker="<!-- software-documentation-kit:end -->"
block="$(cat "$instructions_file")"

if [[ -f "$agents_file" ]]; then
  current="$(cat "$agents_file")"
else
  current=""
fi

if [[ "$current" == *"$begin_marker"* && "$current" == *"$end_marker"* ]]; then
  before="${current%%"$begin_marker"*}"
  remainder="${current#*"$begin_marker"}"
  after="${remainder#*"$end_marker"}"
  current="${before}${begin_marker}
${block}
${end_marker}${after}"
else
  if [[ -n "$current" && "$current" != *$'\n' ]]; then
    current+=$'\n'
  fi
  current+="${begin_marker}
${block}
${end_marker}
"
fi

printf '%s' "$current" > "$agents_file"
echo "Kit installed in $docs_dir; agent instructions added to $agents_file."
