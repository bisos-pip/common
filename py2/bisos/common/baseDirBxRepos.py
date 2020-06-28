# -*- coding: utf-8 -*-
"""\
*    *[Summary]* ::  A /library/ with ICM Cmnds to support BxRepos bases (/bisos/vc/git) creation facilities
** if anon git clone git://github.com/SomeUser/SomeRepo.git if auth git clone git@github.com:UserName/OtherRepo.git
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft ""
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/bisos/common/dev/bisos/common/baseDirBxRepos.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net

 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "baseDirBxRepos"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201810092926"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/dev/null"
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
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
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

from bisos.common import bxpBaseDir

import shutil
import copy

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

"""
** TODO gitClone needs to support anon, auth=authSsh and authHttp. 
   SCHEDULED: <2020-06-25 Thu>
"""

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bxReposBaseDir_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /bxReposBaseDir_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bxReposBaseDir_libOverview(icm.Cmnd):
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
*** bxReposRootXxFile   -- /etc/bxReposRoot, ~/.bxReposRoot, /bxRepos
*** bxReposRoot         -- Base For This Module
*** bpb             -- BxRepos Platform Base, Location Of Relevant Parts (BxRepos, blee, bsip
*** bpd             -- BxRepos Platform Directory (Object), An instance of Class BxReposBaseDir
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
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Directory Base Locations*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:subSection :title "BxRepos Root"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BxRepos Root*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bxReposRootBaseDirPtrUserFile_obtain" :comment "~/.bxReposRoot" :funcType "obtain" :retType "str" :argsList "" :deco "ucf.runOnceOnlyReturnFirstInvokation"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bxReposRootBaseDirPtrUserFile_obtain/ =~/.bxReposRoot= retType=str argsList=nil deco=ucf.runOnceOnlyReturnFirstInvokation  [[elisp:(org-cycle)][| ]]
"""
@ucf.runOnceOnlyReturnFirstInvokation
def bxReposRootBaseDirPtrUserFile_obtain():
####+END:
    return os.path.abspath(
        os.path.expanduser(
            "~/.bxReposRoot"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bxReposRootBaseDirDefault_obtain" :comment "/bxRepos" :funcType "obtain" :retType "str" :argsList "" :deco "ucf.runOnceOnlyReturnFirstInvokation"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bxReposRootBaseDirDefault_obtain/ =/bxRepos= retType=str argsList=nil deco=ucf.runOnceOnlyReturnFirstInvokation  [[elisp:(org-cycle)][| ]]
"""
@ucf.runOnceOnlyReturnFirstInvokation
def bxReposRootBaseDirDefault_obtain():
####+END:
    return os.path.abspath(
        "/bisos/git/auth/bxRepos"
    )


####+BEGIN: bx:dblock:python:subSection :title "BXREPOS Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BXREPOS Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "pbBxRepos_baseObtain_root" :comment "BXREPOS BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /pbBxRepos_baseObtain_root/ =BXREPOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbBxRepos_baseObtain_root(
    baseDir,
):
####+END:
    bxReposRoot = bxReposRoot_baseObtain(baseDir)            

    return ( os.path.join(
        bxReposRoot,
        # "bxRepos", Obsolted After introduction of bxReposlatformConfig
        # NOTYET, Is this necessary?
    ))


####+BEGIN: bx:dblock:python:func :funcName "pbBxRepos_baseObtain_bin" :comment "BXREPOS BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /pbBxRepos_baseObtain_bin/ =BXREPOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbBxRepos_baseObtain_bin(
    baseDir,
):
####+END:
    return ( os.path.join(
        pbBxRepos_baseObtain_root(baseDir),
        "bin",
    ))

####+BEGIN: bx:dblock:python:func :funcName "pbBxRepos_baseObtain_var" :comment "BXREPOS BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /pbBxRepos_baseObtain_var/ =BXREPOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbBxRepos_baseObtain_var(
    baseDir,
):
####+END:
    return( os.path.join(
        pbBxRepos_baseObtain_root(baseDir),
        "var",
    ))


####+BEGIN: bx:dblock:python:subSection :title "BXREPOS Pkg Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BXREPOS Pkg Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:section :title "Common Arguments Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Arguments Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-ParSpec   :: /commonParamsSpecify/ retType= argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
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

    icmParams.parDictAdd(
        parName='vcMode',
        parDescription="VC (git) Mode -- auth or anon",
        parDataType=None,
        parDefault=None,
        parChoices=["auth", "anon",],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--vcMode',
    )

    
        
####+BEGIN: bx:dblock:python:section :title "Common Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "examples_bxReposBaseDirsCommon" :comment "Base Roots Info And Preps" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-examples  :: /examples_bxReposBaseDirsCommon/ =Base Roots Info And Preps= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxReposBaseDirsCommon():
####+END:
    icm.cmndExampleMenuChapter('* =BxRepos BaseDir=  BxRepos Platform Base Dirs')

    cmndName = "bxReposRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "bxReposRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['baseDir'] = '/tmp/bxBase'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    icm.ex_gExecMenuItem(execLine="""cat {}""".format(bxReposRootBaseDirPtrUserFile_obtain()),)
    #icm.ex_gExecMenuItem(execLine="""cat {}""".format(bxReposRootBaseDirPtrSysFile_obtain()),)
    icm.ex_gExecMenuItem(execLine="""ls -l {}""".format(bxReposRootBaseDirDefault_obtain(),))
    
    # icm.ex_gExecMenuItem(execLine="""ls -l /bisos/vc/git/bxRepos/*""")   
    # icm.ex_gExecMenuItem(execLine="""sudo mkdir -p /bisos/vc/git/bxRepos/auth; sudo chown {}:{} /bisos/vc/git/bxRepos/auth"""
    #                      .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))
    # icm.ex_gExecMenuItem(execLine="""sudo mkdir -p /bisos/vc/git/bxRepos/anon; sudo chown {}:{} /bisos/vc/git/bxRepos/anon"""
    #                      .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))

    #icm.ex_gExecMenuItem(execLine="""ls -l /bisos/git/auth/bxRepos/*""")   
    icm.ex_gExecMenuItem(execLine="""sudo mkdir -p /bisos/git/auth; sudo chown {}:{} /bisos/git/auth"""
                         .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))
    icm.ex_gExecMenuItem(execLine="""sudo mkdir -p /bisos/git/anon; sudo chown {}:{} /bisos/git/anon"""
                         .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))

####+BEGIN: bx:dblock:python:func :funcName "examples_bxReposBaseDirs" :comment "bx-bases.py module information" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-examples  :: /examples_bxReposBaseDirs/ =bx-bases.py module information= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxReposBaseDirs():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    #examples_bxReposlatformBaseDirsCommon()

    icm.cmndExampleMenuChapter('* =BxRepos BaseDir=  Module Description,Usage,Status Information')
    
    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="bx-bases", verbosity='none')    


####+BEGIN: bx:dblock:python:func :funcName "examples_bxReposBaseDirsFull" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-examples  :: /examples_bxReposBaseDirsFull/ =Show/Verify/Update For relevant PBDs= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxReposBaseDirsFull():
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
    
    #bxRootBase = bxReposRoot_baseObtain(None)

    examples_bxReposBaseDirsCommon()
    
    icm.cmndExampleMenuChapter('* =Module=  Overview (desc, usage, status)')    
   
    cmndName = "overview_bxReposBaseDir" ; cmndArgs = "moduleDescription moduleUsage moduleStatus" ;
    cps = collections.OrderedDict()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    icm.cmndExampleMenuChapter(' =BxReposCollection DirBases=  *pbdShow/pbdVerify/pbdUpdate Of Relevant PBDs*')    

    icm.cmndExampleMenuSection(' =BxReposCollection DirBases=  *pbdVerify*')            

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/anon';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'anon'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/auth';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'auth'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
   
    icm.cmndExampleMenuSection(' =BxReposCollection DirBases=  *pbdUpdate*')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/anon';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'anon'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/auth';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'auth'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    
    icm.cmndExampleMenuChapter(' =BxRepos DirBases=  *pbdShow/pbdVerify/pbdUpdate Of Relevant PBDs*')    

    # icm.cmndExampleMenuSection(' =BxRepos DirBases=  *pbdShow*')        
    # cmndName = "pbdShow" ; cmndArgs = "/ blee-pip" ;
    # cps = collections.OrderedDict() ;
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdShow" ; cmndArgs = "/ blee-pip" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bxReposRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bxReposRoot'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    icm.cmndExampleMenuSection(' =BxRepos DirBases=  *pbdVerify*')            
    
    cmndName = "pbdVerify" ; cmndArgs = "/ blee-pip" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'; cps['pbdName'] = 'bxReposRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'; cps['pbdName'] = 'bxReposRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
    icm.cmndExampleMenuSection(' =BxRepos DirBases=  *pbdUpdate*')
    
    cmndName = "pbdUpdate" ; cmndArgs = "/ blee-pip" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'; cps['pbdName'] = 'bxReposRoot' 
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/anon/bxRepos';
    cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'anon'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/auth/bxRepos';
    cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'auth'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict(); cps['baseDir'] = '/bisos/git/anon/ext';
    cps['pbdName'] = 'extRepos' ; cps['vcMode'] = 'anon'
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    
    # cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/vc/git/bxRepos/anon';
    # cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'anon'
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/vc/git/bxRepos/auth';
    # cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'auth'
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    
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
 
    icm.cmndExampleMenuSection(' =BxRepos DirBases Creation/Ownership=  *pbdRootsForPlatform*')   
    
    cmndName = "pbdRootsForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    cmndName = "pbdRootsForPlatform" ; cmndArgs = "bxReposRoot" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    icm.cmndExampleMenuSection(' =BxRepos DirBases Update=  *pbdUpdateForPlatform*')   

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "bxReposRoot" ;
    cps=cpsInit() ; icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")
    
    # pbdList has been OBSOLETED
    # icm.cmndExampleMenuChapter(' =BxRepos DirBases=  *pbdShow/pbdVerify/pbdUpdate*')    

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bxRepos" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bxRepos" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] =  bxRootBase
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    
####+BEGIN: bx:dblock:python:section :title "Misc To Be Sorted Out"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Misc To Be Sorted Out*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    
####+BEGIN: bx:dblock:python:func :funcName "bxReposUserName_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Obtain    :: /bxReposUserName_obtain/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def bxReposUserName_obtain():
####+END:
    """
** BxRepos UserName.
"""
    import getpass
    
    return getpass.getuser()


####+BEGIN: bx:dblock:python:func :funcName "bxReposGroupName_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Obtain    :: /bxReposGroupName_obtain/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def bxReposGroupName_obtain():
####+END:
    """
** BxRepos GroupName
"""
    return os.getegid()


####+BEGIN: bx:dblock:python:section :title "Base Dirs Specifications ::"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Base Dirs Specifications ::*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:section :title " /===== PBD SPECIFICATION CMNDs =====/ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    * /===== PBD SPECIFICATION CMNDs =====/ *  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxReposCollection" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bxReposCollection/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxReposCollection(
    baseDir,
    vcMode=None,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bxReposBasesInstall.tex
*** See: \section{/bxRepos Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    root = bxReposRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpBaseDir.bxpObjGet_baseDir(root, '')

    if not vcMode:
        vcMode = "anon"
    
    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpBaseDir.bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpBaseDir.bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        pbdDict[dstPathRel] = bxpBaseDir.BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )

    def gitClone(dstPathRel, gitRepoPath, vcMode):
        pathComps = os.path.split(dstPathRel)
        baseDir = pathComps[0]
        #repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            # "cd {root}/{baseDir}; git clone git@github.com:{gitRepoPath}.git"
            command(  dstPathRel,
              "cd {root}/{baseDir}; git clone git://github.com/{gitRepoPath}.git"
              .format(root=root, baseDir=baseDir, gitRepoPath=gitRepoPath)
            )
        elif vcMode == "auth":
            command(  dstPathRel,
              "cd {root}/{baseDir}; git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
              .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            )
        else:
            icm.EH_problem_usageError("")
            

    def gitCloneBase(dstPathRel, gitRepoPath, vcMode):
        pathComps = os.path.split(gitRepoPath)
        baseDir = pathComps[0]
        repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            # "cd {root}; git clone git@github.com:{gitRepoPath}.git"
            command(  dstPathRel,
              "cd {root}; git clone git://github.com/{gitRepoPath}.git"                      
              .format(root=root, baseDir=baseDir, gitRepoPath=gitRepoPath)
            )
            command(  dstPathRel,
              "cd {root}; mv {repoName} {dstPathRel}".format(root=root, repoName=repoName, dstPathRel=dstPathRel))
            
        elif vcMode == "auth":
            command(  dstPathRel,
              "cd {root}; git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
              .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            )
            command(  gitRepoPath,            
                      "cd {root}; mv {repoName} {dstPathRel}".format(root=root, repoName=repoName, dstPathRel=dstPathRel)
            )
            
        else:
            icm.EH_problem_usageError("")
            
            
    #
    # NOTYET, this is a hack for now. To Be replaced by bue.credentials
    #

    with open('/acct/employee/lsipusr/gitUserName', 'r') as myfile:
        gitUserName=myfile.read().replace('\n', '')        

    with open('/acct/employee/lsipusr/gitPasswd', 'r') as myfile:
        gitPasswd=myfile.read().replace('\n', '')        

    #
    # NOTYET, the model of specifying one command here is wrong.
    # We should be dealing with abstract directory bases, where
    # each directory base has a create and verify method.
    # Things like update and clean, etc should then be driven
    # with the fto (File Tree Objects).
    #
    # So, gitCloneBase should be renamed gitReposCollectionBase and gitRepoBase
    #

    command(  'bxReposBasedir',
              "mkdir -p {root}".format(root=root))
    
    gitCloneBase( 'bxRepos',  'ByStar/bxReposBase', vcMode)    
    
    return pbdDict



####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxReposRoot" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bxReposRoot/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxReposRoot(
    baseDir,
    vcMode=None,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bxReposBasesInstall.tex
*** See: \section{/bxRepos Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    root = bxReposRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpBaseDir.bxpObjGet_baseDir(root, '')

    if not vcMode:
        vcMode = "anon"
    
    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpBaseDir.bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpBaseDir.bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        # print("AAAA Entering command {createCmnd}".format(createCmnd=createCmnd))
        pbdDict[dstPathRel] = bxpBaseDir.BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )

    #
    # NOTYET, Change the name to: gitMapClone,
    # Make it be
    #    gitCloneBase(locPathRel, remGitRepoPath, vcMode)
    #  A single gitMapClone can then do both gitClone() and gitCloneBase()
    #  If basename of locPathRel and remGitRepoPath are the same, we then have gitClone()
    #  Otherwise, gitCloneBase() which includes the move.
    #
        
    def gitClone(dstPathRel, gitRepoPath, vcMode):
        """ repoName of remGitRepoPath, is same as basename of dstPathRel"""
        pathComps = os.path.split(dstPathRel)
        baseDir = pathComps[0]
        #repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            #               "cd {root}/{baseDir} && git clone git@github.com:{gitRepoPath}.git"
            command(  dstPathRel,
              "cd {root}/{baseDir} && git clone git://github.com/{gitRepoPath}.git"
              .format(root=root, baseDir=baseDir, gitRepoPath=gitRepoPath)
            )
        elif vcMode == "auth":
            command(  dstPathRel,
              "cd {root}/{baseDir} && git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
              .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            )
        else:
            icm.EH_problem_usageError("")


    def gitCloneBase(locPathRel, remGitRepoPath, vcMode):
        locBasenameRel = os.path.basename(locPathRel)
        locDirnameRel =  os.path.dirname(locPathRel)
        
        locDirnameFull = os.path.join(root, locDirnameRel)
        
        repoName = os.path.basename(remGitRepoPath)

        # This is the before the move to locPathRel location
        locDirnamePlusRepoRel = os.path.join(locDirnameRel, repoName)        
        
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            # "cd {locDirnameFull} && git clone git@github.com:{remGitRepoPath}.git"
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            command(  locPathRel,
                      "cd {locDirnameFull} && git clone git://github.com/{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                      .format(locDirnameFull=locDirnameFull, remGitRepoPath=remGitRepoPath, repoName=repoName, locBasenameRel=locBasenameRel)
            )
            
        elif vcMode == "auth":
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            command(  locDirnamePlusRepoRel,
              "cd {locDirnameFull} && git clone https://{gitUserName}:{gitPasswd}@github.com/{remGitRepoPath} && mv {repoName} {locBasenameRel}"
              .format(
                  locDirnameFull=locDirnameFull,
                  gitUserName=gitUserName,
                  gitPasswd=gitPasswd,
                  remGitRepoPath=remGitRepoPath,
                  repoName=repoName,
                  locBasenameRel=locBasenameRel
              )
            )
            
        else:
            icm.EH_problem_usageError("")
            
            
    #
    # NOTYET, this is a hack for now. To Be replaced by bue.credentials
    #

    with open('/acct/employee/lsipusr/gitUserName', 'r') as myfile:
        gitUserName=myfile.read().replace('\n', '')        

    with open('/acct/employee/lsipusr/gitPasswd', 'r') as myfile:
        gitPasswd=myfile.read().replace('\n', '')        

    #
    # NOTYET, the model of specifying one command here is wrong.
    # We should be dealing with abstract directory bases, where
    # each directory base has a create and verify method.
    # Things like update and clean, etc should then be driven
    # with the fto (File Tree Objects).
    #
    # So, gitCloneBase should be renamed gitReposCollectionBase and gitRepoBase
    #


    directory( 'mohsenBanan')
    gitClone( 'mohsenBanan/ReposOverview',  'mohsenBanan/ReposOverview', vcMode)
    gitClone( 'mohsenBanan/StartHere',  'mohsenBanan/StartHere', vcMode)        

    gitCloneBase( 'ByStar',  'ByStar/base', vcMode)    
    gitClone( 'ByStar/overview',  'ByStar/overview', vcMode)

    
    gitCloneBase( 'unisos',  'bx-unisos/base', vcMode)
    gitClone( 'unisos/overview',  'bx-unisos/overview', vcMode)
    

    gitCloneBase( 'bisos',  'bisos/base', vcMode)
    gitClone( 'bisos/overview',  'bisos/overview', vcMode)
    
    
    gitCloneBase( 'blee',  'bx-blee/base',  vcMode)
    gitClone( 'blee/overview',  'bx-blee/overview',  vcMode)
    gitClone(
        'blee/org-img-link',
        'bx-blee/org-img-link',
        vcMode
    )
    gitClone(
        'blee/persian-input-method',
        'bx-blee/persian-input-method',
        vcMode
    )
    

    gitCloneBase( 'bxGenesis',  'bxGenesis/base', vcMode)
    gitClone( 'bxGenesis/overview',  'bxGenesis/overview', vcMode)

    gitClone( 'bxGenesis/vagrants',  'bxGenesis/vagrants', vcMode)
    gitClone( 'bxGenesis/vagrantBue',  'bxGenesis/vagrantBue', vcMode)    
    gitClone( 'bxGenesis/fbxoPkgs',  'bxGenesis/fbxoPkgs', vcMode)
    gitClone( 'bxGenesis/provisioners',  'bxGenesis/provisioners', vcMode)    


    gitCloneBase( 'unisos-pip',  'unisos-pip/base', vcMode)
    gitClone( 'unisos-pip/overview',  'unisos-pip/overview', vcMode)    

    gitClone( 'unisos-pip/namespace',  'unisos-pip/namespace', vcMode)

    gitClone( 'unisos-pip/common',  'unisos-pip/common', vcMode)

    gitClone( 'unisos-pip/ucf',  'unisos-pip/ucf', vcMode)

    gitClone( 'unisos-pip/icm',  'unisos-pip/icm', vcMode)

    gitClone( 'unisos-pip/icmExamples',  'unisos-pip/icmExamples', vcMode)

    gitClone( 'unisos-pip/x822Msg',  'unisos-pip/x822Msg', vcMode)

    gitClone( 'unisos-pip/utils',  'unisos-pip/utils', vcMode)

    gitClone( 'unisos-pip/githubApi',  'unisos-pip/githubApi', vcMode)        
    
    gitCloneBase( 'bisos-pip',  'bisos-pip/base', vcMode)
    gitClone( 'bisos-pip/overview',  'bisos-pip/overview', vcMode)    

    gitClone( 'bisos-pip/namespace',  'bisos-pip/namespace', vcMode)

    gitClone( 'bisos-pip/mmwsIcm',  'bisos-pip/mmwsIcm', vcMode)

    gitClone( 'bisos-pip/bootstrap',  'bisos-pip/bootstrap', vcMode)

    # /bisos/git/auth/bxRepos/bisos-pip/bootstrap/dev/bisos
    gitCloneBase( 'bisos-pip/bootstrap/dev/bisos/bootstrap-vagrants',  'bxGenesis/vagrants', vcMode)    

    gitClone( 'bisos-pip/bx-bases',  'bisos-pip/bx-bases', vcMode)

    gitClone( 'bisos-pip/common',  'bisos-pip/common', vcMode)

    gitClone( 'bisos-pip/examples',  'bisos-pip/examples', vcMode)

    gitClone( 'bisos-pip/gossonot',  'bisos-pip/gossonot', vcMode)

    gitClone( 'bisos-pip/lcnt',  'bisos-pip/lcnt', vcMode)

    gitClone( 'bisos-pip/currents',  'bisos-pip/currents', vcMode)

    gitClone( 'bisos-pip/platform',  'bisos-pip/platform', vcMode)

    gitClone( 'bisos-pip/things',  'bisos-pip/things', vcMode)

    gitClone( 'bisos-pip/marme',  'bisos-pip/marme', vcMode)

    gitClone( 'bisos-pip/core',  'bisos-pip/core', vcMode)

    gitClone( 'bisos-pip/coreDist',  'bisos-pip/coreDist', vcMode)

    gitClone( 'bisos-pip/full',  'bisos-pip/full', vcMode)


    gitCloneBase( 'blee-pip',  'blee-pip/base', vcMode)
    gitClone( 'blee-pip/overview',  'blee-pip/overview', vcMode)    

    gitClone( 'blee-pip/namespace',  'blee-pip/namespace', vcMode)

    gitClone( 'blee-pip/elispDist',  'blee-pip/elispDist', vcMode)

    gitClone( 'blee-pip/icmPlayer',  'blee-pip/icmPlayer', vcMode)

    
    gitCloneBase( 'roPerf-pip',  'roPerf-pip/base', vcMode)
    gitClone( 'roPerf-pip/overview',  'roPerf-pip/overview', vcMode)    

    gitClone( 'roPerf-pip/namespace',  'roPerf-pip/namespace', vcMode)

    gitClone( 'roPerf-pip/bearerTokenExample',  'roPerf-pip/bearerTokenExample', vcMode)

    
    gitCloneBase( 'efficientProtocols',  'efficientProtocols/base', vcMode)
    gitClone( 'efficientProtocols/overview',  'efficientProtocols/overview', vcMode)    

    gitClone( 'efficientProtocols/OCP',  'efficientProtocols/OCP', vcMode)        
    gitClone( 'efficientProtocols/ESRO',  'efficientProtocols/ESRO', vcMode)
    gitClone( 'efficientProtocols/EMSD',  'efficientProtocols/EMSD', vcMode)        
    
    
    return pbdDict



####+BEGIN: bx:dblock:python:func :funcName "pbdDict_extRepos" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_extRepos/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_extRepos(
    baseDir,
    vcMode=None,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bxReposBasesInstall.tex
*** See: \section{/bxRepos Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    #root = bxReposRoot_baseObtain(baseDir)
    root = baseDir
    pbdDict['/'] = bxpBaseDir.bxpObjGet_baseDir(root, '')

    if not vcMode:
        vcMode = "anon"
    
    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpBaseDir.bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpBaseDir.bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        # print("AAAA Entering command {createCmnd}".format(createCmnd=createCmnd))
        pbdDict[dstPathRel] = bxpBaseDir.BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )

    #
    # NOTYET, Change the name to: gitMapClone,
    # Make it be
    #    gitCloneBase(locPathRel, remGitRepoPath, vcMode)
    #  A single gitMapClone can then do both gitClone() and gitCloneBase()
    #  If basename of locPathRel and remGitRepoPath are the same, we then have gitClone()
    #  Otherwise, gitCloneBase() which includes the move.
    #
        
    def gitClone(dstPathRel, gitRepoPath, vcMode):
        """ repoName of remGitRepoPath, is same as basename of dstPathRel"""
        pathComps = os.path.split(dstPathRel)
        baseDir = pathComps[0]
        # repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            #               "cd {root}/{baseDir} && git clone git@github.com:{gitRepoPath}.git"
            command(
                dstPathRel,
                "cd {root}/{baseDir} && git clone git://github.com/{gitRepoPath}.git"
                .format(root=root, baseDir=baseDir, gitRepoPath=gitRepoPath)
            )
        elif vcMode == "auth":
            command(  dstPathRel,
              "cd {root}/{baseDir} && git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
              .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            )
        else:
            icm.EH_problem_usageError("")


    def gitCloneBase(locPathRel, remGitRepoPath, vcMode):
        locBasenameRel = os.path.basename(locPathRel)
        locDirnameRel =  os.path.dirname(locPathRel)
        
        locDirnameFull = os.path.join(root, locDirnameRel)
        
        repoName = os.path.basename(remGitRepoPath)

        # This is the before the move to locPathRel location
        locDirnamePlusRepoRel = os.path.join(locDirnameRel, repoName)        
        
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            # "cd {locDirnameFull} && git clone git@github.com:{remGitRepoPath}.git"
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            command(  locPathRel,
                      "cd {locDirnameFull} && git clone git://github.com/{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                      .format(locDirnameFull=locDirnameFull, remGitRepoPath=remGitRepoPath, repoName=repoName, locBasenameRel=locBasenameRel)
            )
            
        elif vcMode == "auth":
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            command(  locDirnamePlusRepoRel,
              "cd {locDirnameFull} && git clone https://{gitUserName}:{gitPasswd}@github.com/{remGitRepoPath} && mv {repoName} {locBasenameRel}"
              .format(
                  locDirnameFull=locDirnameFull,
                  gitUserName=gitUserName,
                  gitPasswd=gitPasswd,
                  remGitRepoPath=remGitRepoPath,
                  repoName=repoName,
                  locBasenameRel=locBasenameRel
              )
            )
            
        else:
            icm.EH_problem_usageError("")
            
            
    #
    # NOTYET, this is a hack for now. To Be replaced by bue.credentials
    #

    with open('/acct/employee/lsipusr/gitUserName', 'r') as myfile:
        gitUserName=myfile.read().replace('\n', '')        

    with open('/acct/employee/lsipusr/gitPasswd', 'r') as myfile:
        gitPasswd=myfile.read().replace('\n', '')        

    #
    # NOTYET, the model of specifying one command here is wrong.
    # We should be dealing with abstract directory bases, where
    # each directory base has a create and verify method.
    # Things like update and clean, etc should then be driven
    # with the fto (File Tree Objects).
    #
    # So, gitCloneBase should be renamed gitReposCollectionBase and gitRepoBase
    #

    directory('emacs')
    
    gitClone(
        'emacs/emacs-application-framework',
        'manateelazycat/emacs-application-framework',
        vcMode
    )
    gitClone(
        'emacs/frame-cmds',
        'emacsmirror/frame-cmds',
        vcMode
    )
    gitClone(
        'emacs/frame-fns',
        'emacsmirror/frame-fns',
        vcMode
    )
    gitClone(
        'emacs/thumb-frm',
        'emacsmirror/thumb-frm',
        vcMode
    )

    
    
    return pbdDict



####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxReposRootObsoleted" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bxReposRootObsoleted/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxReposRootObsoleted(
    baseDir,
    vcMode=None,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bxReposBasesInstall.tex
*** See: \section{/bxRepos Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    root = bxReposRoot_baseObtain(baseDir)
    pbdDict['/'] = bxpBaseDir.bxpObjGet_baseDir(root, '')

    if not vcMode:
        vcMode = "anon"
    
    
    def fullDestPathGet(dstPathRel):
        return( os.path.join(
            root, dstPathRel,
        ))

    def directory(pathRel):
        pbdDict[pathRel] = bxpBaseDir.bxpObjGet_baseDir(root, pathRel)

    def symLink(dstPathRel, srcPath, srcPathType='internal'):
        pbdDict[dstPathRel] = bxpBaseDir.bxpObjGet_symLink(root, dstPathRel, srcPath, srcPathType=srcPathType)

    def command(dstPathRel, createCmnd):
        pbdDict[dstPathRel] = bxpBaseDir.BxpBaseDir_Command(
            destPathRoot=root,
            destPathRel=dstPathRel,
            createCommand=createCmnd,
        )

    def gitClone(dstPathRel, vcMode):
        pathComps = os.path.split(dstPathRel)
        baseDir = pathComps[0]
        repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            command(  dstPathRel,
              "cd {root}/{baseDir}; git clone git@github.com:{dstPathRel}.git"
              .format(root=root, baseDir=baseDir, dstPathRel=dstPathRel)
            )
        elif vcMode == "auth":
            command(  dstPathRel,
              "cd {root}/{baseDir}; git clone https://{gitUserName}:{gitPasswd}@github.com/{dstPathRel}"
              .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, dstPathRel=dstPathRel)
            )
        else:
            icm.EH_problem_usageError("")
            

    #
    # NOTYET, this is a hack for now. To Be replaced by bue.credentials
    #

    with open('/acct/employee/lsipusr/gitUserName', 'r') as myfile:
        gitUserName=myfile.read().replace('\n', '')        

    with open('/acct/employee/lsipusr/gitPasswd', 'r') as myfile:
        gitPasswd=myfile.read().replace('\n', '')        
        

    directory('ByStar')
    # command(  'ByStar/overview',
    #           "cd {root}/ByStar; git clone https://{gitUserName}:{gitPasswd}@github.com/ByStar/overview"
    #           .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    gitClone('ByStar/overview', vcMode)

    directory('unisos')
    command(  'unisos/overview',
              "cd {root}/unisos; git clone https://{gitUserName}:{gitPasswd}@github.com/bx-unisos/overview"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))

    directory('bisos')
    command(  'bisos/overview',
              "cd {root}/bisos; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos/overview"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    
    directory('blee')
    command(  'blee/overview',
              "cd {root}/blee; git clone https://{gitUserName}:{gitPasswd}@github.com/bx-blee/overview"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))


    directory('unisos-pip')
    command(  'unisos-pip/overview',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/overview"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'unisos-pip/namespace',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/namespace"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'unisos-pip/common',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/common"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'unisos-pip/ucf',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/ucf"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'unisos-pip/icm',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/icm"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'unisos-pip/icmExamples',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/icmExamples"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'unisos-pip/x822Msg',
              "cd {root}/unisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/unisos-pip/x822Msg"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))

    
    directory('bisos-pip')
    command(  'bisos-pip/overview',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/overview"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/namespace',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/namespace"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/mmwsIcm',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/mmwsIcm"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/bootstrap',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/bootstrap"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/bx-bases',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/bx-bases"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/common',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/common"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/examples',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/examples"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/gossonot',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/gossonot"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/lcnt',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/lcnt"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/currents',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/currents"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/platform',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/platform"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/things',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/things"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/marme',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/marme"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/core',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/core"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/coreDist',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/coreDist"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'bisos-pip/full',
              "cd {root}/bisos-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/bisos-pip/full"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))


    directory('blee-pip')
    command(  'blee-pip/overview',
              "cd {root}/blee-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/blee-pip/overview"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'blee-pip/namespace',
              "cd {root}/blee-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/blee-pip/namespace"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'blee-pip/elispDist',
              "cd {root}/blee-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/blee-pip/elispDist"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))
    command(  'blee-pip/icmPlayer',
              "cd {root}/blee-pip; git clone https://{gitUserName}:{gitPasswd}@github.com/blee-pip/icmPlayer"
              .format(root=root, gitUserName=gitUserName, gitPasswd=gitPasswd))


    
    
    return pbdDict




####+BEGIN: bx:dblock:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bxReposRoot_baseObtain" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bxReposRoot_baseObtain/ retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bxReposRoot_baseObtain(
    baseDir,
):
####+END:
    outcome = bxReposRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)    

    return outcome.results

    
####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "bxReposRootGet" :parsMand "" :parsOpt "baseDir" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /bxReposRootGet/ parsMand= parsOpt=baseDir argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bxReposRootGet(icm.Cmnd):
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

            #retVal = bxReposlatformConfig.rootDir_bxRepos_fpObtain(None)
            retVal = "/bisos/git/anon"
            break

            # The Rest Is Now Obsolete

            userFileName = bxReposRootBaseDirPtrUserFile_obtain()
            if os.path.isfile(
                    userFileName
            ):
                with open(userFileName, 'r') as myfile:
                    data=myfile.read().replace('\n', '')
                    retVal = data
                    break

            sysFileName = bxReposRootBaseDirPtrSysFile_obtain()
            if os.path.isfile(
                    sysFileName
            ):
                with open(sysFileName, 'r') as myfile:
                    data=myfile.read().replace('\n', '')
                    retVal = data
                    break

            # Default BxRepos Root Directory
            defaultBxRootDir = bxReposRootBaseDirDefault_obtain()
            if os.path.isdir(defaultBxRootDir):
                retVal = defaultBxRootDir
                break

            icm.EH_problem_usageError("Missing /bxRepos and no /etc/bxReposRoot")            
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
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Based ~/.bxReposRoot or /etc/bxReposRoot decide on meta.
   ** if --baseDir Was specified, it is returned or 
   ** If ~/.bxReposRoot exists, its content is returned
   ** If /etc/bxReposRoot exists, its content is returned
   ** If /bxRepos exists, "/bxRepos" is returned
"""


####+BEGIN: bx:dblock:python:subSection :title "ICM Each Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ICM Each Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
            
            
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdShow" :parsMand "" :parsOpt "baseDir pbdName" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /pbdShow/ parsMand= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
** for each arg, output bxRepos parameters.
"""
        icm.ANN_write("{}".format(baseDir))

        if not pbdName:
            pbdName = 'bxReposRoot'

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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /pbdVerify/ parsMand= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
            pbdName = 'bxReposRoot'

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
 
####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdUpdate" :parsMand "" :parsOpt "baseDir pbdName vcMode" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /pbdUpdate/ parsMand= parsOpt=baseDir pbdName vcMode argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class pbdUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', 'vcMode', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        baseDir=None,         # or Cmnd-Input
        pbdName=None,         # or Cmnd-Input
        vcMode=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, 'vcMode': vcMode, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        baseDir = callParamsDict['baseDir']
        pbdName = callParamsDict['pbdName']
        vcMode = callParamsDict['vcMode']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        icm.ANN_here("baseDir={baseDir} -- pbdName={pbdName}".format(baseDir=baseDir, pbdName=pbdName))

        if not pbdName:
            #pbdName = 'bxReposRoot'
            pbdName = 'bxReposRoot'

        if not vcMode:
            vcName = 'anon'
            
        if baseDir:
            pbdDict = eval("""pbdDict_{pbdName}("{baseDir}", vcMode="{vcMode}")""".format(
                pbdName=pbdName, baseDir=baseDir, vcMode=vcMode))
        else:
            # Do Not Quote None in eval
            pbdDict = eval("""pbdDict_{pbdName}({baseDir}, vcMode="{vcMode}")""".format(
                pbdName=pbdName, baseDir=baseDir, vcMode=vcMode))

        def procEach(pbdItem):
            #icm.ANN_here("pbdItem={pbdItem}".format(pbdItem=pbdItem))
            # NOTYET, Capture keyerror and report it as bad input.
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
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** For each arg, update each to what has been specified.
"""


        
####+BEGIN: bx:dblock:python:subSection :title "ICM Multiple pbdUpdates Based On Platform Defaults Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ICM Multiple pbdUpdates Based On Platform Defaults Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdRootsForPlatform" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /pbdRootsForPlatform/ parsMand= parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
            
            bxReposlatformConfigBase = bxReposlatformThis.pkgBase_configDir()
            
            if pbdName == "bxReposRoot":
                rootDirName = bxReposlatformConfig.rootDir_bxRepos_fpObtain(bxReposlatformConfigBase)
                
            elif pbdName == "deRunRoot":
                rootDirName = bxReposlatformConfig.rootDir_bxo_fpObtain(bxReposlatformConfigBase)
                
            elif pbdName == "bxoRoot":
                rootDirName = bxReposlatformConfig.rootDir_deRun_fpObtain(bxReposlatformConfigBase)
            else:
                icm.EH_problem_usageError("")

            return rootDirName

        bxReposUserName = bxReposUserName_obtain()
        bxReposGroupName = bxReposGroupName_obtain()

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
            #shutil.chown(rootDir, bxReposUserName, bxReposGroupName)
            uid = pwd.getpwnam(bxReposUserName).pw_uid
            gid = grp.getgrnam(bxReposGroupName).gr_gid
            os.chown(rootDir, uid, gid)

            os.chmod(rootDir, 0775)            

            outcome = icm.subProc_bash("""\
ls -ld  {rootDir}"""
                                       .format(rootDir=rootDir)
            ).log()
            if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
            

        #icm.ANN_here("{}".format(bxReposUserName))

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
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
            argChoices=['all', 'bxReposRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "pbdUpdateForPlatform" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /pbdUpdateForPlatform/ parsMand= parsOpt= argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
            
            bxReposlatformConfigBase = bxReposlatformThis.pkgBase_configDir()
            
            if pbdName == "bxReposRoot":
                rootDirName = bxReposlatformConfig.rootDir_bxRepos_fpObtain(bxReposlatformConfigBase)
                
            elif pbdName == "bxoRoot":
                rootDirName = bxReposlatformConfig.rootDir_bxo_fpObtain(bxReposlatformConfigBase)
                
            elif pbdName == "deRunRoot":
                rootDirName = bxReposlatformConfig.rootDir_deRun_fpObtain(bxReposlatformConfigBase)
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
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
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
            argChoices=['all', 'bxReposRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict
    

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

    

####+BEGIN: bx:dblock:python:subSection :title "Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
