# ************************************************************
#                   Google Search Tool
#                 Project By : MAMATA SHEE
# ************************************************************




from googlesearch import search

query="Sumita Roy"
for i in search(query,start=0,pause=2):
    print(i)




# ----------------------------------------------------------
# --> For this we need to install a package named 'google'
# --> To install this package use the below command
# --> 'pip install google'
# ----------------------------------------------------------