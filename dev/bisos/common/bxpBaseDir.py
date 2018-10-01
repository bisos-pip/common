# -*- coding: utf-8 -*-
"""\
*    *[Summary]* ::  A /library/ with ICM Cmnds to support ByStar bases creation facilities
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/bisos/common/dev/bisos/common/bxpBaseDir.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "bxpBaseDir"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805254923"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:icm:python:topControls 
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

"""
* 
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pythonWb.org"
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
####+END:
"""


####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import pwd
import grp
import os
import collections
import enum

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:

from bisos.platform import bxPlatformConfig
from bisos.platform import bxPlatformThis

import shutil
import copy

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bxpBaseDir_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /bxpBaseDir_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bxpBaseDir_libOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
*** bxpRootXxFile   -- /etc/bystarRoot, ~/.bystarRoot, /bystar
*** bxpRoot         -- Base For This Module
*** bpb             -- ByStar Platform Base, Location Of Relevant Parts (Bisos, blee, bsip
*** bpd             -- ByStar Platform Directory (Object), An instance of Class BxpBaseDir
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print each
            if interactive:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:


####+BEGIN: bx:dblock:python:section :title "Directory Base Locations"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Directory Base Locations*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:subSection :title "ByStar Root"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ByStar Root*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: bx:dblock:python:func :funcName "bxpRootBaseDirPtrSysFile_obtain" :comment "/etc/bystarRoot" :funcType "obtain" :retType "str" :argsList "" :deco "ucf.runOnceOnlyReturnFirstInvokation"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bxpRootBaseDirPtrSysFile_obtain/ =/etc/bystarRoot= retType=str argsList=nil deco=ucf.runOnceOnlyReturnFirstInvokation  [[elisp:(org-cycle)][| ]]
"""
@ucf.runOnceOnlyReturnFirstInvokation
def bxpRootBaseDirPtrSysFile_obtain():
####+END:
    return os.path.abspath(
        "/etc/bisosRoot"
    )


####+BEGIN: bx:dblock:python:func :funcName "bxpRootBaseDirPtrUserFile_obtain" :comment "~/.bystarRoot" :funcType "obtain" :retType "str" :argsList "" :deco "ucf.runOnceOnlyReturnFirstInvokation"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bxpRootBaseDirPtrUserFile_obtain/ =~/.bystarRoot= retType=str argsList=nil deco=ucf.runOnceOnlyReturnFirstInvokation  [[elisp:(org-cycle)][| ]]
"""
@ucf.runOnceOnlyReturnFirstInvokation
def bxpRootBaseDirPtrUserFile_obtain():
####+END:
    return os.path.abspath(
        os.path.expanduser(
            "~/.bisosRoot"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bxpRootBaseDirDefault_obtain" :comment "/bystar" :funcType "obtain" :retType "str" :argsList "" :deco "ucf.runOnceOnlyReturnFirstInvokation"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bxpRootBaseDirDefault_obtain/ =/bystar= retType=str argsList=nil deco=ucf.runOnceOnlyReturnFirstInvokation  [[elisp:(org-cycle)][| ]]
"""
@ucf.runOnceOnlyReturnFirstInvokation
def bxpRootBaseDirDefault_obtain():
####+END:
    return os.path.abspath(
        "/bisos"
    )


