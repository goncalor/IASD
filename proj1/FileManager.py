__author__ = 'Henrique'

import string

class FileManager:

    client_file=''
    map_file=''
    clientNumber=0
    requestNumber=0



    def __init__(self, client_file, map_file):
        self.client_file= open(client_file, 'r')
        self.map_file= open(map_file, 'r')

    def parseFiles(self):
        parseClient()
        parseMap()

    def parseClient(self):

        #first parse the first line
        buf= self.client_file.readline();
        buf= buf.rstrip()
        buf= buf.split(' ')
        clientNumber= int(buf[0])
        requestNumber= int(buf[1])

        #now parse the rest of the file
        for line in self.client_file:
            #remove the end of line
            buf= line.rstrip()
            buf= buf.split(' ')



    def parseMap(self):





manager = FileManager()


