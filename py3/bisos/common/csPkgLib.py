# -*- coding: utf-8 -*-
"""\
* *[Summary]* ::  A /library/ to support icmsPkg facilities based on the pkgThis information
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
""" #+begin_org
*  This file:/bisos/git/bxRepos/bisos-pip/common/py3/bisos/common/csPkgLib.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
#+end_org """
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "icmsPkgLib"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805311412"
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
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['boxRegfps'], }
csInfo['version'] = '202402043414'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'boxRegfps-Panel.org'
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
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
import collections
#import enum

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

from bisos.common import serviceObject


####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "icmsPkgLib_libOverview" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<icmsPkgLib_libOverview>>  =verify= argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class icmsPkgLib_libOverview(cs.Cmnd):
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
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"

####+END:


def pkgBaseDir_obtain():
    return os.path.abspath(
        ".."
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  pkgInfoBaseDir_obtain    [[elisp:(org-cycle)][| ]]
"""
def pkgInfoBaseDir_obtain():
    return os.path.abspath(
        "../pkgInfo"
    )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  pkgInputsBaseDir_obtain    [[elisp:(org-cycle)][| ]]
"""
####+BEGIN: bx:cs:python:func :funcName "pkgInputsBaseDir_obtain" :funcType "anyOrNone" :retType "str" :deco "" :argsList "icmsPkgInputsBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /pkgInputsBaseDir_obtain/ retType=str argsList=(icmsPkgInputsBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def pkgInputsBaseDir_obtain(
    icmsPkgInputsBaseDir,
):
####+END:
    if icmsPkgInputsBaseDir:
        return os.path.abspath(
            "{}".format(icmsPkgInputsBaseDir)
        )
    else:
        return b_io.eh.problem_usageError("Missing BaseDir")        


####+BEGIN: bx:cs:python:func :funcName "pkgInfoFpBaseDir_obtain" :funcType "anyOrNone" :retType "str" :deco "" :argsList "icmsPkgInfoBaseDir"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /pkgInfoFpBaseDir_obtain/ retType=str argsList=(icmsPkgInfoBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def pkgInfoFpBaseDir_obtain(
    icmsPkgInfoBaseDir,
):
####+END:
    if icmsPkgInfoBaseDir:
        return os.path.abspath(
            "{}/pkgInfo/fp".format(icmsPkgInfoBaseDir)
        )
    else:
        return b_io.eh.problem_usageError("Missing BaseDir")        

####+BEGIN: bx:cs:python:func :funcName "controlBaseDir_obtain" :funcType "anyOrNone" :retType "str" :deco "" :argsList "icmsPkgInfoBaseDir bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /controlBaseDir_obtain/ retType=str argsList=(icmsPkgInfoBaseDir bxoId=None sr=None)  [[elisp:(org-cycle)][| ]]
"""
def controlBaseDir_obtain(
    icmsPkgInfoBaseDir,
    bxoId=None,
    sr=None,
):
####+END:
    if bxoId:
        return (
            serviceObject.srFullPathBaseDir_obtain(
                bxoId,
                sr,
            )
        )
    
    if icmsPkgInfoBaseDir:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot= os.path.abspath("{}/pkgInfo/fp".format(icmsPkgInfoBaseDir)),
                parName="icmsPkgControlBaseDir")
        )
    else:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot="../pkgInfo/fp",
                parName="icmsPkgControlBaseDir")
        )


def logBaseDir_obtain(
    icmsPkgInfoBaseDir=None,
    bxoId=None,
    sr=None,
):
    if bxoId:
        return (
            serviceObject.bxoSr_runBaseObtain_log(
                bxoId,
                sr,
            )
        )

    if icmsPkgInfoBaseDir:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot= os.path.abspath("{}/pkgInfo/fp".format(icmsPkgInfoBaseDir)),
                parName="icmsPkgLogBaseDir")
        )
    else:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot="../pkgInfo/fp",
                parName="icmsPkgLogBaseDir")
        )


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  varBaseDir_obtain    [[elisp:(org-cycle)][| ]]
"""
def varBaseDir_obtain(
    icmsPkgInfoBaseDir=None,
    bxoId=None,
    sr=None,
):
    if bxoId:
        return (
            serviceObject.bxoSr_runBaseObtain_var(
                bxoId,
                sr,
            )
        )
    if icmsPkgInfoBaseDir:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot= os.path.abspath("{}/pkgInfo/fp".format(icmsPkgInfoBaseDir)),
                parName="icmsPkgVarBaseDir")
        )
    else:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot="../pkgInfo/fp",
                parName="icmsPkgVarBaseDir")
        )