####+BEGIN: bx:dblock:python:subSection :title "BISOS Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BISOS Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bpbDist_baseObtain_bin" :comment "DIST BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbDist_baseObtain_bin/ =DIST BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbDist_baseObtain_bin(
    baseDir,
):
####+END:
    """
** /bystar/dist/pip/bisos/bin
"""
    bxpRoot = bxpRoot_baseObtain(baseDir)            

    return( os.path.join(
        bxpRoot, "dist/pip/bisos", "bin"
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbDist_baseObtain_input" :comment "DIST DATA" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbDist_baseObtain_input/ =DIST DATA= retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbDist_baseObtain_input(
    baseDir,
):
####+END:
    """
** /bystar/dist/pip/bisos/input
ICM packages and ICM Groups can keep their specific inputs, configuratios/etc. here.
"""
    bxpRoot = bxpRoot_baseObtain(baseDir)                

    return( os.path.join(
        bxpRoot, "dist/pip/bisos", "input"
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbBisos_baseObtain_root" :comment "BISOS BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisos_baseObtain_root/ =BISOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisos_baseObtain_root(
    baseDir,
):
####+END:
    bxpRoot = bxpRoot_baseObtain(baseDir)            

    return ( os.path.join(
        bxpRoot,
        # "bisos", Obsolted After introduction of bxPlatformConfig
    ))


####+BEGIN: bx:dblock:python:func :funcName "bpbBisos_baseObtain_bin" :comment "BISOS BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisos_baseObtain_bin/ =BISOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisos_baseObtain_bin(
    baseDir,
):
####+END:
    return ( os.path.join(
        bpbBisos_baseObtain_root(baseDir),
        "bin",
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbBisos_baseObtain_var" :comment "BISOS BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisos_baseObtain_var/ =BISOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisos_baseObtain_var(
    baseDir,
):
####+END:
    return( os.path.join(
        bpbBisos_baseObtain_root(baseDir),
        "var",
    ))


####+BEGIN: bx:dblock:python:func :funcName "bpbBisos_baseObtain_input" :comment "BISOS DATA" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisos_baseObtain_input/ =BISOS DATA= retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisos_baseObtain_input(
    baseDir,
):
####+END:
    bxpRoot = bxpRoot_baseObtain(baseDir)                

    return( os.path.join(
        bxpRoot, "bisos", "input"
    ))


####+BEGIN: bx:dblock:python:subSection :title "BISOS Pkg Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BISOS Pkg Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_var" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisosPkg_baseObtain_var/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_var(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_tmp" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisosPkg_baseObtain_tmp/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_tmp(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_log" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisosPkg_baseObtain_log/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_log(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))


####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_control" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisosPkg_baseObtain_control/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_control(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))



####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_input" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bpbBisosPkg_baseObtain_input/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_input(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))


####+BEGIN: bx:dblock:python:section :title "Common Arguments Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Arguments Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-ParSpec   :: /commonParamsSpecify/ retType= argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    icmParams.parDictAdd(
        parName='baseDir',
        parDescription="Bx Platform Base Dir",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--baseDir',
    )

    icmParams.parDictAdd(
        parName='pbdName',
        parDescription="Platform BaseDirs Dict Name",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--pbdName',
    )

        
####+BEGIN: bx:dblock:python:section :title "Common Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "examples_bxPlatformBaseDirsCommon" :comment "Base Roots Info And Preps" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-examples  :: /examples_bxPlatformBaseDirsCommon/ =Base Roots Info And Preps= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxPlatformBaseDirsCommon():
####+END:
    icm.cmndExampleMenuChapter('* =BxP BaseDir=  ByStar Platform Base Dirs')

    cmndName = "bxpRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "bxpRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['baseDir'] = '/tmp/bxBase'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    icm.ex_gExecMenuItem(execLine="""cat {}""".format(bxpRootBaseDirPtrUserFile_obtain()),)
    icm.ex_gExecMenuItem(execLine="""cat {}""".format(bxpRootBaseDirPtrSysFile_obtain()),)
    icm.ex_gExecMenuItem(execLine="""ls -l {}""".format(bxpRootBaseDirDefault_obtain(),)) 
    icm.ex_gExecMenuItem(execLine="""ls -l /bisos /de /bxo""")   
    icm.ex_gExecMenuItem(execLine="""sudo mkdir /bisos; sudo chown {}:{} /bisos"""
                         .format(bisosUserName_obtain(), bisosGroupName_obtain()))
    icm.ex_gExecMenuItem(execLine="""sudo mkdir /de; sudo chown {}:{} /de"""
                         .format(bisosUserName_obtain(), bisosGroupName_obtain()))
    icm.ex_gExecMenuItem(execLine="""sudo mkdir /bxo; sudo chown {}:{} /bxo"""
                         .format(bisosUserName_obtain(), bisosGroupName_obtain()))


####+BEGIN: bx:dblock:python:func :funcName "examples_bxPlatformBaseDirs" :comment "bx-bases.py module information" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-examples  :: /examples_bxPlatformBaseDirs/ =bx-bases.py module information= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxPlatformBaseDirs():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    #examples_bxPlatformBaseDirsCommon()

    icm.cmndExampleMenuChapter('* =BxP BaseDir=  Module Description,Usage,Status Information')
    
    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="bx-bases", verbosity='none')    


####+BEGIN: bx:dblock:python:func :funcName "examples_bxPlatformBaseDirsFull" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-examples  :: /examples_bxPlatformBaseDirsFull/ =Show/Verify/Update For relevant PBDs= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxPlatformBaseDirsFull():
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    #bxRootBase = bxpRoot_baseObtain(None)

    examples_bxPlatformBaseDirsCommon()
    
    icm.cmndExampleMenuChapter('* =Module=  Overview (desc, usage, status)')    
   
    cmndName = "overview_bxpBaseDir" ; cmndArgs = "moduleDescription moduleUsage moduleStatus" ;
    cps = collections.OrderedDict()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    icm.cmndExampleMenuChapter(' =BxP DirBases=  *pbdShow/pbdVerify/pbdUpdate Of Relevant PBDs*')    

    icm.cmndExampleMenuSection(' =BxP DirBases=  *pbdShow*')        
    cmndName = "pbdShow" ; cmndArgs = "/ dist" ;
    cps = collections.OrderedDict() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdShow" ; cmndArgs = "/ var tmp dist/pip " ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bisosRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bisosRoot'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'deRunRoot'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bxoRoot'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    icm.cmndExampleMenuSection(' =BxP DirBases=  *pbdVerify*')            
    
    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdVerify" ; cmndArgs = "/ var" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BISOS'; cps['pbdName'] = 'bisosRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos'; cps['pbdName'] = 'bisosRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/de'; cps['pbdName'] = 'deRunRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bxo'; cps['pbdName'] = 'bxoRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    icm.cmndExampleMenuSection(' =BxP DirBases=  *pbdUpdate*')
    
    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdUpdate" ; cmndArgs = "/ var" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BISOS'; cps['pbdName'] = 'bisosRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos'; cps['pbdName'] = 'bisosRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/de'; cps['pbdName'] = 'deRunRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bxo'; cps['pbdName'] = 'bxoRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    icm.cmndExampleMenuSection(' *bx-platformInfoManage.py -- Specifiy Platform Defaults*')

    execLineEx("""bx-platformInfoManage.py""")

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ;
    cps=cpsInit() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper=None, icmName="bx-platformInfoManage.py")

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /" ;
    cps=cpsInit() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                         comment='none', icmWrapper=None, icmName="bx-platformInfoManage.py")

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /tmp" ;
    cps=cpsInit() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                         comment='none', icmWrapper="echo", icmName="bx-platformInfoManage.py")
 
    icm.cmndExampleMenuSection(' =BxP DirBases Creation/Ownership=  *pbdRootsForPlatform*')   
    
    cmndName = "pbdRootsForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    cmndName = "pbdRootsForPlatform" ; cmndArgs = "bisosRoot" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    icm.cmndExampleMenuSection(' =BxP DirBases Update=  *pbdUpdateForPlatform*')   

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "bisosRoot" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")
    
    # pbdList has been OBSOLETED
    # icm.cmndExampleMenuChapter(' =BxP DirBases=  *pbdShow/pbdVerify/pbdUpdate*')    

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bystar" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BISOS'
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bystar" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] =  bxRootBase
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
####+BEGIN: bx:dblock:python:section :title "Misc To Be Sorted Out"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Misc To Be Sorted Out*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    
####+BEGIN: bx:dblock:python:func :funcName "bisosUserName_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-Obtain    :: /bisosUserName_obtain/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def bisosUserName_obtain():
####+END:
    """
** ByStar UserName.
"""
    bxPlatformConfigBase = bxPlatformThis.pkgBase_configDir()
    bisosUserName = bxPlatformConfig.bisosUserName_fpObtain(bxPlatformConfigBase)
    
    return bisosUserName


