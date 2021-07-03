# Clean history
git filter-branch --index-filter 'git rm --cached --ignore-unmatch \*.mp4' -- --all
rm -Rf .git/refs/original
rm -Rf .git/logs/
git gc --aggressive --prune=now

git rev-list --objects --all | grep -f <(git verify-pack -v .git/objects/pack/\*.idx| sort -k 3 -n | cut -f 1 -d " " | tail -10)


# Delete remote unused or unpresent branches
git fetch -p && git branch -vv | awk '/: gone]/{print $1}' | xargs git branch -d