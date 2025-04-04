links = [
    "www.boo1.io",
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.com"
]

## Wrong Way, Will remove matching w letter also

for link in links:
    print(link.lstrip("www."))

## Correct Way

for link in links:
    print(link.removeprefix("www."))
