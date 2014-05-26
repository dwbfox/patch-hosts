import urllib2
import shutil
import os

hosts_dir = 'C:\\Windows\\System32\\drivers\\etc\\'
hosts_download = 'http://winhelp2002.mvps.org/hosts.txt'



print 'Download updated hosts file...'
with open('hosts.data', 'w') as hfile:
    hfile.write(urllib2.urlopen(hosts_download).read())

try:
    print 'Making a backup of existing hosts file...'
    shutil.move(hosts_dir + 'hosts', hosts_dir + 'hosts.bak')

    print 'Copying over updated hosts file...'
    shutil.move('hosts.data', hosts_dir + 'hosts')
except IOError as e:
    print 'An error occured while patching hosts file. Make sure this script is running as root!'