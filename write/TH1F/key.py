from write.key import Key as SuperKey

class Key(SuperKey):

    def __init__(self, string, stringloc):
        self.string = string
        self.fVersion = 4
        self.fObjlen = 582 + len(self.string)
        self.fDatime = 1581978882
        self.fKeylen = 0
        self.fNbytes = self.fObjlen + self.fKeylen
        self.fCycle = 1
        self.fSeekKey = stringloc
        self.fSeekPdir = 100
        self.packer = ">ihiIhhii"
        self.fClassName = b'TH1F'
        self.fName = self.string
        self.fTitle = b'th1f title'
        SuperKey.__init__(self, self.packer, self.fNbytes, self.fVersion, self.fObjlen, self.fDatime, self.fKeylen, self.fCycle,
                     self.fSeekKey, self.fSeekPdir, self.fClassName, self.fName, self.fTitle)

