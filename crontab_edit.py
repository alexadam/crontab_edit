'''
Created on Apr 28, 2012

python script for editing crontab files

@author: Alexandru Adam
'''
import os

#returns crontab content as string
def getCrontabJobs():
    p = os.popen('crontab -l')
    content = p.read()
    p.close()
    return content

def getCrontabJobsAsList():
    content = getCrontabJobs()
    
    if len(content) == 0 or content == '\n':
        return []
    elif content[len(content) - 1] == '\n':
        content = content[0:(len(content) - 1)]
    
    return content.split('\n')

#return a list with all jobs containing the 'string'
def getCrontabContentContaining(string):
    if not isinstance(string, str):
        raise 'Error! Input must be a string!'
    
    result = []
    lines = getCrontabJobsAsList()
    
    for line in lines:
        if string in line:
            result.append(line)
    return result

#set crontab content from a string - a '\n' separated job list or a single job
def setCrontabContent(content):
    if not isinstance(content, str):
        raise 'Error! Input must be a string!'
    
    if len(content) == 0:
        content = '\n'
    elif not content[len(content) - 1] == '\n':
        content = content + '\n'
    
    f = open('crontab.txt', 'wb')
    f.write(content);
    f.flush()
    f.close()
    
    p = os.popen('crontab crontab.txt')
    output = p.read()
    p.close()
    
    os.remove('crontab.txt')
    print output
    
def setCrontabContentFromList(contentList):
    if not isinstance(contentList, list):
        raise 'Error! Input must be a list!'
    
    setCrontabContent('\n'.join(contentList))
    
def appendCrontab(job):
    if not isinstance(job, str):
        raise 'Error! Input must be a string!'
    
    content = getCrontabJobs()
    setCrontabContent(content + job) 
    
def appendCrontabList(jobList):
    if not isinstance(jobList, list):
        raise 'Error! Input must be a list!'
    
    content = getCrontabJobs()
    setCrontabContent(content + '\n'.join(jobList)) 
    
def removeJobsContaining(string):
    if not isinstance(string, str):
        raise 'Error! Input must be a string!'
    
    content = getCrontabJobsAsList()
    result = []
    
    for job in content:
        if not string in job:
            result.append(job)
            
    setCrontabContentFromList(result)

def clearCrontab():
    setCrontabContent('')
