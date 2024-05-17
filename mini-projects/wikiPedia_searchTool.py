# ****************************************************
#               Wikipedia Search Tool
#              Project by : MAMATA SHEE
#
# ****************************************************


#--------------------------------------------------------
# --> For this we need to install the package named 'wikipedia'
# --> Use the below command to install this package
# --> 'pip install wikipedia'
#
# --> After installing this package import 'wikipedia' in your code
# --> Then search whatever you like from wikipedia
# --> You can use 'summary' to get the summary of the query
# ----------------------------------------------------------


import wikipedia
query=wikipedia.page("python programming")
print(query.summary)