# ************************************************************
#                   Url Shortening Tool
#                 Project By : MAMATA SHEE
# ************************************************************




import pyshorteners

url=input("Enter the url : ")
shortner=pyshorteners.Shortener()
u=shortner.tinyurl.short(url)
print(u)





# --------------------------------------------------------
# --> For this we need to install a module 'pyshorteners'
# --> Use the below command to install this
# --> 'pip install pyshorteners'
# --------------------------------------------------------