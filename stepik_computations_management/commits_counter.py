import github
import sys
import datetime as dt

g = github.Github()
since = dt.datetime(2016, 1, 1, 0, 0)
until = dt.datetime(2016, 12, 31, 23, 59)
s = 0
for line in sys.stdin.readlines():
    repo = g.get_repo(line.rstrip()[19:])
    try:
        s += repo.get_commits(sha='master', since=since, until=until).totalCount
    except github.GithubException:
        pass
print(s)
    
