# ************************************************************
#                 url-extraction (headers)
#                 Project By : MAMATA SHEE
# ************************************************************




from urllib.request import urlopen

page=urlopen("https://google.com")
print(page.headers)


# --------------------------------------------------------
# --> We don't need to  install any package for this
# --> urllib is in-built in our local
# ---------------------------------------------------------
