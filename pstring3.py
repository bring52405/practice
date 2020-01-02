#!/usr/local/bon/python2
import re

#job_ids = ['8574473','8570136','00010001']

with open('jobs.txt', 'r') as f:
   status = f.read() # Read whole file in the file_content string
   #print xml.strip().splitlines()
   for line in status.strip().splitlines():
       if line.startswith("job-ID"):
           continue
       if line.startswith("-"):
           continue
       line_parts = re.compile("\s+").split(line)
       #print len(line_parts)
       #print (line_parts)
       #if len(line_parts) < 9:
            #continue
       id = line_parts[0]
       state = line_parts[1]

       print ('%s - %s') % (id, state)
       #if id in job_ids:
          #print ('%s - %s') % (id, state)
