# -*- mode: python -*-

block_cipher = None


a = Analysis(['buscaminas.py'],
             pathex=['C:\\Users\\Francisco Dadone\\OneDrive\\Documentos\\Programacion\\Python\\Proyectos\\Buscaminas\\Version 2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='buscaminas',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='img\\bomba.ico')