def varConfigBaseDir_obtain(
    icmsPkgInfoBaseDir=None,
    bxoId=None,
    sr=None,
):
    if bxoId:
        return (
            serviceObject.bxoSr_runBaseObtain_var(
                bxoId,
                sr,
            )
        )
    return(
        os.path.join(varBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "config")
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  tmpBaseDir_obtain    [[elisp:(org-cycle)][| ]]
"""
def tmpBaseDir_obtain(
    icmsPkgInfoBaseDir=None,
    bxoId=None,
    sr=None,
):
    if bxoId:
        return (
            serviceObject.bxoSr_runBaseObtain_tmp(
                bxoId,
                sr,
            )
        )
    if icmsPkgInfoBaseDir:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot= os.path.abspath("{}/pkgInfo/fp".format(icmsPkgInfoBaseDir)),
                parName="icmsPkgTmpBaseDir")
        )
    else:
        return(
            b.fp.FileParamValueReadFrom(
                parRoot="../pkgInfo/fp",
                parName="icmsPkgTmpBaseDir")
        )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF          ::  icmsBxoBaseDir_obtain    [[elisp:(org-cycle)][| ]]
"""
def icmsBxoBaseDir_obtain():
    return os.path.abspath(
        "../../.."
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF          ::  icmsRunEnvBaseDir_obtain    [[elisp:(org-cycle)][| ]]
"""
def icmsRunEnvBaseDir_obtain():
    return icmsBxoBaseDir_obtain()


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *File Parameters Obtain*
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  icmsPkgName_fpObtain    [[elisp:(org-cycle)][| ]]
"""
def icmsPkgName_fpObtain(
        icmsPkgInfoBaseDir=None,
):
    """NOTYET -- Called obtain to leave Get for the IIF"""
    return b.fp.FileParamValueReadFrom(
        parRoot=os.path.join(
            pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir),
        ),
        parName="icmsPkgName",
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  icmsPkgControlBaseDir_fpObtain    [[elisp:(org-cycle)][| ]]
"""
def icmsPkgControlBaseDir_fpObtain():
    """NOTYET -- Called obtain to leave Get for the IIF"""
    return b.fp.FileParamValueReadFrom(
        parRoot=os.path.join(
            pkgInfoFpBaseDir_obtain(),            
        ),
        parName="icmsPkgControlBaseDir",        
    )



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Arguments Specification*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  commonParamsSpecify    [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
        csParams,
):
    
    csParams.parDictAdd(
        parName='icmsPkgName',
        parDescription="ICMs Package Name",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgName',
    )

    csParams.parDictAdd(
        parName='icmsPkgInfoBaseDir',
        parDescription="ICMs Package Info Environment -- A BaseDir for var/log/tmp (bxo=current bxo)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgInfoBaseDir',
    )
    
    csParams.parDictAdd(
        parName='icmsPkgRunBaseDir',
        parDescription="ICMs Package Run Environment -- A BaseDir for var/log/tmp (bxo=current bxo)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgRunBaseDir',
    )
    
    csParams.parDictAdd(
        parName='icmsPkgControlBaseDir',
        parDescription="ICMs Package Control Base Directory",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgControlBaseDir',
    )
    
    csParams.parDictAdd(
        parName='icmsPkgVarBaseDir',
        parDescription="ICMs Package Var Base Directory",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgVarBaseDir',
    )

    
    csParams.parDictAdd(
        parName='icmsPkgLogBaseDir',
        parDescription="ICMs Package Log Base Directory",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgLogBaseDir',
    )

        
    csParams.parDictAdd(
        parName='icmsPkgTmpBaseDir',
        parDescription="ICMs Package Tmp Base Directory",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=cs.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--icmsPkgTmpBaseDir',
    )


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common Examples Sections*
"""
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_pkgInfoPars    [[elisp:(org-show-subtree)][|=]]   [[elisp:(org-cycle)][| ]]
"""    
def examples_pkgInfoPars():
    """
** Auxiliary examples to be commonly used.
"""
    cs.examples.menuChapter('* =FP Values=  pkgInfo Parameters')

    cmndAction = " -i inMailAcctParsGet" ; cmndArgs = ""
    menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    cs.cmndExampleMenuItem(menuLine, verbosity='none')

    menuLine = """"""
    cs.cmndExampleMenuItem(menuLine, icmName="pkgManage.py", verbosity='none')

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  examples_pkgInfoParsFull    [[elisp:(org-cycle)][| ]]
"""
def examples_pkgInfoParsFull(
    icmsPkgName,
    icmsPkgInfoBaseDir=None,
    icmsPkgModuleBaseDir=None,        
    icmsPkgControlBaseDir=None,
    icmsPkgRunBaseDir=None,
):
    """
** Auxiliary examples to be commonly used.
"""
    
    cs.examples.menuChapter(' =Pkg/Module BaseDirs=  *Admin Panel*')

    print(("{icmsPkgInfoBaseDir}  # pkgInfo/fp/icmsPkgName ## Rest is obsolete".format(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir)))
    print(("{icmsPkgModuleBaseDir} #  admin,inputs".format(icmsPkgModuleBaseDir=icmsPkgModuleBaseDir))) 
    print(("{panel}".format(panel=os.path.join(icmsPkgModuleBaseDir, "admin", "Panel.org"))))
        
    
    cs.examples.menuChapter(' =FP Values=  *pkgInfo Get Parameters*')

    cmndName = "pkgInfoParsGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['icmsPkgInfoBaseDir'] = icmsPkgInfoBaseDir 
    cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')

    # cmndAction = " -i pkgInfoParsGet" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, verbosity='none')

    # cs.examples.menuChapter(' =FP Values=  *PkgInfo Defaults ParsSet  --*')

    # cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bisosPolicy" ;
    # cps = collections.OrderedDict() ; cps['icmsPkgName'] = icmsPkgName ; cps['icmsPkgControlBaseDir'] = icmsPkgControlBaseDir ; cps['icmsPkgInfoBaseDir'] = icmsPkgInfoBaseDir 
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    # cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "bxoPolicy" ;
    # cps = collections.OrderedDict() ; cps['icmsPkgName'] = icmsPkgName ; cps['icmsPkgControlBaseDir'] = icmsPkgControlBaseDir 
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    # cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "runBaseDirPolicy" ;
    # cps = collections.OrderedDict() ; cps['icmsPkgName'] = icmsPkgName
    # cps['icmsPkgControlBaseDir'] = icmsPkgControlBaseDir ; cps['icmsPkgRunBaseDir'] = icmsPkgRunBaseDir
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    # cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "debianPolicy" ;
    # cps = collections.OrderedDict() ; cps['icmsPkgName'] = icmsPkgName 
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    
    # cmndName = "pkgInfoParsDefaultsSet" ; cmndArgs = "centosPolicy" ;
    # cps = collections.OrderedDict() ; cps['icmsPkgName'] = icmsPkgName 
    # cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity='little')
    

    # cs.examples.menuChapter(' =FP Values=  *PkgInfo ParsSet -- Set Parameters Explicitly*')

    # cmndAction = " -i pkgInfoParsSet" ; cmndArgs = ""
    # menuLine = """--icmsPkgName="pkgName" {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')

    # cmndAction = " -i pkgInfoParsSet" ; cmndArgs = ""
    # menuLine = """--icmsPkgControlBaseDir="path"  {cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')

    # cmndAction = " -i pkgInfoParsSet" ; cmndArgs = ""
    # varPath = os.path.join(icmsRunEnvBaseDir_obtain(), "var", icmsPkgName_fpObtain(
    #     icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))
    # menuLine = """--icmsPkgVarBaseDir={varPath}  {cmndAction} {cmndArgs}""".format(
    #     varPath=varPath, cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')

    # cmndAction = " -i pkgInfoParsSet" ; cmndArgs = ""
    # tmpPath = os.path.join(icmsRunEnvBaseDir_obtain(), "tmp", icmsPkgName_fpObtain(
    #     icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))
    # menuLine = """--icmsPkgTmpBaseDir={tmpPath}  {cmndAction} {cmndArgs}""".format(
    #     tmpPath=tmpPath, cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="echo", verbosity='none')
  
    # cs.examples.menuChapter(' =RunEnv=  *Run Environment (BaseDirs) Setups/Clean*')    

    # cmndAction = " -i icmsRunEnvsPreps" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')

    # cmndAction = " -i icmsRunEnvsClean" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')

    # cs.examples.menuChapter(' =RunEnv=  *SymLinks To var/log/tmp/ Setups/Clean*')    

    # cmndAction = " -i icmsRunEnvsLinks" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')

    # cmndAction = " -i icmsRunEnvsLinksClean" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')

    # cs.examples.menuChapter(' =RunEnv=  *SymLinks To Libraries Setups/Clean*')    
    
    # cmndAction = " -i icmsLibsLinks" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')

    # cmndAction = " -i icmsLibsLinksClean" ; cmndArgs = ""
    # menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
    # icm.cmndExampleMenuItem(menuLine, icmWrapper="", verbosity='none')
     

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *File Parameters Get/Set -- Commands*
"""

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  FP_readTreeAtBaseDir_CmndOutput    [[elisp:(org-cycle)][| ]]
"""
def FP_readTreeAtBaseDir_CmndOutput(
        interactive,
        fpBaseDir,
        cmndOutcome,
):
    """Invokes FP_readTreeAtBaseDir.cmnd as interactive-output only."""
    #
    # Interactive-Output + Chained-Outcome Command Invokation
    #
    FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
    FP_readTreeAtBaseDir.cmndLineInputOverRide = True
    FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome
        
    return FP_readTreeAtBaseDir.cmnd(
        interactive=interactive,
        FPsDir=fpBaseDir,
    )


####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "pkgInfoParsGet" :comment "" :parsMand "icmsPkgInfoBaseDir" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pkgInfoParsGet>>  =verify= parsMand=icmsPkgInfoBaseDir ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pkgInfoParsGet(cs.Cmnd):
    cmndParamsMandatory = [ 'icmsPkgInfoBaseDir', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             icmsPkgInfoBaseDir: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'icmsPkgInfoBaseDir': icmsPkgInfoBaseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        icmsPkgInfoBaseDir = csParam.mappedValue('icmsPkgInfoBaseDir', icmsPkgInfoBaseDir)
####+END:

        #if not icmsPkgInfoBaseDir:
        #    icmsPkgInfoBaseDir = marmePkgThis.pkgBase_configDir()    # Should Delete This Line

        FP_readTreeAtBaseDir_CmndOutput(
            interactive=interactive,
            fpBaseDir=pkgInfoFpBaseDir_obtain(
                icmsPkgInfoBaseDir=icmsPkgInfoBaseDir,
            ),
            cmndOutcome=cmndOutcome,
        )

        return cmndOutcome


    def cmndDesc(): """
** Without --icmsPkgInfoBaseDir, it reads from ../pkgInfo/fp.
"""


####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "pkgInfoParsSet" :comment "" :parsMand "" :parsOpt "icmsPkgInfoBaseDir icmsPkgName icmsPkgControlBaseDir icmsPkgVarBaseDir icmsPkgTmpBaseDir icmsPkgBasesPolicy icmsPkgLogBaseDir" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pkgInfoParsSet>>  =verify= parsOpt=icmsPkgInfoBaseDir icmsPkgName icmsPkgControlBaseDir icmsPkgVarBaseDir icmsPkgTmpBaseDir icmsPkgBasesPolicy icmsPkgLogBaseDir ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pkgInfoParsSet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'icmsPkgInfoBaseDir', 'icmsPkgName', 'icmsPkgControlBaseDir', 'icmsPkgVarBaseDir', 'icmsPkgTmpBaseDir', 'icmsPkgBasesPolicy', 'icmsPkgLogBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             icmsPkgInfoBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgName: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgControlBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgVarBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgTmpBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgBasesPolicy: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgLogBaseDir: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'icmsPkgInfoBaseDir': icmsPkgInfoBaseDir, 'icmsPkgName': icmsPkgName, 'icmsPkgControlBaseDir': icmsPkgControlBaseDir, 'icmsPkgVarBaseDir': icmsPkgVarBaseDir, 'icmsPkgTmpBaseDir': icmsPkgTmpBaseDir, 'icmsPkgBasesPolicy': icmsPkgBasesPolicy, 'icmsPkgLogBaseDir': icmsPkgLogBaseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        icmsPkgInfoBaseDir = csParam.mappedValue('icmsPkgInfoBaseDir', icmsPkgInfoBaseDir)
        icmsPkgName = csParam.mappedValue('icmsPkgName', icmsPkgName)
        icmsPkgControlBaseDir = csParam.mappedValue('icmsPkgControlBaseDir', icmsPkgControlBaseDir)
        icmsPkgVarBaseDir = csParam.mappedValue('icmsPkgVarBaseDir', icmsPkgVarBaseDir)
        icmsPkgTmpBaseDir = csParam.mappedValue('icmsPkgTmpBaseDir', icmsPkgTmpBaseDir)
        icmsPkgBasesPolicy = csParam.mappedValue('icmsPkgBasesPolicy', icmsPkgBasesPolicy)
        icmsPkgLogBaseDir = csParam.mappedValue('icmsPkgLogBaseDir', icmsPkgLogBaseDir)
####+END:

        #G = cs.globalContext.get()        

        def createPathAndFpWrite(
                fpPath,
                valuePath,
        ):
            valuePath = os.path.abspath(valuePath)
            try:
                os.makedirs(valuePath)
            except OSError:
                if not os.path.isdir(valuePath):
                    raise
            
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=fpPath,
                parValue=valuePath,
            )

            
        if icmsPkgName:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "icmsPkgName"),
                parValue=icmsPkgName,
            )

        if icmsPkgBasesPolicy:
            icm.b.fp.FileParamWriteToPath(
                parNameFullPath=os.path.join(pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "icmsPkgBasesPolicy"),
                parValue=icmsPkgBasesPolicy,
            )

        if icmsPkgControlBaseDir:
            createPathAndFpWrite(
                os.path.join(pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "icmsPkgControlBaseDir"),
                icmsPkgControlBaseDir,
            )

        if icmsPkgVarBaseDir:
            createPathAndFpWrite(
                os.path.join(pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "icmsPkgVarBaseDir"),
                icmsPkgVarBaseDir,
            )

        if icmsPkgLogBaseDir:
            createPathAndFpWrite(
                os.path.join(pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "icmsPkgLogBaseDir"),
                icmsPkgLogBaseDir,
            )
            
        if icmsPkgTmpBaseDir:
            createPathAndFpWrite(
                os.path.join(pkgInfoFpBaseDir_obtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir), "icmsPkgTmpBaseDir"),
                icmsPkgTmpBaseDir,
            )
            
        if rtInv.outs:
            b_io.ann.here("pkgInfoParsSet")

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )


    def cmndDesc(): """
** Doc String Outside Of Dblock.
"""
    

