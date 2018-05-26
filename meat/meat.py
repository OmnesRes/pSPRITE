import sys
sys.path.append("..")

from pSPRITE import SPRITE


##women restrictions
##int(.525*602)=316
##int(.515*602)=310

####try to find the min SD possible for women
##restrictions=[4]*310
########success
##
##for i in range(100):
##    print SPRITE(2.8,1,1.25,2,602,1,4,restrictions=restrictions)


#####try to find the max SD possible for women
##restrictions=[5]*125+[4]*(316-125)
#####success
##for i in range(100):
##    print SPRITE(2.8,1,1.73,2,602,1,5,restrictions=restrictions)
##
##


