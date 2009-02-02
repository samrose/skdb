#writes out a pretty html table with categories side by side
version = 1.0
import time
import yaml

f = open('comparison.yaml')
a = yaml.load(f)

#find the superset
categories = []
labs = [lab for lab in a]
for lab in labs:
  categories += lab['inventory'].keys()
categories = [i for i in set(categories)]
categories.sort()

print '<table valign="top" padding="10px">'
print '<thead>'
for lab in labs:
  print '<td>'
  print '<h2><a href="' + lab['link'] + '">'
  print '<img src="' + lab['logo'] + '" alt="' + lab['name'] + '"></a></h2>'
print '</thead>'

for category in categories:
  print '<tr>'
  for lab in labs:
    inv = lab['inventory']
    print '<td>'
    print '<b>' + category + ': </b><br>'
    if inv.__contains__(category) and inv[category]:
      for item in inv[category]:
        print '&nbsp;', item, '<br>'
    print '</td>'
  print '</tr>'
print '</table><br>'

print 'table generated by:'
print '<a href="http://fennetic.net/git/gitweb.cgi?p=skdb.git;a=tree;f=inventory">'
print 'skdb inventory comparison engine v', version, '</a><br>'
print 'on ', time.asctime(time.localtime(time.time())), time.time()