####+BEGIN: b:py3:cs:cmnd/classHead :modPrefix "new" :cmndName "pkgInfoParsDefaultsSet" :comment "" :parsMand "icmsPkgName" :parsOpt "icmsPkgInfoBaseDir icmsPkgControlBaseDir icmsPkgRunBaseDir" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<pkgInfoParsDefaultsSet>>  =verify= parsMand=icmsPkgName parsOpt=icmsPkgInfoBaseDir icmsPkgControlBaseDir icmsPkgRunBaseDir argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class pkgInfoParsDefaultsSet(cs.Cmnd):
    cmndParamsMandatory = [ 'icmsPkgName', ]
    cmndParamsOptional = [ 'icmsPkgInfoBaseDir', 'icmsPkgControlBaseDir', 'icmsPkgRunBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             icmsPkgName: typing.Optional[str]=None,  # Cs Mandatory Param
             icmsPkgInfoBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgControlBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             icmsPkgRunBaseDir: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'icmsPkgName': icmsPkgName, 'icmsPkgInfoBaseDir': icmsPkgInfoBaseDir, 'icmsPkgControlBaseDir': icmsPkgControlBaseDir, 'icmsPkgRunBaseDir': icmsPkgRunBaseDir, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        icmsPkgName = csParam.mappedValue('icmsPkgName', icmsPkgName)
        icmsPkgInfoBaseDir = csParam.mappedValue('icmsPkgInfoBaseDir', icmsPkgInfoBaseDir)
        icmsPkgControlBaseDir = csParam.mappedValue('icmsPkgControlBaseDir', icmsPkgControlBaseDir)
        icmsPkgRunBaseDir = csParam.mappedValue('icmsPkgRunBaseDir', icmsPkgRunBaseDir)
####+END:
        #G = cs.globalContext.get()

        #basesPolicyChoices = self.__class__.cmndArgsSpec[0]

        basesPolicy = effectiveArgsList[0]

        if not basesPolicy:
            basesPolicy = G.icmRunArgsGet().cmndArgs[0]

        print(basesPolicy)
        print(icmsPkgInfoBaseDir)

        pkgInfoParsSet().cmnd(
            interactive=False,
            icmsPkgInfoBaseDir=icmsPkgInfoBaseDir,
            icmsPkgName=icmsPkgName,  
        )

        if basesPolicy == "bisosPolicy":
            if not icmsPkgControlBaseDir:
                return b_io.eh.problem_usageError("Missing Control BaseDir")

            controlPath = icmsPkgControlBaseDir
            varPath = os.path.join("/bisos", "var")
            logPath = os.path.join("/bisos", "log")            
            tmpPath = os.path.join("/bisos", "tmp")

        elif basesPolicy == "bxoPolicy":
            if not icmsPkgControlBaseDir:
                return b_io.eh.problem_usageError("")

            controlPath = icmsPkgControlBaseDir
            varPath = os.path.join(icmsRunEnvBaseDir_obtain(), "var", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))
            logPath = os.path.join(icmsRunEnvBaseDir_obtain(), "log", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))            
            tmpPath = os.path.join(icmsRunEnvBaseDir_obtain(), "tmp", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))

        elif basesPolicy == "runBaseDirPolicy":
            if not icmsPkgRunBaseDir:
                return b_io.eh.problem_usageError("")
            
            if icmsPkgControlBaseDir:
                controlPath = icmsPkgControlBaseDir
            else:
                controlPath = os.path.join(icmsPkgRunBaseDir, "control", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))

            varPath = os.path.join(icmsPkgRunBaseDir, "var", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))
            logPath = os.path.join(icmsPkgRunBaseDir, "log", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))            
            tmpPath = os.path.join(icmsPkgRunBaseDir, "tmp", icmsPkgName_fpObtain(icmsPkgInfoBaseDir=icmsPkgInfoBaseDir))
            
        elif basesPolicy == "debianPolicy":
            controlPath = os.path.join("/etc/bystar", icmsPkgName)
            varPath = os.path.join("/var/lib/bystar/", icmsPkgName)
            logPath = os.path.join("/var/log/bystar/", icmsPkgName)            
            tmpPath = os.path.join("/tmp/bystar", icmsPkgName)
            
        elif basesPolicy == "centosPolicy":
            controlPath = os.path.join("/etc/bystar", icmsPkgName)
            varPath = os.path.join("/var/lib/bystar/", icmsPkgName)
            logPath = os.path.join("/var/log/bystar/", icmsPkgName)            
            tmpPath = os.path.join("/tmp/bystar", icmsPkgName)
            
        else:
            return b_io.eh.critical_oops("basesPolicy={}".format(basesPolicy))

        pkgInfoParsSet().cmnd(
            interactive=False,
            icmsPkgInfoBaseDir=icmsPkgInfoBaseDir,
            icmsPkgBasesPolicy=basesPolicy,
            icmsPkgControlBaseDir=controlPath,
            icmsPkgVarBaseDir=varPath,
            icmsPkgLogBaseDir=logPath,            
            icmsPkgTmpBaseDir=tmpPath,
        )


    def cmndDesc(): """
** Set File Parameters at ../pkgInfo/fp -- By default
** TODO NOTYET auto detect marme.dev -- marme.control and decide where they should be, perhaps in /var/
"""
    

        
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Run Envs Setup/Clean*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  icmsRunEnvsPreps    [[elisp:(org-cycle)][| ]]
"""
class icmsRunEnvsPreps(cs.Cmnd):
    """
