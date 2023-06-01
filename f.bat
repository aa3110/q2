7z a "%date%".7z chart\*.* alerts\*.*  -r
copy "%date%".7z d:\backup\
copy "%date%".7z f:\backup
del "%date%".7z
pause