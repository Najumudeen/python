
links = [
    "www.b001.io",
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.com"
]

# for i in links:
#     print(i.lstrip("www.*")) # will remove www and .w and  it's not good idea
    
for link in links:
    print(link.removeprefix("www."))

for link in links:
    print(link.removesuffix(".com"))