** Create run time environment directories (tmp var)
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""

####+END:

        #G = cs.globalContext.get()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  icmsRunEnvsClean    [[elisp:(org-cycle)][| ]]
"""        
class icmsRunEnvsClean(cs.Cmnd):
    """
** Remove run time environment directories (tmp var)
    opDo rm -r "${icmsRunEnvBaseDir}/tmp/${icmsPkgName}"
    opDo rm -r "${icmsRunEnvBaseDir}/var/${icmsPkgName}"
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""

####+END:

        #G = cs.globalContext.get()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  icmsRunEnvLinks    [[elisp:(org-cycle)][| ]]
"""        
class icmsRunEnvLinks(cs.Cmnd):
    """
** Create links for ../tmp ../var and ../control
    opDo rm -r "${icmsRunEnvBaseDir}/tmp/${icmsPkgName}"
    opDo rm -r "${icmsRunEnvBaseDir}/var/${icmsPkgName}"
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""

####+END:

        #G = cs.globalContext.get()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  icmsRunEnvLinksClean    [[elisp:(org-cycle)][| ]]
"""        
class icmsRunEnvLinksClean(cs.Cmnd):
    """
** Remove links of ../tmp ../var and ../control
    opDo FN_fileSymlinkRemoveIfThere "${icmsPkgBaseDir}/tmp"
    opDo FN_fileSymlinkRemoveIfThere "${icmsPkgBaseDir}/var"

    opDo FN_fileSymlinkRemoveIfThere "${controlsBaseDir}"
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""

