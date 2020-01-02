#!/usr/local/bon/python2

import xml.etree.cElementTree as et

#----------------------------------------------------------------------
def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """

    job_ids = ['7517210','7442066','00010001']
    tree = None
    tree = et.ElementTree(file=xml_file)
    print tree.getroot()
    root = tree.getroot()
    print "tag=%s, attrib=%s, text=%s" % (root.tag, root.attrib, root.text)
    """
    for job in tree.iter():
          id = job.find('JB_job_number')
          if job.tag == 'JB_job_number':
              print "%s = %s" % (job.tag, job.text)

    for job in tree.iter():
        #print "%s - %s" % (job.tag, job.text)
    """
    for job in tree.findall('./*/'):
        #print job.tag
        id = job.find('JB_job_number').text
        if id in job_ids:
            state = job.find('state').text
            print "%s === %s" % (id, state)

#----------------------------------------------------------------------
if __name__ == "__main__":
    parseXML("jobs3.xml")
