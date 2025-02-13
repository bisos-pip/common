# -*- coding: utf-8 -*-
"""\
*    *[Summary]* ::  A /library/ with ICM Cmnds to support BxRepos bases (/bisos/vc/git) creation facilities
** if anon git clone git://github.com/SomeUser/SomeRepo.git if auth git clone git@github.com:UserName/OtherRepo.git
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft ""
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

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['baseDirBxRepos'], }
csInfo['version'] = '202408043723'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'baseDirBxRepos-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/dev/null"
####+END:

####+BEGIN: bx:cs:python:topControls 
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


####+BEGIN: bx:cs:python:section :title "ContentsList"
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

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:


####+BEGINNOT: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
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

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bxReposBaseDir_libOverview" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxReposBaseDir_libOverview>>  =verify= argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxReposBaseDir_libOverview(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:

        moduleDescription="""
*       [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
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


####+BEGIN: bx:dblock:python:func :funcName "bxReposRootBaseDirPtrUserFile_obtain" :comment "~/.bxReposRoot" :funcType "obtain" :retType "str" :argsList "" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-obtain   [[elisp:(outline-show-subtree+toggle)][||]] /bxReposRootBaseDirPtrUserFile_obtain/ =~/.bxReposRoot= retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def bxReposRootBaseDirPtrUserFile_obtain():
####+END:
    return os.path.abspath(
        os.path.expanduser(
            "~/.bxReposRoot"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bxReposRootBaseDirDefault_obtain" :comment "/bxRepos" :funcType "obtain" :retType "str" :argsList "" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-obtain   [[elisp:(outline-show-subtree+toggle)][||]] /bxReposRootBaseDirDefault_obtain/ =/bxRepos= retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
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


####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "csParams"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-ParSpec   :: /commonParamsSpecify/ retType= argsList=(csParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    csParams,
):
####+END:
    csParams.parDictAdd(
        parName='baseDir',
        parDescription="Bx Platform Base Dir",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--baseDir',
    )

    csParams.parDictAdd(
        parName='gitLabel',
        parDescription="Corresponding to an entry in ~/.ssh/config",
        parDataType=None,
        parDefault="github.com",
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--gitLabel',
    )
    
    csParams.parDictAdd(
        parName='pbdName',
        parDescription="Platform BaseDirs Dict Name",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--pbdName',
    )

    csParams.parDictAdd(
        parName='vcMode',
        parDescription="VC (git) Mode -- auth or anon",
        parDataType=None,
        parDefault=None,
        parChoices=["auth", "anon",],
        parScope=cs.CmndParamScope.TargetParam,
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
    cs.examples.menuChapter('* =BxRepos BaseDir=  BxRepos Platform Base Dirs')

    cmndName = "bxReposRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "bxReposRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['baseDir'] = '/tmp/bxBase'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cs.examples.execInsert(execLine="""cat {}""".format(bxReposRootBaseDirPtrUserFile_obtain()),)
    #cs.examples.execInsert(execLine="""cat {}""".format(bxReposRootBaseDirPtrSysFile_obtain()),)
    cs.examples.execInsert(execLine="""ls -l {}""".format(bxReposRootBaseDirDefault_obtain(),))
    
    # cs.examples.execInsert(execLine="""ls -l /bisos/vc/git/bxRepos/*""")   
    # cs.examples.execInsert(execLine="""sudo mkdir -p /bisos/vc/git/bxRepos/auth; sudo chown {}:{} /bisos/vc/git/bxRepos/auth"""
    #                      .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))
    # cs.examples.execInsert(execLine="""sudo mkdir -p /bisos/vc/git/bxRepos/anon; sudo chown {}:{} /bisos/vc/git/bxRepos/anon"""
    #                      .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))

    #cs.examples.execInsert(execLine="""ls -l /bisos/git/auth/bxRepos/*""")   
    cs.examples.execInsert(execLine="""sudo mkdir -p /bisos/git/auth; sudo chown {}:{} /bisos/git/auth"""
                         .format(bxReposUserName_obtain(), bxReposGroupName_obtain()))
    cs.examples.execInsert(execLine="""sudo mkdir -p /bisos/git/anon; sudo chown {}:{} /bisos/git/anon"""
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

    cs.examples.menuChapter('* =BxRepos BaseDir=  Module Description,Usage,Status Information')
    
    menuLine = """"""
    cs.cmndExampleMenuItem(menuLine, icmName="bx-bases", verbosity='none')


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
    def menuItem(): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    #bxRootBase = bxReposRoot_baseObtain(None)

    examples_bxReposBaseDirsCommon()
    
    cs.examples.menuChapter('* =Module=  Overview (desc, usage, status)')    
   
    cmndName = "overview_bxReposBaseDir" ; cmndArgs = "moduleDescription moduleUsage moduleStatus" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cs.examples.menuChapter(' =BxReposCollection DirBases=  *pbdShow/pbdVerify/pbdUpdate Of Relevant PBDs*')    

    cs.examples.menuSection(' =BxReposCollection DirBases=  *pbdVerify*')            

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/anon';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'anon'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/auth';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'auth'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
   
    cs.examples.menuSection(' =BxReposCollection DirBases=  *pbdUpdate*')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/anon';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'anon'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/auth';
    cps['pbdName'] = 'bxReposCollection' ; cps['vcMode'] = 'auth' ;
    cps['gitLabel'] = 'github.com'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    
    cs.examples.menuChapter(' =BxRepos DirBases=  *pbdShow/pbdVerify/pbdUpdate Of Relevant PBDs*')    

    # cs.examples.menuSection(' =BxRepos DirBases=  *pbdShow*')        
    # cmndName = "pbdShow" ; cmndArgs = "/ blee-pip" ;
    # cps = collections.OrderedDict() ;
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdShow" ; cmndArgs = "/ blee-pip" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bxReposRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bxReposRoot'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cs.examples.menuSection(' =BxRepos DirBases=  *pbdVerify*')            
    
    cmndName = "pbdVerify" ; cmndArgs = "/ blee-pip" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'; cps['pbdName'] = 'bxReposRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'; cps['pbdName'] = 'bxReposRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cs.examples.menuSection(' =BxRepos DirBases=  *pbdUpdate*')
    
    cmndName = "pbdUpdate" ; cmndArgs = "/ blee-pip" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'; cps['pbdName'] = 'bxReposRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/anon/bxRepos';
    cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'anon' ; cps['gitLabel'] = 'github.com'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/git/auth/bxRepos';
    cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'auth' ; cps['gitLabel'] = 'github.com'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict(); cps['baseDir'] = '/bisos/git/anon/ext';
    cps['pbdName'] = 'extRepos' ; cps['vcMode'] = 'anon' ; cps['gitLabel'] = 'github.com'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    
    # cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/vc/git/bxRepos/anon';
    # cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'anon'
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos/vc/git/bxRepos/auth';
    # cps['pbdName'] = 'bxReposRoot' ; cps['vcMode'] = 'auth'
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    
    cs.examples.menuSection(' *bx-platformInfoManage.py -- Specifiy Platform Defaults*')

    execLineEx("""bx-platformInfoManage.py""")

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ;
    cps=cpsInit() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='none',
                         comment='none', icmWrapper=None, icmName="bx-platformInfoManage.py")

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /" ;
    cps=cpsInit() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                         comment='none', icmWrapper=None, icmName="bx-platformInfoManage.py")

    cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy /tmp" ;
    cps=cpsInit() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                         comment='none', icmWrapper="echo", icmName="bx-platformInfoManage.py")
 
    cs.examples.menuSection(' =BxRepos DirBases Creation/Ownership=  *pbdRootsForPlatform*')   
    
    cmndName = "pbdRootsForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    cmndName = "pbdRootsForPlatform" ; cmndArgs = "bxReposRoot" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    cs.examples.menuSection(' =BxRepos DirBases Update=  *pbdUpdateForPlatform*')   

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "bxReposRoot" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")
    
    # pbdList has been OBSOLETED
    # cs.examples.menuChapter(' =BxRepos DirBases=  *pbdShow/pbdVerify/pbdUpdate*')    

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bxRepos" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BXREPOS'
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bxRepos" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] =  bxRootBase
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
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


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxReposCollection" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None gitLabel='github.com'" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bxReposCollection/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None gitLabel='github.com')  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxReposCollection(
    baseDir,
    vcMode=None,
    gitLabel='github.com',
):
####+END:
    """
** TODO PROBLEM -- NOTYET, still uses https git auth -- 
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
        """ repoName of remGitRepoPath, is same as basename of dstPathRel"""
        pathComps = os.path.split(dstPathRel)
        baseDir = pathComps[0]
        # repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            #               "cd {root}/{baseDir} && git clone git@github.com:{gitRepoPath}.git"
            command(
                dstPathRel,
                "cd {root}/{baseDir} && git clone git://{gitLabel}/{gitRepoPath}.git"
                .format(
                    root=root,
                    baseDir=baseDir,
                    gitLabel=gitLabel,
                    gitRepoPath=gitRepoPath,
                )
            )
        elif vcMode == "auth":
            # command(  dstPathRel,
            #   "cd {root}/{baseDir} && git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
            #   .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            # )
            command(
                dstPathRel,
                "cd {root}/{baseDir} && git clone git@{gitLabel}:{gitRepoPath}.git"
                .format(
                    root=root,
                    baseDir=baseDir,
                    gitLabel=gitLabel,
                    gitRepoPath=gitRepoPath,
                )
            )           
        else:
            b_io.eh.problem_usageError("")

    def gitCloneBase(locPathRel, remGitRepoPath, vcMode):
        locBasenameRel = os.path.basename(locPathRel)
        locDirnameRel = os.path.dirname(locPathRel)
        
        locDirnameFull = os.path.join(root, locDirnameRel)
        
        repoName = os.path.basename(remGitRepoPath)

        # This is the before the move to locPathRel location
        #locDirnamePlusRepoRel = os.path.join(locDirnameRel, repoName)        
        
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            # "cd {locDirnameFull} && git clone git@github.com:{remGitRepoPath}.git"
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            command(
                locPathRel,
                "cd {locDirnameFull} && git clone git://{gitLabel}/{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                .format(
                    locDirnameFull=locDirnameFull,
                    remGitRepoPath=remGitRepoPath,
                    gitLabel=gitLabel,
                    repoName=repoName,
                    locBasenameRel=locBasenameRel,
                )
            )
            
        elif vcMode == "auth":
            #
            # Note: You can not use multiple command() below.
            # The last command's info gets appended to a list and it is onth that which is executed.
            #
            # command(  locDirnamePlusRepoRel,
            #   "cd {locDirnameFull} && git clone https://{gitUserName}:{gitPasswd}@github.com/{remGitRepoPath} && mv {repoName} {locBasenameRel}"
            #   .format(
            #       locDirnameFull=locDirnameFull,
            #       gitUserName=gitUserName,
            #       gitPasswd=gitPasswd,
            #       remGitRepoPath=remGitRepoPath,
            #       repoName=repoName,
            #       locBasenameRel=locBasenameRel
            #   )
            # )
            command(locPathRel,
                    "cd {locDirnameFull} && git clone git@{gitLabel}:{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                    .format(
                        locDirnameFull=locDirnameFull,
                        remGitRepoPath=remGitRepoPath,
                        gitLabel=gitLabel,                        
                        repoName=repoName,
                        locBasenameRel=locBasenameRel
                    )
            )
            
        else:
            b_io.eh.problem_usageError("")
            
    #command('bxReposBasedir', "mkdir -p {root}".format(root=root))
    
    gitCloneBase('bxRepos', 'ByStar/bxReposBase', vcMode)    
    
    return pbdDict



####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bxReposRoot" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None gitLabel='github.com'" :deco ""
"""
1*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bxReposRoot/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None gitLabel='github.com')  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bxReposRoot(
    baseDir,
    vcMode=None,
    gitLabel='github.com',
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
        # repoName = pathComps[1]
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            #               "cd {root}/{baseDir} && git clone git@github.com:{gitRepoPath}.git"
            command(
                dstPathRel,
                "cd {root}/{baseDir} && git clone git://{gitLabel}/{gitRepoPath}.git"
                .format(
                    root=root,
                    baseDir=baseDir,
                    gitLabel=gitLabel,
                    gitRepoPath=gitRepoPath,
                )
            )
        elif vcMode == "auth":
            # command(  dstPathRel,
            #   "cd {root}/{baseDir} && git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
            #   .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            # )
            command(
                dstPathRel,
                "cd {root}/{baseDir} && git clone git@{gitLabel}:{gitRepoPath}.git"
                .format(
                    root=root,
                    baseDir=baseDir,
                    gitLabel=gitLabel,                    
                    gitRepoPath=gitRepoPath,
                )
            )           
        else:
            b_io.eh.problem_usageError("")

    def gitCloneBase(locPathRel, remGitRepoPath, vcMode):
        locBasenameRel = os.path.basename(locPathRel)
        locDirnameRel = os.path.dirname(locPathRel)
        
        locDirnameFull = os.path.join(root, locDirnameRel)
        
        repoName = os.path.basename(remGitRepoPath)

        # This is the before the move to locPathRel location
        #locDirnamePlusRepoRel = os.path.join(locDirnameRel, repoName)        
        
        if vcMode == "anon":
            # git clone git://github.com/SomeUser/SomeRepo.git
            # "cd {locDirnameFull} && git clone git@github.com:{remGitRepoPath}.git"
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            command(
                locPathRel,
                "cd {locDirnameFull} && git clone git://{gitLabel}/{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                .format(
                    locDirnameFull=locDirnameFull,
                    gitLabel=gitLabel,                                        
                    remGitRepoPath=remGitRepoPath,
                    repoName=repoName,
                    locBasenameRel=locBasenameRel,
                )
            )
            
        elif vcMode == "auth":
            #
            # Note: You can not use multiple command() below.
            # The last command's info gets appended to a list and it is onth that which is executed.
            #
            # command(  locDirnamePlusRepoRel,
            #   "cd {locDirnameFull} && git clone https://{gitUserName}:{gitPasswd}@github.com/{remGitRepoPath} && mv {repoName} {locBasenameRel}"
            #   .format(
            #       locDirnameFull=locDirnameFull,
            #       gitUserName=gitUserName,
            #       gitPasswd=gitPasswd,
            #       remGitRepoPath=remGitRepoPath,
            #       repoName=repoName,
            #       locBasenameRel=locBasenameRel
            #   )
            # )
            command(locPathRel,
                    "cd {locDirnameFull} && git clone git@{gitLabel}:{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                    .format(
                        locDirnameFull=locDirnameFull,
                        gitLabel=gitLabel,                                                                
                        remGitRepoPath=remGitRepoPath,
                        repoName=repoName,
                        locBasenameRel=locBasenameRel
                    )
            )
            
        else:
            b_io.eh.problem_usageError("")
            
            
    #
    # NOTYET, this is a hack for now. To Be replaced by bue.credentials
    #

    # with open('/acct/employee/lsipusr/gitUserName', 'r') as myfile:
    #     gitUserName=myfile.read().replace('\n', '')        

    # with open('/acct/employee/lsipusr/gitPasswd', 'r') as myfile:
    #     gitPasswd=myfile.read().replace('\n', '')        

    #
    # NOTYET, the model of specifying one command here is wrong.
    # We should be dealing with abstract directory bases, where
    # each directory base has a create and verify method.
    # Things like update and clean, etc should then be driven
    # with the fto (File Tree Objects).
    #
    # So, gitCloneBase should be renamed gitReposCollectionBase and gitRepoBase
    #

    gitCloneBase('ByStar', 'ByStar/base', vcMode)    
    gitClone('ByStar/overview', 'ByStar/overview', vcMode)

    gitCloneBase('mohsenBanan', 'ByStar/mohsenBananBase', vcMode)    
    gitClone('mohsenBanan/ReposOverview', 'mohsenBanan/ReposOverview', vcMode)
    gitClone('mohsenBanan/StartHere', 'mohsenBanan/StartHere', vcMode)        
  
    gitCloneBase('unisos', 'bx-unisos/base', vcMode)
    gitClone('unisos/overview', 'bx-unisos/overview', vcMode)

    gitCloneBase('bisos', 'bisos/base', vcMode)
    gitClone('bisos/overview',  'bisos/overview', vcMode)
    gitClone('bisos/bsip4',  'bisos/bsip4', vcMode)
    gitClone('bisos/bpip1',  'bisos/bpip1', vcMode)
    gitClone('bisos/comeega',  'bisos/comeega', vcMode)
    gitClone('bisos/gatherer',  'bisos/gatherer', vcMode)
    gitClone('bisos/defaults',  'bisos/defaults', vcMode)
    # gitClone('bisos/bxio',  'bisos/bxio', vcMode)
    # gitClone('bisos/bxso',  'bisos/bxso', vcMode)
    gitClone('bisos/asc',  'bisos/asc', vcMode)    
    gitClone('bisos/apps',  'bisos/apps', vcMode)
    gitClone('bisos/lcnt',  'bisos/lcnt', vcMode)
    gitClone('bisos/mail',  'bisos/mail', vcMode)
    gitClone('bisos/pals',  'bisos/pals', vcMode)
    gitClone('bisos/dev',  'bisos/dev', vcMode)
    gitClone('bisos/admin',  'bisos/admin', vcMode)

    gitCloneBase('bxObjects', 'bxObjects/base', vcMode)
    gitClone('bxObjects/overview',  'bxObjects/overview', vcMode)
    gitClone('bxObjects/a-ig-ub-cur-small',  'bxObjects/a-ig-ub-cur-small', vcMode)    
    
    gitCloneBase('blee', 'bx-blee/base',  vcMode)
    gitClone('blee/overview', 'bx-blee/overview', vcMode)
    gitClone('blee/env', 'bx-blee/env', vcMode)
    gitClone('blee/envsShare', 'bx-blee/envsShare', vcMode)
    gitClone('blee/env2', 'bx-blee/env2', vcMode)
    gitClone('blee/env3', 'bx-blee/env3', vcMode)
    #
    # Doom Bases
    #
    gitClone('blee/doom-emacs-framework', 'bx-blee/doom-emacs-framework', vcMode)
    # NOTYET defunct doom-emacs-init
    gitClone('blee/doom-emacs-init', 'bx-blee/doom-emacs-init', vcMode)
    # NOTYET defunct doom-blee-init
    gitClone('blee/doom-blee-init', 'bx-blee/doom-blee-init', vcMode)
    gitClone('blee/doom-base', 'bx-blee/doom-base', vcMode)
    gitClone('blee/doom-blee-base', 'bx-blee/doom-blee-base', vcMode)
    gitClone('blee/doom-base-emacs', 'bx-blee/doom-base-emacs', vcMode)
    gitClone('blee/doom-base-blee2', 'bx-blee/doom-base-blee2', vcMode)
    gitClone('blee/doom-base-blee3', 'bx-blee/doom-base-blee3', vcMode)
    #
    # Blee Packages
    #
    gitClone('blee/blee-dblocks', 'bx-blee/blee-dblocks', vcMode)
    gitClone('blee/blee-libs', 'bx-blee/blee-libs', vcMode)
    gitClone('blee/blee-menus', 'bx-blee/blee-menus', vcMode)
    gitClone('blee/comeega', 'bx-blee/comeega', vcMode)
    gitClone('blee/comment-block', 'bx-blee/comment-block', vcMode)
    gitClone('blee/poly-dblock', 'bx-blee/poly-dblock', vcMode)
    gitClone('blee/pkgs-profile', 'bx-blee/pkgs-profile', vcMode)
    gitClone('blee/blee3-pkgs-profile', 'bx-blee/blee3-pkgs-profile', vcMode)
    # gitClone('blee/mcdt', 'bx-blee/mcdt', vcMode)
    gitClone('blee/mtdt', 'bx-blee/mtdt', vcMode)
    gitClone('blee/mtdt-mailing', 'bx-blee/mtdt-mailing', vcMode)
    gitClone('blee/mtdt-distribution', 'bx-blee/mtdt-distribution', vcMode)
    gitClone('blee/mtdt-names', 'bx-blee/mtdt-names', vcMode)
    gitClone('blee/mtdt-share', 'bx-blee/mtdt-share', vcMode)
    gitClone('blee/mua-abstract', 'bx-blee/mua-abstract', vcMode)
    gitClone('blee/tutorials', 'bx-blee/tutorials', vcMode)
    gitClone('blee/org-img-link', 'bx-blee/org-img-link', vcMode)
    gitClone('blee/persian-input-method', 'bx-blee/persian-input-method', vcMode)
    gitClone('blee/fshell', 'bx-blee/fshell', vcMode)
    gitClone('blee/repub_sr-speedbar', 'bx-blee/repub_sr-speedbar', vcMode)
    gitClone('blee/bidi-menu', 'bx-blee/bidi-menu', vcMode)
    gitClone('blee/bisos', 'bx-blee/bisos', vcMode)
    gitClone('blee/chatGptInv', 'bx-blee/chatGptInv', vcMode)
    #
    # Blee Misc
    #
    gitClone('blee/bbdb-filters-0.51', 'bx-blee/bbdb-filters-0.51', vcMode)
    gitClone('blee/emacs-developers-requests', 'bx-blee/emacs-developers-requests', vcMode)

    
    gitCloneBase('bxGenesis', 'bxGenesis/base', vcMode)
    gitClone('bxGenesis/overview', 'bxGenesis/overview', vcMode)
    gitClone('bxGenesis/vagrants', 'bxGenesis/vagrants', vcMode)
    gitClone('bxGenesis/vagrantBue', 'bxGenesis/vagrantBue', vcMode)    
    gitClone('bxGenesis/fbxoPkgs', 'bxGenesis/fbxoPkgs', vcMode)
    gitClone('bxGenesis/provisioners', 'bxGenesis/provisioners', vcMode)
    gitClone('bxGenesis/start', 'bxGenesis/start', vcMode)

    # gitCloneBase('unisos-pip', 'unisos-pip/base', vcMode)
    # gitClone('unisos-pip/overview', 'unisos-pip/overview', vcMode)
    # gitClone('unisos-pip/namespace', 'unisos-pip/namespace', vcMode)
    # gitClone('unisos-pip/common', 'unisos-pip/common', vcMode)
    # gitClone('unisos-pip/ucf', 'unisos-pip/ucf', vcMode)
    # gitClone('unisos-pip/icm',  'unisos-pip/icm', vcMode)
    # gitClone('unisos-pip/icmExamples',  'unisos-pip/icmExamples', vcMode)
    # gitClone('unisos-pip/x822Msg',  'unisos-pip/x822Msg', vcMode)
    # gitClone('unisos-pip/utils',  'unisos-pip/utils', vcMode)
    # gitClone('unisos-pip/githubApi',  'unisos-pip/githubApi', vcMode)
    # gitClone('unisos-pip/cryptKeyring',  'unisos-pip/cryptKeyring', vcMode)
    # gitClone('unisos-pip/gcipher',  'unisos-pip/gcipher', vcMode)
    # gitClone('unisos-pip/symCrypt',  'unisos-pip/symCrypt', vcMode)

    gitCloneBase('bisos-pip',  'bisos-pip/base', vcMode)
    gitClone('bisos-pip/overview',  'bisos-pip/overview', vcMode)    
    gitClone('bisos-pip/namespace',  'bisos-pip/namespace', vcMode)
    gitClone('bisos-pip/mmwsIcm',  'bisos-pip/mmwsIcm', vcMode)
    gitClone('bisos-pip/bootstrap',  'bisos-pip/bootstrap', vcMode)
    # /bisos/git/auth/bxRepos/bisos-pip/bootstrap/dev/bisos
    gitCloneBase(
        'bisos-pip/bootstrap/dev/bisos/bootstrap-vagrants',
        'bxGenesis/vagrants',
        vcMode
    )
    gitClone('bisos-pip/bx-bases',  'bisos-pip/bx-bases', vcMode)
    gitClone('bisos-pip/common',  'bisos-pip/common', vcMode)
    gitClone('bisos-pip/examples',  'bisos-pip/examples', vcMode)
    gitClone('bisos-pip/gossonot',  'bisos-pip/gossonot', vcMode)
    gitClone('bisos-pip/lcnt',  'bisos-pip/lcnt', vcMode)
    gitClone('bisos-pip/currents',  'bisos-pip/currents', vcMode)
    gitClone('bisos-pip/platform',  'bisos-pip/platform', vcMode)
    gitClone('bisos-pip/things',  'bisos-pip/things', vcMode)
    gitClone('bisos-pip/marme',  'bisos-pip/marme', vcMode)
    gitClone('bisos-pip/core',  'bisos-pip/core', vcMode)
    gitClone('bisos-pip/coreDist',  'bisos-pip/coreDist', vcMode)
    gitClone('bisos-pip/full',  'bisos-pip/full', vcMode)
    gitClone('bisos-pip/bashStandaloneIcmSeed',  'bisos-pip/bashStandaloneIcmSeed', vcMode)
    gitClone('bisos-pip/provision',  'bisos-pip/provision', vcMode)
    gitClone('bisos-pip/bxoGitlab',  'bisos-pip/bxoGitlab', vcMode)
    gitClone('bisos-pip/basics',  'bisos-pip/basics', vcMode)
    gitClone('bisos-pip/bpo',  'bisos-pip/bpo', vcMode)
    gitClone('bisos-pip/b',  'bisos-pip/b', vcMode)
    gitClone('bisos-pip/cntnr',  'bisos-pip/cntnr', vcMode)
    gitClone('bisos-pip/icm',  'bisos-pip/icm', vcMode)
    gitClone('bisos-pip/pals',  'bisos-pip/pals', vcMode)
    gitClone('bisos-pip/marmee',  'bisos-pip/marmee', vcMode)
    gitClone('bisos-pip/gmail-oauth2-facilities',  'bisos-pip/gmail-oauth2-facilities', vcMode)
    ### After PyCsFramework
    gitClone('bisos-pip/b',  'bisos-pip/b', vcMode)
    # gitClone('bisos-pip/bpf',  'bisos-pip/bpf', vcMode)
    gitClone('bisos-pip/binsprep',  'bisos-pip/binsprep', vcMode)
    gitClone('bisos-pip/crypt',  'bisos-pip/crypt', vcMode)
    gitClone('bisos-pip/cs',  'bisos-pip/cs', vcMode)
    gitClone('bisos-pip/debian',  'bisos-pip/debian', vcMode)
    gitClone('bisos-pip/io',  'bisos-pip/io', vcMode)
    gitClone('bisos-pip/qmail',  'bisos-pip/qmail', vcMode)
    gitClone('bisos-pip/regfps', 'bisos-pip/regfps', vcMode)
    gitClone('bisos-pip/siteRegistrars', 'bisos-pip/siteRegistrars', vcMode)
    gitClone('bisos-pip/banna', 'bisos-pip/banna', vcMode)
    # gitClone('bisos-pip/sites', 'bisos-pip/sites', vcMode)
    gitClone('bisos-pip/transit', 'bisos-pip/transit', vcMode)
    gitClone('bisos-pip/usgAcct', 'bisos-pip/usgAcct', vcMode)
    gitClone('bisos-pip/facter', 'bisos-pip/facter', vcMode)
    gitClone('bisos-pip/cmdb', 'bisos-pip/cmdb', vcMode)

    gitClone('bisos-pip/graphviz-cs', 'bisos-pip/graphviz-cs', vcMode)
    gitClone('bisos-pip/capability', 'bisos-pip/capability', vcMode)
    gitClone('bisos-pip/capSpecs', 'bisos-pip/capSpecs', vcMode)
    gitClone('bisos-pip/sbom', 'bisos-pip/sbom', vcMode)
    gitClone('bisos-pip/virsh', 'bisos-pip/virsh', vcMode)
    gitClone('bisos-pip/pycs', 'bisos-pip/pycs', vcMode)
    gitClone('bisos-pip/githubApi', 'bisos-pip/githubApi', vcMode)
    gitClone('bisos-pip/csPlayer', 'bisos-pip/csPlayer', vcMode)
    gitClone('bisos-pip/gcipher', 'bisos-pip/gcipher', vcMode)

    # gitCloneBase('blee-pip',  'blee-pip/base', vcMode)
    # gitClone('blee-pip/overview',  'blee-pip/overview', vcMode)
    # gitClone('blee-pip/namespace',  'blee-pip/namespace', vcMode)
    # gitClone('blee-pip/elispDist',  'blee-pip/elispDist', vcMode)
    # gitClone('blee-pip/icmPlayer',  'blee-pip/icmPlayer', vcMode)
    # gitClone('blee-pip/csPlayer',  'blee-pip/csPlayer', vcMode)

    # gitCloneBase('roPerf-pip',  'roPerf-pip/base', vcMode)
    # gitClone('roPerf-pip/overview',  'roPerf-pip/overview', vcMode)
    # gitClone('roPerf-pip/namespace',  'roPerf-pip/namespace', vcMode)
    # gitClone('roPerf-pip/bearerTokenExample',  'roPerf-pip/bearerTokenExample', vcMode)

    gitCloneBase('efficientProtocols',  'efficientProtocols/base', vcMode)
    gitClone('efficientProtocols/overview',  'efficientProtocols/overview', vcMode)    
    gitClone('efficientProtocols/OCP',  'efficientProtocols/OCP', vcMode)        
    gitClone('efficientProtocols/ESRO',  'efficientProtocols/ESRO', vcMode)
    gitClone('efficientProtocols/EMSD',  'efficientProtocols/EMSD', vcMode)        

    gitCloneBase('blee-binders',  'blee-binders/base', vcMode)    
    gitClone('blee-binders/overview',  'blee-binders/overview', vcMode)
    gitClone('blee-binders/bisos-core',  'blee-binders/bisos-core', vcMode)    
    # gitClone('blee-binders/bisos-model',  'blee-binders/bisos-model', vcMode)
    # gitClone('blee-binders/bisos-dev',  'blee-binders/bisos-dev', vcMode)
    gitClone('blee-binders/blee-core',  'blee-binders/blee-core', vcMode)
    # gitClone('blee-binders/blee-model',  'blee-binders/blee-model', vcMode)
    # gitClone('blee-binders/blee-dev',  'blee-binders/blee-dev', vcMode)
    gitClone('blee-binders/bxde-core',  'blee-binders/bxde-core', vcMode)
    # gitClone('blee-binders/bxde-model',  'blee-binders/bxde-model', vcMode)
    # gitClone('blee-binders/bxde-dev',  'blee-binders/bxde-dev', vcMode)
    gitClone('blee-binders/development',  'blee-binders/development', vcMode)
    gitClone('blee-binders/bisos-apps',  'blee-binders/bisos-apps', vcMode)
    gitClone('blee-binders/bisos-svcs',  'blee-binders/bisos-svcs', vcMode)
    gitClone('blee-binders/connectivity',  'blee-binders/connectivity', vcMode)
    gitClone('blee-binders/desktop',  'blee-binders/desktop', vcMode)
    gitClone('blee-binders/bisos-periphery',  'blee-binders/bisos-periphery', vcMode)
    gitClone('blee-binders/espoused',  'blee-binders/espoused', vcMode)
    gitClone('blee-binders/non-libre-halaal',  'blee-binders/non-libre-halaal', vcMode)
    gitClone('blee-binders/panelsRoot',  'blee-binders/panelsRoot', vcMode)
    gitClone('blee-binders/system-container',  'blee-binders/system-container', vcMode)
    
    gitCloneBase('bxexamples',  'bxexamples/base', vcMode)
    gitClone('bxexamples/overview',  'bxexamples/overview', vcMode)    
    gitClone('bxexamples/bashIcm',  'bxexamples/bashIcm', vcMode)
    gitClone('bxexamples/bashProcessArgsAndStdin',  'bxexamples/bashProcessArgsAndStdin', vcMode)
    gitClone('bxexamples/roVerifier-petstore',  'bxexamples/roVerifier-petstore', vcMode)
    gitClone('bxexamples/usbTetheredMobilePhoneLinuxRouter',  'bxexamples/usbTetheredMobilePhoneLinuxRouter', vcMode)
    gitClone('bxexamples/comeega',  'bxexamples/comeega', vcMode)

    gitCloneBase('bxlcnt',  'bxlcnt/base', vcMode)    
    gitClone('bxlcnt/overview',  'bxlcnt/overview', vcMode)
    gitClone('bxlcnt/bxtex',  'bxlcnt/bxtex', vcMode)    
    gitClone('bxlcnt/facilities',  'bxlcnt/facilities', vcMode)
    gitClone('bxlcnt/results',  'bxlcnt/results', vcMode)

    return pbdDict



