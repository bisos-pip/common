# -*- coding: utf-8 -*-
"""\
*    *[Summary]* ::  A /library/ with ICM Cmnds to support ByStar bases creation facilities
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/bisos/common/dev/bisos/common/bisosBaseDir.py :: [[elisp:(org-cycle)][| ]]
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
__libName__ = "bisosBaseDir"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201810053638"
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
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['baseDirBisos'], }
csInfo['version'] = '202408022832'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'baseDirBisos-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

####+BEGINNOT: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/csInfo-mbNedaGpl.py"
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

G = cs.globalContext.get()

from bisos.platform import bxPlatformConfig
from bisos.platform import bxPlatformThis

import shutil
import copy
import os


####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bxpBaseDir_libOverview" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxpBaseDir_libOverview>>  =verify= argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxpBaseDir_libOverview(cs.Cmnd):
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
** TODO [[elisp:(org-cycle)][| ]]  Problem         :: bxpBaseDir.py, baseDirBisos.py and bx-bases should collectively be cleaned up. [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Problem         :: At this time baseDirBisos.py is not being used.  [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:python:section :title "Directory Base Locations"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Directory Base Locations*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:subSection :title "ByStar Root"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *ByStar Root*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: bx:dblock:python:func :funcName "bxpRootBaseDirPtrSysFile_obtain" :comment "/etc/bystarRoot" :funcType "obtain" :retType "str" :argsList "" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-obtain   [[elisp:(outline-show-subtree+toggle)][||]] /bxpRootBaseDirPtrSysFile_obtain/ =/etc/bystarRoot= retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def bxpRootBaseDirPtrSysFile_obtain():
####+END:
    return os.path.abspath(
        "/etc/bisosRoot"
    )


####+BEGIN: bx:dblock:python:func :funcName "bxpRootBaseDirPtrUserFile_obtain" :comment "~/.bystarRoot" :funcType "obtain" :retType "str" :argsList "" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-obtain   [[elisp:(outline-show-subtree+toggle)][||]] /bxpRootBaseDirPtrUserFile_obtain/ =~/.bystarRoot= retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def bxpRootBaseDirPtrUserFile_obtain():
####+END:
    return os.path.abspath(
        os.path.expanduser(
            "~/.bisosRoot"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bxpRootBaseDirDefault_obtain" :comment "/bystar" :funcType "obtain" :retType "str" :argsList "" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-obtain   [[elisp:(outline-show-subtree+toggle)][||]] /bxpRootBaseDirDefault_obtain/ =/bystar= retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def bxpRootBaseDirDefault_obtain():
####+END:
    return os.path.abspath(
        "/bisos"
    )


####+BEGIN: bx:dblock:python:subSection :title "BISOS Bases"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BISOS Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bpbDist_baseObtain_bin" :comment "DIST BIN" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbDist_baseObtain_bin/ =DIST BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbDist_baseObtain_input/ =DIST DATA= retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisos_baseObtain_root/ =BISOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisos_baseObtain_bin/ =BISOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisos_baseObtain_var/ =BISOS BIN= retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisos_baseObtain_input/ =BISOS DATA= retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *BISOS Pkg Bases*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_var" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisosPkg_baseObtain_var/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_var(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_tmp" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisosPkg_baseObtain_tmp/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_tmp(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))

####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_log" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisosPkg_baseObtain_log/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_log(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))


####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_control" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisosPkg_baseObtain_control/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_control(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))



####+BEGIN: bx:dblock:python:func :funcName "bpbBisosPkg_baseObtain_input" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bpbBisosPkg_baseObtain_input/ retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisosPkg_baseObtain_input(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return( os.path.join(
        outcome.results, "unisos", "data"
    ))


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
        parScope=icm.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--baseDir',
    )

    csParams.parDictAdd(
        parName='pbdName',
        parDescription="Platform BaseDirs Dict Name",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--pbdName',
    )

        
####+BEGIN: bx:dblock:python:section :title "Common Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "examples_bxPlatformBaseDirsCommon" :comment "Base Roots Info And Preps" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-examples  :: /examples_bxPlatformBaseDirsCommon/ =Base Roots Info And Preps= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxPlatformBaseDirsCommon():
####+END:
    cs.examples.menuChapter('* =BxP BaseDir=  ByStar Platform Base Dirs')

    cmndName = "bxpRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "bxpRootGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['baseDir'] = '/tmp/bxBase'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cs.examples.execInsert(execLine="""cat {}""".format(bxpRootBaseDirPtrUserFile_obtain()),)
    cs.examples.execInsert(execLine="""cat {}""".format(bxpRootBaseDirPtrSysFile_obtain()),)
    cs.examples.execInsert(execLine="""ls -l {}""".format(bxpRootBaseDirDefault_obtain(),)) 
    cs.examples.execInsert(execLine="""ls -l /bisos /de /bxo""")   
    cs.examples.execInsert(execLine="""sudo mkdir /bisos; sudo chown {}:{} /bisos"""
                         .format(bisosUserName_obtain(), bisosGroupName_obtain()))
    cs.examples.execInsert(execLine="""sudo mkdir /de; sudo chown {}:{} /de"""
                         .format(bisosUserName_obtain(), bisosGroupName_obtain()))
    cs.examples.execInsert(execLine="""sudo mkdir /bxo; sudo chown {}:{} /bxo"""
                         .format(bisosUserName_obtain(), bisosGroupName_obtain()))


####+BEGIN: bx:dblock:python:func :funcName "examples_bxPlatformBaseDirs" :comment "bx-bases.py module information" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-examples  :: /examples_bxPlatformBaseDirs/ =bx-bases.py module information= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxPlatformBaseDirs():
####+END:
    """
