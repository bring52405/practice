#!/usr/local/bon/python2

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et
job_ids = ['7517210','7442066','00010001']
tree = None
with open('jobs3.xml', 'r') as f:
   xml = f.read() # Read whole file in the file_content string
   #print xml.strip().splitlines()
   for line in xml.strip().splitlines():

    try:
      tree = et.fromstring(xml.strip())
      #print line.strip()
      assert tree.tag == 'job_info'
    except Exception:
      tree = None
   for job in tree.findall('./*/'):
       #print job.tag
       id = job.find('JB_job_number').text
       if id in job_ids:
           state = job.find('state').text
           print "%s === %s" % (id, state)
if tree is None:
    print tree.tag
    print 'Dookie'
else:
    print tree.tag
    print 'Success'
