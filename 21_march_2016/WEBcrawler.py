start_link = page.find('<a href =')
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote+1)
url = [start_quote+1:end_quote]