** Auxiliary examples to be commonly used.
"""
    #examples_bxPlatformBaseDirsCommon()

    cs.examples.menuChapter('* =BxP BaseDir=  Module Description,Usage,Status Information')
    
    menuLine = """"""
    icm.cmndExampleMenuItem(menuLine, icmName="bx-bases", verbosity='none')    


####+BEGIN: bx:dblock:python:func :funcName "examples_bxPlatformBaseDirsFull" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-examples  :: /examples_bxPlatformBaseDirsFull/ =Show/Verify/Update For relevant PBDs= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_bxPlatformBaseDirsFull():
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)
    
    #bxRootBase = bxpRoot_baseObtain(None)

    examples_bxPlatformBaseDirsCommon()
    
    cs.examples.menuChapter('* =Module=  Overview (desc, usage, status)')    
   
    cmndName = "overview_bxpBaseDir" ; cmndArgs = "moduleDescription moduleUsage moduleStatus" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cs.examples.menuChapter(' =BxP DirBases=  *pbdShow/pbdVerify/pbdUpdate Of Relevant PBDs*')    

    cs.examples.menuSection(' =BxP DirBases=  *pbdShow*')        
    cmndName = "pbdShow" ; cmndArgs = "/ dist" ;
    cps = collections.OrderedDict() ;
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdShow" ; cmndArgs = "/ var tmp dist/pip " ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bisosRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bisosRoot'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'deRunRoot'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdShow" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['pbdName'] = 'bxoRoot'
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cs.examples.menuSection(' =BxP DirBases=  *pbdVerify*')            
    
    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdVerify" ; cmndArgs = "/ var" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BISOS'; cps['pbdName'] = 'bisosRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos'; cps['pbdName'] = 'bisosRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/de'; cps['pbdName'] = 'deRunRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdVerify" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bxo'; cps['pbdName'] = 'bxoRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cs.examples.menuSection(' =BxP DirBases=  *pbdUpdate*')
    
    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict()
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little', comment="# default pbdName")

    cmndName = "pbdUpdate" ; cmndArgs = "/ var" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BISOS'; cps['pbdName'] = 'bisosRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bisos'; cps['pbdName'] = 'bisosRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/de'; cps['pbdName'] = 'deRunRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "pbdUpdate" ; cmndArgs = "all" ;
    cps = collections.OrderedDict() ; cps['baseDir'] = '/bxo'; cps['pbdName'] = 'bxoRoot' 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

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
 
    cs.examples.menuSection(' =BxP DirBases Creation/Ownership=  *pbdRootsForPlatform*')   
    
    cmndName = "pbdRootsForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    cmndName = "pbdRootsForPlatform" ; cmndArgs = "bisosRoot" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         icmWrapper="sudo", comment="# Create Root Bases")

    cs.examples.menuSection(' =BxP DirBases Update=  *pbdUpdateForPlatform*')   

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "all" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")

    cmndName = "pbdUpdateForPlatform" ; cmndArgs = "bisosRoot" ;
    cps=cpsInit() ; cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little',
                                         comment="# Create/Update Initial Base DirTrees")
    
    # pbdList has been OBSOLETED
    # cs.examples.menuChapter(' =BxP DirBases=  *pbdShow/pbdVerify/pbdUpdate*')    

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bystar" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] = '/tmp/BISOS'
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "pbdListUpdate" ; cmndArgs = "pbdList_bystar" ;
    # cps = collections.OrderedDict() ; cps['baseDir'] =  bxRootBase
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
####+BEGIN: bx:dblock:python:section :title "Misc To Be Sorted Out"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Misc To Be Sorted Out*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    
####+BEGIN: bx:dblock:python:func :funcName "bisosUserName_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Obtain    :: /bisosUserName_obtain/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Obtain    :: /bisosGroupName_obtain/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Base Dirs Specifications ::*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:section :title " /===== PBD SPECIFICATION CMNDs =====/ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    * /===== PBD SPECIFICATION CMNDs =====/ *  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bisosRoot" :comment "pbd Dictionary" :funcType "Init" :retType "bxpRootBaseDirsDict" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bisosRoot/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bisosRoot(
    baseDir,
):
####+END:
    """
