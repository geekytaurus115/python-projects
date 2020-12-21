# ************************************************************
#                 url-extraction (page source)
#                 Project By : MAMATA SHEE
# ************************************************************




from urllib.request import urlopen

page=urlopen("https://google.com")
sourceCode=page.read()
print(sourceCode)


# --------------------------------------------------------
# --> We don't need to  install any package for this
# --> urllib is in-built in our local
# ---------------------------------------------------------