####+BEGIN: bx:dblock:python:func :funcName "bisosGroupName_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-Obtain    :: /bisosGroupName_obtain/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def bisosGroupName_obtain():
####+END:
    """
** ByStar GroupName
"""
    bxPlatformConfigBase = bxPlatformThis.pkgBase_configDir()
    bisosGroupName = bxPlatformConfig.bisosGroupName_fpObtain(bxPlatformConfigBase)
    
    return bisosGroupName


####+BEGIN: bx:dblock:python:section :title "Base Dirs Specifications ::"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Base Dirs Specifications ::*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:section :title " /===== PBD SPECIFICATION CMNDs =====/ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    * /===== PBD SPECIFICATION CMNDs =====/ *  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bisosRoot" :comment "pbd Dictionary" :funcType "Init" :retType "bxpRootBaseDirsDict" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-Init      :: /pbdDict_bisosRoot/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bisosRoot(
    baseDir,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bisosBasesInstall.tex
*** See: \section{/bisos Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    root = bxpRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpObjGet_baseDir(root, '')

    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        pbdDict[dstPathRel] = BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )
        
    directory('dist')
    directory('dist/pip')
    directory('dist/pip/bisos')
    directory('dist/pip/bisos/bin')
    directory('dist/pip/bisos/input')                
    directory('dist/pip/blee')
    directory('dist/pip/bsip')

    directory('venv')
    command(  'venv/py2-bisos-3',
              "virtualenv --no-site-packages --python=python2 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('venv/py2-bisos-3')))
    command(  'venv/dev-py2-bisos-3',
              "virtualenv --no-site-packages --python=python2 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('venv/dev-py2-bisos-3')))
    command(  'venv/py3-bisos-3',
              "virtualenv --no-site-packages --python=python3 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('venv/py3-bisos-3')))
    command(  'venv/dev-py3-bisos-3',
              "virtualenv --no-site-packages --python=python3 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('venv/dev-py3-bisos-3')))

    
    directory('vcAuth')
    directory('vcAuth/bisos')
    
    directory('vcAnon')
    directory('vcAnon/bisos')    

    directory('control')
    directory('control/bisos')    
    directory('control/bisos/site')    

    directory('var')
    directory('var/bisos')
    directory('var/bisos/icmsPkg')        
    
    
    directory('tmp')
    
    directory('log')
    directory('log/bisos')

    directory('core')
    symLink(  'core/bin', 'dist/pip/core/bin')
    symLink(  'core/input', 'dist/pip/core/input')
    symLink(  'core/var', 'var/core')
    symLink(  'core/tmp', 'tmp')
    symLink(  'core/log', 'log/core')                
              
    directory('bsip')
    
    directory('blee')

    return pbdDict


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_deRunRoot" :comment "pbd Dictionary" :funcType "Init" :retType "bxpRootBaseDirsDict" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-Init      :: /pbdDict_deRunRoot/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_deRunRoot(
    baseDir,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bisosBasesInstall.tex
*** See: \section{/de/run Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    root = bxpRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpObjGet_baseDir(root, '')

    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        pbdDict[dstPathRel] = BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )

    # Assuming /de/run as default
        
    directory('bisos')
    directory('bisos/r3')
    directory('bisos/r3/pkgs')
    directory('bisos/r3/pkgs/marmee')
    directory('bisos/r3/pkgs/marmee/control')
    directory('bisos/r3/pkgs/marmee/pkgInfo')
    directory('bisos/r3/pkgs/marmee/admin')            

    return pbdDict



####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxoRoot" :comment "pbd Dictionary" :funcType "Init" :retType "bxpRootBaseDirsDict" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-Init      :: /pbdDict_bxoRoot/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxoRoot(
    baseDir,
):
####+END:
    """
** BISOS Policy  baseDir="/bxo"
** In /lcnt/lgpc/bystar/permanent/common/clips/bisosBasesInstall.tex
*** See: \section{/de/bxo Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    root = bxpRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpObjGet_baseDir(root, '')

    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        pbdDict[dstPathRel] = BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )
        
    directory('r3')                          # BISOS Release 3 account Bases
    directory('r3/so')                       # Service Objects
    directory('r3/io')                       # Information Objects
    directory('r3/fso')                      # Foreign Service Objects
    directory('r3/fio')                      # Foreign Information Objects
    
    symLink(  'so', 'r3/so')                 # Canonical Symlink
    symLink(  'io', 'r3/io')                 # Canonical Symlink
    symLink(  'fso', 'r3/fso')                 # Canonical Symlink
    symLink(  'fio', 'r3/fio')                 # Canonical Symlink

    return pbdDict


####+BEGIN: bx:dblock:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bxpRoot_baseObtain" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-obtain    :: /bxpRoot_baseObtain/ retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bxpRoot_baseObtain(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return outcome.results

    
####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "bxpRootGet" :parsMand "" :parsOpt "baseDir" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /bxpRootGet/ parsMand= parsOpt=baseDir argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bxpRootGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        baseDir=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'baseDir': baseDir, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        baseDir = callParamsDict['baseDir']

####+END:
        retVal = None
        while True:           # Executes once only -- always breaks.
            if baseDir:
                retVal = baseDir
                break

            retVal = bxPlatformConfig.rootDir_bisos_fpObtain(None)
            break

            # The Rest Is Now Obsolete

            userFileName = bxpRootBaseDirPtrUserFile_obtain()
            if os.path.isfile(
                    userFileName
            ):
                with open(userFileName, 'r') as myfile:
                    data=myfile.read().replace('\n', '')
                    retVal = data
                    break

            sysFileName = bxpRootBaseDirPtrSysFile_obtain()
            if os.path.isfile(
                    sysFileName
            ):
                with open(sysFileName, 'r') as myfile:
                    data=myfile.read().replace('\n', '')
                    retVal = data
                    break

            # Default ByStar Root Directory
            defaultBxRootDir = bxpRootBaseDirDefault_obtain()
            if os.path.isdir(defaultBxRootDir):
                retVal = defaultBxRootDir
                break

            icm.EH_problem_usageError("Missing /bystar and no /etc/bystarRoot")            
            retVal = None
            break

        if interactive:
            icm.ANN_write("{}".format(retVal))

        return cmndOutcome.set(
            opError=icm.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Based ~/.bystarRoot or /etc/bystarRoot decide on meta.
   ** if --baseDir Was specified, it is returned or 
   ** If ~/.bystarRoot exists, its content is returned
   ** If /etc/bystarRoot exists, its content is returned
   ** If /bystar exists, "/bystar" is returned
"""


####+BEGIN: bx:dblock:python:subSection :title "ICM Each Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ICM Each Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
            
            
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdShow" :parsMand "" :parsOpt "baseDir pbdName" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pbdShow/ parsMand= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdShow(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        baseDir=None,         # or Cmnd-Input
        pbdName=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        baseDir = callParamsDict['baseDir']
        pbdName = callParamsDict['pbdName']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
	def cmndDesc(): """
** for each arg, output bxp parameters.
"""
        icm.ANN_write("{}".format(baseDir))

        if not pbdName:
            pbdName = 'bisosRoot'

        if baseDir:
            pbdDict = eval("""pbdDict_{}("{}")""".format(pbdName, baseDir))
        else:
            pbdDict = eval("""pbdDict_{}({})""".format(pbdName, baseDir))

        def procEach(pbdItem):
            pbdObj = pbdDict[pbdItem]
            pbdObj.show()

        if effectiveArgsList[0] == "all":
            for each in pbdDict:
                procEach(each)

            return cmndOutcome.set(
                opError=icm.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )
    
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdVerify" :parsMand "" :parsOpt "baseDir pbdName" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pbdVerify/ parsMand= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdVerify(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        baseDir=None,         # or Cmnd-Input
        pbdName=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        baseDir = callParamsDict['baseDir']
        pbdName = callParamsDict['pbdName']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
	def cmndDesc(): """
** for each arg, verify that each exists as expected.
"""
        icm.ANN_write("{}".format(baseDir))
                
        if not pbdName:
            pbdName = 'bisosRoot'

        if baseDir:
            pbdDict = eval("""pbdDict_{}("{}")""".format(pbdName, baseDir))
        else:
            pbdDict = eval("""pbdDict_{}({})""".format(pbdName, baseDir))

        def procEach(pbdItem):
            pbdObj = pbdDict[pbdItem]
            pbdObj.verify()

        if effectiveArgsList[0] == "all":
            for each in pbdDict:
                procEach(each)

            return cmndOutcome.set(
                opError=icm.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )
 
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdUpdate" :parsMand "" :parsOpt "baseDir pbdName" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pbdUpdate/ parsMand= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        baseDir=None,         # or Cmnd-Input
        pbdName=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        baseDir = callParamsDict['baseDir']
        pbdName = callParamsDict['pbdName']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        icm.ANN_here("baseDir={baseDir} -- pbdName={pbdName}".format(baseDir=baseDir, pbdName=pbdName))

        if not pbdName:
            #pbdName = 'bxpRoot'
            pbdName = 'bisosRoot'

        if baseDir:
            pbdDict = eval("""pbdDict_{}("{}")""".format(pbdName, baseDir))
        else:
            # Do Not Quote None in eval
            pbdDict = eval("""pbdDict_{}({})""".format(pbdName, baseDir))

        def procEach(pbdItem):
            pbdObj = pbdDict[pbdItem]
            #icm.ANN_here("pbdObj={pbdObj} -- pbdItem={pbdItem}".
            #             format(pbdObj=pbdObj, pbdItem=pbdItem))
            pbdObj.update()

        if effectiveArgsList[0] == "all":
            for each in pbdDict:
                procEach(each)

            return cmndOutcome.set(
                opError=icm.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** For each arg, update each to what has been specified.
"""


        
####+BEGIN: bx:dblock:python:subSection :title "ICM Multiple pbdUpdates Based On Platform Defaults Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ICM List Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdRootsForPlatform" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pbdRootsForPlatform/ parsMand= parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdRootsForPlatform(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        def withPbdNameGetRootForPlatform(pbdName):
            rootDirName = None
            
            bxPlatformConfigBase = bxPlatformThis.pkgBase_configDir()
            
            if pbdName == "bisosRoot":
                rootDirName = bxPlatformConfig.rootDir_bisos_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "deRunRoot":
                rootDirName = bxPlatformConfig.rootDir_bxo_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "bxoRoot":
                rootDirName = bxPlatformConfig.rootDir_deRun_fpObtain(bxPlatformConfigBase)
            else:
                icm.EH_problem_usageError("")

            return rootDirName

        bisosUserName = bisosUserName_obtain()
        bisosGroupName = bisosGroupName_obtain()

        pbdNamesList = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        if pbdNamesList[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&-1")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            pbdNamesList = argChoices

	for each in pbdNamesList:
            rootDir = withPbdNameGetRootForPlatform(each)
            # icm.ANN_here("{} -- {}".format(each, rootDir))
            try: 
                os.makedirs(rootDir)
            except OSError:
                if not os.path.isdir(rootDir):
                    raise

            # Python 3
            #shutil.chown(rootDir, bisosUserName, bisosGroupName)
            uid = pwd.getpwnam(bisosUserName).pw_uid
            gid = grp.getgrnam(bisosGroupName).gr_gid
            os.chown(rootDir, uid, gid)

            os.chmod(rootDir, 0775)            

            outcome = icm.subProc_bash("""\
ls -ld  {rootDir}"""
                                       .format(rootDir=rootDir)
            ).log()
            if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
            

        #icm.ANN_here("{}".format(bisosUserName))

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="pbdNamesList",
            argDefault='all',
            argChoices=['all', 'bisosRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdUpdateForPlatform" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pbdUpdateForPlatform/ parsMand= parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdUpdateForPlatform(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        def withPbdNameGetRootForPlatform(pbdName):
            rootDirName = None
            
            bxPlatformConfigBase = bxPlatformThis.pkgBase_configDir()
            
            if pbdName == "bisosRoot":
                rootDirName = bxPlatformConfig.rootDir_bisos_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "bxoRoot":
                rootDirName = bxPlatformConfig.rootDir_bxo_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "deRunRoot":
                rootDirName = bxPlatformConfig.rootDir_deRun_fpObtain(bxPlatformConfigBase)
            else:
                icm.EH_problem_usageError("")

            return rootDirName
            

        pbdNamesList = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        if pbdNamesList[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&-1")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            #pbdNamesList = copy.deepcopy(argChoices)
            pbdNamesList = argChoices

        icm.LOG_here("{}".format(pbdNamesList))

	for each in pbdNamesList:
            rootDir = withPbdNameGetRootForPlatform(each)

            pbdUpdate().cmnd(
                interactive=False,
                baseDir=rootDir,
                pbdName=each,
                argsList=['all'],
            )

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="pbdNamesList",
            argDefault='all',
            argChoices=['all', 'bisosRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict
    

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

    

####+BEGIN: bx:dblock:python:section :title "BxpBaseDir Classes"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *BxpBaseDir Classes*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
    

####+BEGINNOT: bx:dblock:python:enum :enumName "bpd_BaseDirType" :comment ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Enum           :: /bpd_BaseDirType/  [[elisp:(org-cycle)][| ]]
"""
#@enum.unique
class bpd_BaseDirType(enum.Enum):
####+END:
    directory = 'directory'
    symLink = 'symLink'
    gitClone = 'gitClone'


####+BEGIN: bx:dblock:python:func :funcName "bxpObjGet_baseDir" :funcType "BxPD" :retType "BxpBaseDir_Dir" :argsList "pathRoot pathRel" :deco "default"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-BxPD      :: /bxpObjGet_baseDir/ retType=BxpBaseDir_Dir argsList=(pathRoot pathRel) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def bxpObjGet_baseDir(
    pathRoot,
    pathRel,
):
####+END:
    return (
        BxpBaseDir_Dir(
            destPathRoot=pathRoot,
            destPathRel=pathRel,
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bxpObjGet_symLink" :comment "Incomplete" :funcType "BxPD" :retType "BxpBaseDir_SymLink" :argsList "pathRoot dstPathRel srcPath srcPathType='internal'" :deco "default"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-BxPD      :: /bxpObjGet_symLink/ =Incomplete= retType=BxpBaseDir_SymLink argsList=(pathRoot dstPathRel srcPath srcPathType='internal') deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def bxpObjGet_symLink(
    pathRoot,
    dstPathRel,
    srcPath,
    srcPathType='internal',
):
####+END:
    return (
        BxpBaseDir_SymLink(
            destPathRoot=pathRoot,
            destPathRel=dstPathRel,
            srcPath=srcPath,
            srcPathType=srcPathType,
        )
    )




####+BEGIN: bx:dblock:python:subSection :title "Class Definitions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Class Definitions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: bx:dblock:python:class :className "BxpBaseDir" :superClass "object" :comment "Expected to be subclassed" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /BxpBaseDir/ object =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class BxpBaseDir(object):
####+END:
    """	
** ByStar platform base directory specification. 	
"""
    owner = bisosUserName_obtain()
    group = bisosGroupName_obtain()
    permissions = "775"
    
    def __init__(
        self,
        baseDirType=None,
        destPathRoot=None,
        destPathRel=None,            
    ):
        self.baseDirType=baseDirType
        self.destPathRoot=destPathRoot
        self.destPathRel=destPathRel

    def destPathFullGet(self,):
        return (
            os.path.abspath(
                os.path.join(self.destPathRoot, self.destPathRel)
            )
        )
        


####+BEGIN: bx:dblock:python:class :className "BxpBaseDir_Dir" :superClass "BxpBaseDir" :comment "Actual" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /BxpBaseDir_Dir/ BxpBaseDir =Actual=  [[elisp:(org-cycle)][| ]]
"""
class BxpBaseDir_Dir(BxpBaseDir):
####+END:
    """	
** ByStar platform base directory specification. 	
"""
    
    def __init__(
        self,
        baseDirType=bpd_BaseDirType.directory,
        destPathRoot=None,
        destPathRel=None,            
        basePrepFunc=None,
        baseCleanFunc=None,
        comment=None,                        
    ):
        self.baseDirType=baseDirType
        self.destPathRoot=destPathRoot
        self.destPathRel=destPathRel
        self.basePrepFunc=basePrepFunc
        self.baseCleanFunc=baseCleanFunc
        self.comment=comment

    def __str__(self):
        return (
            """
baseDirType={baseDirType}
destPathRoot={destPathRoot}
destPathRel={destPathRel}
owner={owner}
group={group}
permissions={permissions}
basePrepFunc={basePrepFunc}
baseCleanFunc={baseCleanFunc}
comment={comment}
""".format(
    baseDirType=self.baseDirType,
    destPathRoot=self.destPathRoot,
    destPathRel=self.destPathRel,
    owner=self.__class__.owner,
    group=self.__class__.group,
    permissions=self.__class__.permissions,
    basePrepFunc=self.basePrepFunc,
    baseCleanFunc=self.baseCleanFunc,
    comment=self.comment,
        ))

    def update(self):
        destFullPath = self.destPathFullGet()
        if os.path.isdir(destFullPath):
            icm.ANN_here("{} Exists -- mkdir Skipped".format(destFullPath))
        else:
            try:
                os.makedirs(destFullPath)
            except OSError:
                if not os.path.isdir(destFullPath):
                    raise
            icm.ANN_write("Created {}".format(destFullPath))


    def verify(self):
        destFullPath = self.destPathFullGet()        
        if os.path.isdir(destFullPath):
            icm.ANN_here("{} Exists -- As Expected".format(destFullPath))
        else:
            icm.ANN_here("{} Missing -- Un-Expected".format(destFullPath))
        
    def show(self):
        icm.ANN_write("{}".format(self.__str__()))
        
    


####+BEGIN: bx:dblock:python:class :className "BxpBaseDir_SymLink" :superClass "BxpBaseDir" :comment "Actual" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /BxpBaseDir_SymLink/ BxpBaseDir =Actual=  [[elisp:(org-cycle)][| ]]
"""
class BxpBaseDir_SymLink(BxpBaseDir):
####+END:
    """	
** ByStar platform base directory specification. 	
"""
    
    def __init__(
        self,
        destPathRoot,
        destPathRel,
        srcPath,
        srcPathType='internal',            
        basePrepFunc=None,
        baseCleanFunc=None,
        comment=None,                        
    ):
        self.baseDirType=bpd_BaseDirType.symLink
        self.destPathRoot=destPathRoot
        self.destPathRel=destPathRel
        self.srcPath=srcPath
        self.srcPathType=srcPathType        
        self.basePrepFunc=basePrepFunc
        self.baseCleanFunc=baseCleanFunc
        self.comment=comment

    def __str__(self):
        return (
            """
baseDirType={baseDirType}
destPathRoot={destPathRoot}
srcPath={srcPath}
srcPathType={srcPathType}
owner={owner}
group={group}
permissions={permissions}
basePrepFunc={basePrepFunc}
baseCleanFunc={baseCleanFunc}
comment={comment}
""".format(
    baseDirType=self.baseDirType,
    destPathRoot=self.destPathRoot,
    srcPath=self.srcPath,
    srcPathType=self.srcPathType,
    destPathRel=self.destPathRel,    
    owner=self.__class__.owner,
    group=self.__class__.group,
    permissions=self.__class__.permissions,
    basePrepFunc=self.basePrepFunc,
    baseCleanFunc=self.baseCleanFunc,
    comment=self.comment,
        ))

    def srcFullPathObtain(self):
        # NOTYET, check srcPathType
        return (
            os.path.abspath(
                os.path.join(self.destPathRoot, self.srcPath)
            )
        )
    

    def update(self):
        destFullPath = self.destPathFullGet()
        srcFullPath = self.srcFullPathObtain()

        def createSymLink():
            try:            
                os.remove(destFullPath)
            except OSError:
                pass
            
            try:
                os.symlink(srcFullPath, destFullPath)
            except OSError:
                if not os.path.islink(destFullPath):
                    raise
            icm.ANN_write("Created {} SymLink pointing to: {}".format(
                destFullPath, srcFullPath))
        
        if os.path.islink(destFullPath):
            linkPointsToPath = os.readlink(destFullPath)
            if srcFullPath == linkPointsToPath:
                icm.ANN_here("{} SymLink exists and correctly points to: {}".format(
                    destFullPath, srcFullPath))
            else:
                createSymLink() 
        else:
            createSymLink()


    def verify(self):
        destFullPath = self.destPathFullGet()
        srcFullPath = self.srcFullPathObtain()

        if os.path.islink(destFullPath):
            linkPointsToPath = os.readlink(destFullPath)
            if srcFullPath == linkPointsToPath:
                icm.ANN_here("{} SymLink exists and correctly points to: {}".format(
                    destFullPath, srcFullPath))
            else:
                icm.ANN_here("{} SymLink exists but is wrong -- points to: {} instead of".format(
                    destFullPath, linkPointsToPath, srcFullPath))
        else:
            icm.ANN_here("{} SymLink is missing".format(
                destFullPath,))

        
    def show(self):
        icm.ANN_write("{}".format(self.__str__()))
        



####+BEGIN: bx:dblock:python:class :className "BxpBaseDir_Command" :superClass "BxpBaseDir" :comment "Actual" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /BxpBaseDir_Command/ BxpBaseDir =Actual=  [[elisp:(org-cycle)][| ]]
"""
class BxpBaseDir_Command(BxpBaseDir):
####+END:
    """	
** ByStar platform base directory specification. 	
"""
    
    def __init__(
        self,
        destPathRoot,
        destPathRel,
        createCommand,
        basePrepFunc=None,
        baseCleanFunc=None,
        comment=None,                        
    ):
        self.baseDirType=bpd_BaseDirType.symLink
        self.destPathRoot=destPathRoot
        self.destPathRel=destPathRel
        self.createCommand=createCommand
        self.basePrepFunc=basePrepFunc
        self.baseCleanFunc=baseCleanFunc
        self.comment=comment

    def __str__(self):
        return (
            """
baseDirType={baseDirType}
destPathRoot={destPathRoot}
createCommand={createCommand}
owner={owner}
group={group}
permissions={permissions}
basePrepFunc={basePrepFunc}
baseCleanFunc={baseCleanFunc}
comment={comment}
""".format(
    baseDirType=self.baseDirType,
    destPathRoot=self.destPathRoot,
    createCommand=self.createCommand,
    destPathRel=self.destPathRel,    
    owner=self.__class__.owner,
    group=self.__class__.group,
    permissions=self.__class__.permissions,
    basePrepFunc=self.basePrepFunc,
    baseCleanFunc=self.baseCleanFunc,
    comment=self.comment,
        ))


    def update(self):
        destFullPath = self.destPathFullGet()
        if os.path.isdir(destFullPath):
            icm.ANN_here("{} Exists -- mkdir Skipped".format(destFullPath))
            return None

        outcome = icm.subProc_bash(
            self.createCommand,
        ).out()
        if outcome.isProblematic(): return icm.EH_badOutcome(outcome)
        

    def verify(self):            
        destFullPath = self.destPathFullGet()        
        if os.path.isdir(destFullPath):
            icm.ANN_here("{} Exists -- As Expected".format(destFullPath))
        else:
            icm.ANN_here("{} Missing -- Un-Expected".format(destFullPath))
            
        
    def show(self):
        icm.ANN_write("{}".format(self.__str__()))
        
        


####+BEGIN: bx:dblock:python:class :className "BxpBaseDir_GitClone" :superClass "BxpBaseDir" :comment "" :classType ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-         :: /BxpBaseDir_GitClone/ BxpBaseDir  [[elisp:(org-cycle)][| ]]
"""
class BxpBaseDir_GitClone(BxpBaseDir):
####+END:
    """	
** ByStar platform base directory specification. 	
"""
   
    def __init__(
        self,
        destPathRel=None,
    ):
        #self.baseDirType = 
        #self.__class__.destPathRel = destPathRel
        pass

    def __str__(self):
        return format(
            'baseDirType: ' + str(self.baseDirType)
        )
    

####+BEGIN: bx:dblock:python:section :title "Slice Definitions PipPkgsList Classes"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Slice Definitions PipPkgsList Classes*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
    



####+BEGIN: bx:dblock:python:class :className "PipPkgsList" :superClass "object" :comment "Expected to be subclassed" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /PipPkgsList/ object =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class PipPkgsList(object):
####+END:
    """	
** Process a pipPkgsList, which could be passed as inPkgsList or over-writen in pkgsListSpec.	
"""
   
    def __init__(
        self,
        virtualenvBaseDir,
        inPkgsList=None,
        pyVersion=None,
        bisosVersion=None,
    ):
        self.virtualenvBaseDir = virtualenvBaseDir        
        self.inPkgsList = inPkgsList
        self.pyVersion = pyVersion
        self.bisosVersion = bisosVersion
 
    def pkgsListSpec(self):
        pl = collections.OrderedDict()
        pl['pkgName'] = "cur"  # pkgVersion
        return pl

    def pkgsListObtain(self):
        if self.inPkgsList:
            return self.inPkgsList
        else:
            return self.pkgsListSpec()
    
    def __str__(self):
        pkgsList = self.pkgsListObtain()        
        return (
            """NOTYET,  {}""".format(pkgsList)
        )

    def execActionStr(self, actionStr):
        if actionStr == "verify":
            return self.verify()
        elif actionStr == "show":
            return self.show()
        elif actionStr == "update":
            return self.update()
        elif actionStr == "list":
            return self.list()
        else:
            icm.EH_critical_oops("")
            return

    def list(self):
        pkgsList = self.pkgsListObtain()
        for each in pkgsList:
            icm.ANN_write(each)
        return pkgsList
 
    def verify(self):
        pkgsList = self.pkgsListObtain()
        return pkgsList
        
    def show(self):
        icm.ANN_write("{}".format(self.__str__()))
        
    def update(self):
        pkgsList = self.pkgsListObtain()
        activateFile = os.path.join(self.virtualenvBaseDir, "bin/activate")
        for each in pkgsList:
            outcome = icm.subProc_bash(
                """\
source {activateFile}; \
pip install --no-cache-dir {each}; \
"""
                .format(activateFile=activateFile, each=each)
            ).out()
            if outcome.isProblematic(): return icm.EH_badOutcome(outcome)



####+BEGIN: bx:dblock:python:class :className "PipPkgsList_BisosFoundation" :superClass "PipPkgsList" :comment "Actual" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /PipPkgsList_BisosFoundation/ PipPkgsList =Actual=  [[elisp:(org-cycle)][| ]]
"""
class PipPkgsList_BisosFoundation(PipPkgsList):
####+END:
    """	
** SubClassed with pkgsListSpec	
"""
 
    def pkgsListSpec(self):
        pl = collections.OrderedDict()
        pl['coverage'] = "cur"
        return pl

            

####+BEGIN: bx:dblock:python:class :className "PipPkgsList_BisosBase" :superClass "PipPkgsList" :comment "Actual" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-basic    :: /PipPkgsList_BisosBase/ PipPkgsList =Actual=  [[elisp:(org-cycle)][| ]]
"""
class PipPkgsList_BisosBase(PipPkgsList):
####+END:
    """	
** SubClassed with pkgsListSpec	
"""
 
    def pkgsListSpec(self):
        pl = collections.OrderedDict()
        pl['unisos'] = "cur"
        pl['unisos.ucf'] = "cur"
        pl['unisos.icm'] = "cur"
        pl['unisos.common'] = "cur"
        pl['unisos.x822Msg'] = "cur"
        pl['unisos.marme'] = "cur"
        
        pl['bisos'] = "cur"
        pl['bisos.common'] = "cur"
        pl['bisos.bx-bases'] = "cur"
        pl['bisos.things'] = "cur"
        pl['bisos.gossonot'] = "cur"        
        return pl

####+BEGIN: bx:dblock:python:subSection :title "Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxpRootObsoleted" :comment "pbd Dictionary" :funcType "Init" :retType "bxpRootBaseDirsDict" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-Init      :: /pbdDict_bxpRootObsoleted/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxpRootObsoleted(
    baseDir,
):
####+END:

    pbdDict = collections.OrderedDict()

    root = bxpRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpObjGet_baseDir(root, '')

    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        pbdDict[dstPathRel] = BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )
        
    directory('dist')
    directory('dist/venv')
    command(  'dist/venv/py2-bisos-3',
              "virtualenv --no-site-packages --python=python2 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('dist/venv/py2-bisos-3')))
    command(  'dist/venv/dev-py2-bisos-3',
              "virtualenv --no-site-packages --python=python2 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('dist/venv/dev-py2-bisos-3')))
    command(  'dist/venv/py3-bisos-3',
              "virtualenv --no-site-packages --python=python3 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('dist/venv/py3-bisos-3')))
    command(  'dist/venv/dev-py3-bisos-3',
              "virtualenv --no-site-packages --python=python3 {fullDestPathGet}"
              .format(fullDestPathGet=fullDestPathGet('dist/venv/dev-py3-bisos-3')))
    directory('dist/pip')
    directory('dist/pip/bisos')
    directory('dist/pip/bisos/bin')
    directory('dist/pip/bisos/input')                
    directory('dist/pip/blee')
    directory('dist/pip/bsip')    
    
    directory('vcAuth')
    directory('vcAuth/bisos')
    
    directory('vcAnon')
    directory('vcAnon/bisos')    

    directory('control')
    directory('control/bisos')    
    directory('control/bisos/site')    

    directory('var')
    directory('var/bisos')
    directory('var/bisos/icmsPkg')        
    
    directory('tmp')
    
    directory('log')
    directory('log/bisos')

    directory('bisos')
    symLink(  'bisos/bin', 'dist/pip/bisos/bin')
    symLink(  'bisos/input', 'dist/pip/bisos/input')
    symLink(  'bisos/var', 'var/bisos')
    symLink(  'bisos/tmp', 'tmp')
    symLink(  'bisos/log', 'log/bisos')                
              
    directory('bsip')
    
    directory('blee')

    return pbdDict


####+BEGIN: bx:dblock:python:icmItem :itemType "List" :itemTitle "pbdList_bystar" :comment "=OBSOLETED="
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || List           :: pbdList_bystar ==OBSOLETED==  [[elisp:(org-cycle)][| ]]
"""
####+END:

pbdList_bystarObsoleted = [
    "/"
    "var",
    "control",
    "data",
    "tmp",
    "log",    
    "dist",
    "vcAuth",
    "vcAnon",
    "bisos",
    "bsip",
    "blee",    
]


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdListUpdate_Obsoleted" :parsMand "" :parsOpt "baseDir pbdName" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /pbdListUpdate_Obsoleted/ parsMand= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdListUpdate_Obsoleted(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        baseDir=None,         # or Cmnd-Input
        pbdName=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        baseDir = callParamsDict['baseDir']
        pbdName = callParamsDict['pbdName']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
	def cmndDesc(): """
** Doc String Outside Of Dblock.
"""
        icm.ANN_write("{}".format(baseDir))

        for eachArg in  effectiveArgsList:
            pbdList = eval('{}'.format(eachArg))
            for each in pbdList:
                pbdUpdate().cmnd(
                    interactive=False,
                    baseDir=baseDir,
                    argsList=each.split(),
                )

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )



####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