** In /lcnt/lgpc/bystar/permanent/common/clips/bisosBasesInstall.tex
*** See: \section{/bisos Bases Directory Structure Overview}
***  Panel documentation::  [[elisp:(blee:bnsm:panel-goto "../bisosBaseDirs")][bisosBaseDirs]]
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


    directory('git')
    directory('git/auth')
    directory('git/auth/bxRepos')
    directory('git/anon')    
    directory('git/anon/bxRepos')
    symLink(  'git/bxRepos', 'git/anon/bxRepos')
    directory('git/anon/ext')    # base for external repos
    
    
    directory('control')
    directory('control/bisos')    
    directory('control/bisos/site')    

    directory('var')
    directory('var/core')
    directory('var/core/icmsPkg')
    directory('var/log')
    directory('var/log/core')
    
    directory('tmp')

    directory('panels')
    symLink(   'panels/blee', 'git/bxRepos/NOTYET')
    symLink(   'panels/core', 'git/bxRepos/NOTYET')
    symLink(   'panels/site', 'git/bxRepos/NOTYET')
    symLink(   'panels/user', 'git/bxRepos/NOTYET')        
    
    directory('blee')

    return pbdDict


####+BEGIN: bx:dblock:python:func :funcName "pbdDict_bisosRootOrig" :comment "pbd Dictionary" :funcType "Init" :retType "bxpRootBaseDirsDict" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bisosRootOrig/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def pbdDict_bisosRootOrig(
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

    
    # directory('vcAuth')
    # directory('vcAuth/bisos')
    
    # directory('vcAnon')
    # directory('vcAnon/bisos')

    directory('git')
    directory('git/auth')
    directory('git/auth/bxRepos')
    directory('git/anon')    
    directory('git/anon/bxRepos')
    symLink(  'git/bxRepos', 'git/auth/bxRepos')    
    
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_deRunRoot/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-Init      :: /pbdDict_bxoRoot/ =pbd Dictionary= retType=bxpRootBaseDirsDict argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
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
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "bxpRoot_baseObtain" :funcType "obtain" :retType "str" :argsList "baseDir" :deco ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-obtain    :: /bxpRoot_baseObtain/ retType=str argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bxpRoot_baseObtain(
    baseDir,
):
####+END:
    outcome = bxpRootGet().cmnd(
        interactive=False,
        baseDir=baseDir,
    )
    if outcome.isProblematic(): return b_io.eh.badOutcome(outcome)    

    return outcome.results

    
