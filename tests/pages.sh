#!/usr/bin/env bash

if ! git branch --format='%(refname:short)' | grep -q -m1 -x tests-pages; then
  echo "error: missing branch tests-pages"
  echo "hint:"
  echo "git fetch origin tests-pages:tests-pages"
  exit 1
fi

set -eux

cd "$(dirname "$0")/.."

git worktree add tests/pages tests-pages
