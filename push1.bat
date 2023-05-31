git init
set a1=%DATE:~-2,2%%DATE:~-7,2%%DATE:~-10,2%
git checkout -b "%a1%"
git add .
git commit -m "added_ "%a1%""
git remote add origin https://github.com/aa3110/q2.git
git push --force origin
pause