import os
import sys

import List

def remove(pkgName):
    pkgListing = List.findPkg(pkgName)
    if pkgListing == None:
        sys.exit("[Remove] Cannot remove package that is not installed: '" + pkgName + "'")
    
    filesToBeRemoved = pkgListing.fakeRootMap.files
    dirsToBeRemoved = pkgListing.fakeRootMap.dirs


    for i in filesToBeRemoved:
        try:
            print("[Remove] Removing file: " + i)
            os.remove(i)
        except:
            handleFailedRemoval(i)
        
    for i in dirsToBeRemoved:
        try:
            print("[Remove] Removing directory: " + i)
            os.rmdir(i)
        except:
            handleFailedRemoval(i)

    List.removeListingOn(pkgName)

def handleFailedRemoval(itemName):
    print("[Remove] Could not delete file '" + itemName + "'")
    shouldContinue = input("\tShould removal process continue? [y/N] ")

    if shouldContinue != "y" and shouldContinue != "Y":
        os.exit(1)