####+BEGIN: bx:dblock:python:func :funcName "pbdDict_extRepos" :comment "pbd Dictionary" :funcType "Init" :retType "bxReposRootBaseDirsDict" :argsList "baseDir vcMode=None gitLabel='github.com'" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_extRepos/ =pbd Dictionary= retType=bxReposRootBaseDirsDict argsList=(baseDir vcMode=None gitLabel='github.com')  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_extRepos(
    baseDir,
    vcMode=None,
    gitLabel='github.com',
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bxReposBasesInstall.tex
*** See: \section{/bxRepos Bases Directory Structure Overview}
    """

    pbdDict = collections.OrderedDict()

    # root = bxReposRoot_baseObtain(baseDir)
    root = baseDir
    pbdDict['/'] = bxpBaseDir.bxpObjGet_baseDir(root, '')

    if not vcMode:
        vcMode = "anon"
    
    def fullDestPathGet(dstPathRel):
        return(os.path.join(
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
                "cd {root}/{baseDir} && git clone git://{gitLabel}/{gitRepoPath}.git"
                .format(
                    root=root,
                    baseDir=baseDir,
                    gitLabel=gitLabel,
                    gitRepoPath=gitRepoPath,
                )
            )
        elif vcMode == "auth":
            # command(  dstPathRel,
            #   "cd {root}/{baseDir} && git clone https://{gitUserName}:{gitPasswd}@github.com/{gitRepoPath}"
            #   .format(root=root, baseDir=baseDir, gitUserName=gitUserName, gitPasswd=gitPasswd, gitRepoPath=gitRepoPath)
            # )
            command(
                dstPathRel,
                "cd {root}/{baseDir} && git clone git@{gitLabel}:{gitRepoPath}.git"
                .format(
                    root=root,
                    baseDir=baseDir,
                    gitLabel=gitLabel,                    
                    gitRepoPath=gitRepoPath,
                )
            )
 
        else:
            b_io.eh.problem_usageError("")


    def gitCloneBase(locPathRel, remGitRepoPath, vcMode):
        locBasenameRel = os.path.basename(locPathRel)
        locDirnameRel = os.path.dirname(locPathRel)
        
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
            command(
                locPathRel,
                "cd {locDirnameFull} && git clone git://{gitLabel}/{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                .format(
                    locDirnameFull=locDirnameFull,
                    gitLabel=gitLabel,
                    remGitRepoPath=remGitRepoPath,
                    repoName=repoName,
                    locBasenameRel=locBasenameRel,
                )
            )
            
        elif vcMode == "auth":
            #
            # Note: Strange: You can not use multiple command() below.
            # Not understood yet. To be revisited. MB-20200625
            #
            # command(  locDirnamePlusRepoRel,
            #   "cd {locDirnameFull} && git clone https://{gitUserName}:{gitPasswd}@github.com/{remGitRepoPath} && mv {repoName} {locBasenameRel}"
            #   .format(
            #       locDirnameFull=locDirnameFull,
            #       gitUserName=gitUserName,
            #       gitPasswd=gitPasswd,
            #       remGitRepoPath=remGitRepoPath,
            #       repoName=repoName,
            #       locBasenameRel=locBasenameRel
            #   )
            # )
            command(
                locPathRel,
                "cd {locDirnameFull} && git clone git@{gitLabel}:{remGitRepoPath}.git && mv {repoName} {locBasenameRel}"
                .format(
                    locDirnameFull=locDirnameFull,
                    gitLabel=gitLabel,                    
                    remGitRepoPath=remGitRepoPath,
                    repoName=repoName,
                    locBasenameRel=locBasenameRel,
                )
            )

        else:
            b_io.eh.problem_usageError("")
            
            
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
        'emacs/doomemacs',
        'doomemacs/doomemacs',
        vcMode
    )
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

    directory('blee3')

    gitClone(
        'blee3/straight.el',
        'radian-software/straight.el',
        vcMode
    )
    gitClone(
        'blee3/s.el',
        'magnars/s.el',
        vcMode
    )
    gitClone(
        'blee3/loop.el',
        'Wilfred/loop.el',
        vcMode
    )
    
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
    outcome = bxReposRootGet().pyCmnd(
        # interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return outcome.results

    
####+BEGINNOT: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "bxReposRootGet" :parsMand "" :parsOpt "baseDir" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxReposRootGet>>  =verify= parsOpt=baseDir ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxReposRootGet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             baseDir: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'baseDir': baseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        # baseDir = csParam.mappedValue('baseDir', baseDir)
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

            b_io.eh.problem_usageError("Missing /bxRepos and no /etc/bxReposRoot")            
            retVal = None
            break

        if rtInv.outs:
            b_io.ann.write("{}".format(retVal))

        return cmndOutcome.set(
            opError=b.op.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/   [[elisp:(org-cycle)][| ]]
    #+end_org """
    def cmndDocStr(
####+END:
            self,
    ) :
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
            
            
####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pbdShow" :parsMand "" :parsOpt "baseDir pbdName" :argsMin 1 :argsMax 1000 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pbdShow>>  =verify= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pbdShow(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             baseDir: typing.Optional[str]=None,  # Cs Optional Param
             pbdName: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        baseDir = csParam.mappedValue('baseDir', baseDir)
        pbdName = csParam.mappedValue('pbdName', pbdName)
