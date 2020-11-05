import re
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup


def task1(h):
    python_count = h.count("Python")
    cpp_count = h.count("C++")
    print("Python" if python_count > cpp_count else "C++")


def task2(h):
    r = re.compile("<code>(\\w+)</code>")
    most_common = Counter(r.findall(h)).most_common()
    max_count = max(most_common, key=lambda x: x[1])[1]
    print(sorted(filter(lambda x: x[1] == max_count, most_common)))


def task3(h):
    soup = BeautifulSoup(h, "html.parser")
    cnt = 0
    for tr in soup.find_all("tr"):
        cnt += 1
        cnt *= 2 ** len(tr.find_all(["td", "th"]))
    print(cnt)


def task456(h):
    soup = BeautifulSoup(h, "html.parser")
    s = 0
    for tag in soup.find_all("td"):
        s += int(tag.string)
    print(s)


if __name__ == '__main__':
    html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode("utf-8")
    task2(html)
