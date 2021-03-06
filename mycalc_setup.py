
from cx_Freeze import *

includefiles=['Calc1.ico']

base = None
if sys.platform=='win32':
    base='win32GUI'

shortcut_table=[
    [
        'DesktopShortcut',  #shortcut
        'DesktopFolder',    #Diretory_
        'My Calculator...', #name
        'TARGETDIR',        #component_
        '[TARGETDIR]:Mr.Calc.exe',  #target
        None, #argument
        None, #description
        None, #hotkey
        None, #icon
        None, #icondex
        None, #showcmd
         'TARGETDIR' #wkdir
    ]
]
msi_data= {'shortcut':shortcut_table}
bdist_msi_options= {'data': msi_data}
setup(
    version = "0.1",
    description='My Calculator...',
    author='Mohammed Huzaifa',
    name='Smart Calc !',
    options={"build_exe":{'include_files':includefiles},'bdist_msi':bdist_msi_options},
    executables=[
        Executable(
            script='mycalc.py',
            base=base,
            icon='Calc1.ico',
        )
    ]
)