####+END:

        #G = cs.globalContext.get()
        
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  icmsLibsLinks    [[elisp:(org-cycle)][| ]]
"""        
class icmsLibsLinks(cs.Cmnd):
    """
** Creates links in ../lib/python/
    opDo FN_fileSymlinkUpdate /de/bx/nne/dev-py/libs/icmPkg/icm ${icmsPkgBaseDir}/lib/python/icm
    opDo FN_fileSymlinkUpdate /de/bx/nne/dev-py/libs/bxMsgPkg/bxMsg ${icmsPkgBaseDir}/lib/python/bxMsg
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""

####+END:

        #G = cs.globalContext.get()

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Class-IIF    ::  icmsLibsLinksClean    [[elisp:(org-cycle)][| ]]
"""        
class icmsLibsLinksClean(cs.Cmnd):
    """
** Remove links in ../lib/python/
    opDo FN_fileSymlinkRemoveIfThere ${icmsPkgBaseDir}/lib/python/icm
    opDo FN_fileSymlinkRemoveIfThere ${icmsPkgBaseDir}/lib/python/bxMsg    
"""
    cmndParamsMandatory = []
    cmndParamsOptional = []       
    cmndArgsLen = {'Min': 0, 'Max': 0,}

####+BEGIN: bx:dblock:python:icm:cmnd:parsValidate :par ""

####+END:

        #G = cs.globalContext.get()
        

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
