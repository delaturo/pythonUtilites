pyinstaller --clean -i ..\src\icn.ico --distpath ..\dist\Win --add-data="..\src\icn.ico;." -F -w ..\src\keepMeAwake.py
copy /y ..\src\icn.ico  ..\dist\Win\icn.ico