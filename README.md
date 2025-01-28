# Overview

This is an attempt to get the grasp of using an integrated database.
Using SQLite I made a simple receipt tracker. One thing I have a hard time with is remembering what the hieroglyphics on a receipt actually mean. So I made this application to not only store the receipts I have but to also store my own descriptions of what ever CHCLV ORANGE PEEL DA and other such codes mean. Right now the program is fully manual. You'd have to type everything in, but in the future perhaps you can scan the receipts can feed that in instead.


[Software Demo Video](https://youtu.be/SWHXwMk3yEg)  

# Relational Database

I'm using SQLite which is just built right into python making it easy. 
I only have three tables in this data base. One for every receipt (store, date, amount spent, etc), one for every item (store description, my own if I can figure out what it was), and since prices change all the time I have a relational table connecting the receipt to it's items and a third column storing the prices of those items on that day.

# Development Environment

I used just simple python and the splite3 library

# Useful Websites

- [SQLITE Tutorial](https://www.sqlitetutorial.net/)
- [ChatGPT](https://chatgpt.com/)
- [SQLite Databases With Python - Full Course](https://www.youtube.com/watch?v=byHcYRpMgI4&t=6s)

# Future Work

- The program doesn't run yet. It needs the ability to query and to more cleanly add receipts