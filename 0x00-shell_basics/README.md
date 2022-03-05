0. __pwd__ Prints absolute path name of the current working directory.
1. __ls__ Displays the contents list of your current directory.
2. __cd__ Changes the working directory to the user's home directory.
3. __ls -l__ Displays current directory contents in a long format.
4. __ls -la__ Displays current directory contents, including hidden files (starting with __.__).
5. __ls -na__ Displays current directory contents showing long format, with user and group IDs displayed numerically and hidden files (starting with __.__).
6. __mkdir /tmp/holberton/__ Creates a directory named __holberton__ in the __/tmp/__ directory.
7. __mv /tmp/betty /tmp/holberton/__ Moves the file __betty__ from __/tmp/__ to __/tmp/holberton__.
8. __rm /tmp/holberton/betty__ Deletes the file __betty__.
9. __rmdir /tmp/holberton/__ Deletess the directory __holberton__ that is in the __tmp__ directory.
10. __cd -__ Changes the working directory to the previous one.
11. __ls -al . .. /boot__ Lists all files (even ones with names beginning with a period character, which are normally hidden) in the curret directory and the parent of the working directory and the __/boot__ directory, in long format.
12. __file /tmp/iamafile__ Prints the type of the file named __iamafile__.
13. __ln -s /bin/ls _ls___ Creates a symbolic link to __/bin/ls__, named __ls__
14. __cp -rua *.html ../__ Copies all the HTML files from the current working directory to the parent of the working directory, but only copies files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
15. __mv [[:upper:]]* /tmp/u__ Moves all files beginning with an uppercase letter to the directory __/tmp/u__
16. __rm *~__ Deletes all files in the current working directory that ends with the character __~__.
17. __mkdir -p welcome/to/holberton__ Creates the directories __welcome__, __welcome/to/__, and __welcome/to/holberton__ in the current directory.
18. __ls -map__ Lists all files and directories of the current directory, seperated by commas (__.__).
19. __!:mime Holberton__ Creates a magic file __holberton.mgc__ that can be used with the command __file__ to detect __Holberton__ data files.
