def ids():
  from robobrowser import RoboBrowser
  import urllib.request, urllib.parse, urllib.error
  from bs4 import BeautifulSoup
  import ssl

  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  fname = input('Arquivo: ')
  fhand = open(fname)

  d = {}

  for lines in fhand:
    ids = lines.split()
    for id in ids:
      if id == 'Apple':
        aux = ids[2]
      if id == 'Senha:':
        d[aux] = ids[1]
      continue

  browser = RoboBrowser()
  url = input('Site: ')
  browser.open(url)

  signup_form = browser.get_form(class_='')
  signup_form  

  signup_form['authenticity_token'].value 

  # Fill it out
  k = 0
  i = 0
  for i in d:
    signup_form['id'].value = i
    signup_form[''].value = d[k]
    # Submit the form
    browser.submit_form(signup_form)
    i += 1
  
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  
  #tags = soup('input')
  #for tag in tags:
    #print(tag.get('id', None))


ids()