####+END:
        def cmndDesc(): """
** for each arg, output bxRepos parameters.
"""
        b_io.ann.write("{}".format(baseDir))

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
                opError=b.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )
    
####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pbdVerify" :parsMand "" :parsOpt "baseDir pbdName" :argsMin 1 :argsMax 1000 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pbdVerify>>  =verify= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pbdVerify(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             baseDir: typing.Optional[str]=None,  # Cs Optional Param
             pbdName: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        baseDir = csParam.mappedValue('baseDir', baseDir)
        pbdName = csParam.mappedValue('pbdName', pbdName)
####+END:
        def cmndDesc(): """
** for each arg, verify that each exists as expected.
"""
        b_io.ann.write("{}".format(baseDir))
                
        if not pbdName:
            pbdName = 'bxReposRoot'

        if baseDir:
            pbdDict = eval("""pbdDict_{}("{}")""".format(pbdName, baseDir))
        else:
            pbdDict = eval("""pbdDict_{}({})""".format(pbdName, baseDir))

        def procEach(pbdItem):
            pbdObj = pbdDict[pbdItem]
            pbdObj.verify()

        effectiveArgsList = argsList
        
        if effectiveArgsList[0] == "all":
            for each in pbdDict:
                procEach(each)

            return cmndOutcome.set(
                opError=b.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )
 