####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "bxpRootGet" :parsMand "" :parsOpt "baseDir" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bxpRootGet>>  =verify= parsOpt=baseDir ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bxpRootGet(cs.Cmnd):
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
        baseDir = csParam.mappedValue('baseDir', baseDir)
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

            b_io.eh.problem_usageError("Missing /bystar and no /etc/bystarRoot")            
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
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Based ~/.bystarRoot or /etc/bystarRoot decide on meta.
   ** if --baseDir Was specified, it is returned or 
   ** If ~/.bystarRoot exists, its content is returned
   ** If /etc/bystarRoot exists, its content is returned
   ** If /bystar exists, "/bystar" is returned
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
** for each arg, output bxp parameters.
"""
        b_io.ann.write("{}".format(baseDir))

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
                opError=b.OpError.Success,
                opResults=None,
            )
 
        for each in  effectiveArgsList:
            procEach(each)
            
        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )
 
####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "pbdUpdate" :parsMand "" :parsOpt "baseDir pbdName" :argsMin 1 :argsMax 1000 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pbdUpdate>>  =verify= parsOpt=baseDir pbdName argsMin=1 argsMax=1000 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pbdUpdate(cs.Cmnd):
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
        b_io.ann.here("baseDir={baseDir} -- pbdName={pbdName}".format(baseDir=baseDir, pbdName=pbdName))

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
            #b_io.ann.here("pbdObj={pbdObj} -- pbdItem={pbdItem}".
            #             format(pbdObj=pbdObj, pbdItem=pbdItem))
            pbdObj.update()

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

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/   [[elisp:(org-cycle)][| ]]
    #+end_org """
    def cmndDocStr(
####+END:
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
            
            bxPlatformConfigBase = bxPlatformThis.pkgBase_configDir()
            
            if pbdName == "bisosRoot":
                rootDirName = bxPlatformConfig.rootDir_bisos_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "deRunRoot":
                rootDirName = bxPlatformConfig.rootDir_bxo_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "bxoRoot":
                rootDirName = bxPlatformConfig.rootDir_deRun_fpObtain(bxPlatformConfigBase)
            else:
                b_io.eh.problem_usageError("")

            return rootDirName

        bisosUserName = bisosUserName_obtain()
        bisosGroupName = bisosGroupName_obtain()

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
            #shutil.chown(rootDir, bisosUserName, bisosGroupName)
            uid = pwd.getpwnam(bisosUserName).pw_uid
            gid = grp.getgrnam(bisosGroupName).gr_gid
            os.chown(rootDir, uid, gid)

            os.chmod(rootDir, 0775)            

            outcome = icm.subProc_bash("""\
ls -ld  {rootDir}"""
                                       .format(rootDir=rootDir)
            ).log()
            if outcome.isProblematic(): return(io.eh.badOutcome(outcome))
            

        #b_io.ann.here("{}".format(bisosUserName))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/   [[elisp:(org-cycle)][| ]]
    #+end_org """
    def cmndArgsSpec(
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="pbdNamesList",
            argDefault='all',
            argChoices=['all', 'bisosRoot', 'deRunRoot', 'bxoRoot'],
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
            
            bxPlatformConfigBase = bxPlatformThis.pkgBase_configDir()
            
            if pbdName == "bisosRoot":
                rootDirName = bxPlatformConfig.rootDir_bisos_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "bxoRoot":
                rootDirName = bxPlatformConfig.rootDir_bxo_fpObtain(bxPlatformConfigBase)
                
            elif pbdName == "deRunRoot":
                rootDirName = bxPlatformConfig.rootDir_deRun_fpObtain(bxPlatformConfigBase)
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

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/   [[elisp:(org-cycle)][| ]]
    #+end_org """
    def cmndArgsSpec(
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="pbdNamesList",
            argDefault='all',
            argChoices=['all', 'bisosRoot', 'deRunRoot', 'bxoRoot'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict
    

####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndDocStr/   [[elisp:(org-cycle)][| ]]
    #+end_org """
    def cmndDocStr(
####+END:
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