####+BEGINNOT: b:py3:cs:cmnd/classHead :cmndName "pbdUpdate" :parsMand "" :parsOpt "baseDir pbdName vcMode gitLabel" :argsMin 1 :argsMax 1000 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pbdUpdate>>  =verify= parsOpt=baseDir pbdName vcMode gitLabel argsMin=1 argsMax=1000 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pbdUpdate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'baseDir', 'pbdName', 'vcMode', 'gitLabel', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             baseDir: typing.Optional[str]=None,  # Cs Optional Param
             pbdName: typing.Optional[str]=None,  # Cs Optional Param
             vcMode: typing.Optional[str]=None,  # Cs Optional Param
             gitLabel: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'baseDir': baseDir, 'pbdName': pbdName, 'vcMode': vcMode, 'gitLabel': gitLabel, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        # baseDir = csParam.mappedValue('baseDir', baseDir)
        # pbdName = csParam.mappedValue('pbdName', pbdName)
        # vcMode = csParam.mappedValue('vcMode', vcMode)
        # gitLabel = csParam.mappedValue('gitLabel', gitLabel)
####+END:
        b_io.ann.here("baseDir={baseDir} -- pbdName={pbdName} -- gitLabel={gitLabel}".format(
            baseDir=baseDir, pbdName=pbdName, gitLabel=gitLabel))

        if not gitLabel:
            gitLabel = 'github.com'
        
        if not pbdName:
            #pbdName = 'bxReposRoot'
            pbdName = 'bxReposRoot'

        if not vcMode:
            vcName = 'anon'
            
        if baseDir:
            pbdDict = eval("""pbdDict_{pbdName}("{baseDir}", vcMode="{vcMode}", gitLabel="{gitLabel}")""".format(
                pbdName=pbdName, baseDir=baseDir, vcMode=vcMode, gitLabel=gitLabel))
        else:
            # Do Not Quote None in eval
            pbdDict = eval("""pbdDict_{pbdName}({baseDir}, vcMode="{vcMode}", gitLabel="{gitLabel}")""".format(
                pbdName=pbdName, baseDir=baseDir, vcMode=vcMode, gitLabel=gitLabel))

        def procEach(pbdItem):
            #b_io.ann.here("pbdItem={pbdItem}".format(pbdItem=pbdItem))
            # NOTYET, Capture keyerror and report it as bad input.
            pbdObj = pbdDict[pbdItem]
            #b_io.ann.here("pbdObj={pbdObj} -- pbdItem={pbdItem}".
            #             format(pbdObj=pbdObj, pbdItem=pbdItem))
            pbdObj.update()

        effectiveArgsList = argsList

        if effectiveArgsList[0] == "all":
            for each in pbdDict:
                procEach(each)

            return cmndOutcome.set(
                opError=b.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
            self,
    ) :
        return """
***** For each arg, update each to what has been specified.
"""


        
####+BEGIN: bx:dblock:python:subSection :title "ICM Multiple pbdUpdates Based On Platform Defaults Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ICM Multiple pbdUpdates Based On Platform Defaults Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pbdRootsForPlatform" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pbdRootsForPlatform>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pbdRootsForPlatform(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
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
                b_io.eh.problem_usageError("")

            return rootDirName

        bxReposUserName = bxReposUserName_obtain()
        bxReposGroupName = bxReposGroupName_obtain()

        pbdNamesList = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)

        if pbdNamesList[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&-1")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            pbdNamesList = argChoices

        for each in pbdNamesList:
            rootDir = withPbdNameGetRootForPlatform(each)
            # b_io.ann.here("{} -- {}".format(each, rootDir))
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

            os.chmod(rootDir, 0o775)            

            outcome = icm.subProc_bash("""\
ls -ld  {rootDir}"""
                                       .format(rootDir=rootDir)
            ).log()
            if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
            

        #b_io.ann.here("{}".format(bxReposUserName))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(
####+END:
            self,
    ) :
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="pbdNamesList",
            argDefault='all',
            argChoices=['all', 'bxReposRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

    

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pbdUpdateForPlatform" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pbdUpdateForPlatform>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pbdUpdateForPlatform(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
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
                b_io.eh.problem_usageError("")

            return rootDirName
            

        pbdNamesList = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)

        if pbdNamesList[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&-1")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            #pbdNamesList = copy.deepcopy(argChoices)
            pbdNamesList = argChoices

        b_io.tm.here("{}".format(pbdNamesList))

        for each in pbdNamesList:
            rootDir = withPbdNameGetRootForPlatform(each)

            pbdUpdate().cmnd(
                interactive=False,
                baseDir=rootDir,
                pbdName=each,
                argsList=['all'],
            )

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(
####+END:
            self,
    ) :
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="pbdNamesList",
            argDefault='all',
            argChoices=['all', 'bxReposRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict
    

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(
####+END:
            self,
    ) :
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

    

####+BEGIN: bx:dblock:python:subSection :title "Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
