# Data-modeling-with-postgres

## **Overview**
In this project, we apply Data Modeling with PostgreSql and build an ETL pipeline using Python.
A startup wants to analyze data they've heen collecting on songs and user activity on their new music streaming app.
Data was stored in json file, after load to db, it have schema as below:

![image](https://private-user-images.githubusercontent.com/66172810/239989555-3c466d77-e7db-4586-bbd3-f56f98c86c8f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZXkxIiwiZXhwIjoxNjg0Nzc3NzY0LCJuYmYiOjE2ODQ3Nzc0NjQsInBhdGgiOiIvNjYxNzI4MTAvMjM5OTg5NTU1LTNjNDY2ZDc3LWU3ZGItNDU4Ni1iYmQzLWY1NmY5OGM4NmM4Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwNTIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDUyMlQxNzQ0MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZDAzNmIxMjhkYzIwNDc5NDljNmZlM2NiOWQ4M2Q5MzkzMTBmZTBlMzVlYmZlY2MxYjRiNzg1YWQ5ZTc2ZWE4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ucxEg3XMOuUxqMX-iizSoy9bLY_NQbMuCY8NdS8gcP8)

# Determine requirement:
- Know which song is played the most, by which artist, of what time
- Know which location use this app most.
- Know the songs heard by each user

# Data modeling:
Star schema:

![image](https://private-user-images.githubusercontent.com/66172810/239992378-d52be9b3-41b3-4bfc-8074-d661ec0d2e1d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZXkxIiwiZXhwIjoxNjg0Nzc4NTAyLCJuYmYiOjE2ODQ3NzgyMDIsInBhdGgiOiIvNjYxNzI4MTAvMjM5OTkyMzc4LWQ1MmJlOWIzLTQxYjMtNGJmYy04MDc0LWQ2NjFlYzBkMmUxZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwNTIyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDUyMlQxNzU2NDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MTdkZDZiNDEwMmE4MjVhM2RmN2NiZjZjZWQ1YTk2ZDUxMDdkMTk2ZTRjMGM3OGZhOGYzNGExMjE5OWViMjYzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.UeYn83ePBFSrRBe4VOAjtYmWQcWg1CTiy5cFY7lLUvY)
# How to run
Run bash file to load data from file to local mongoDb:
```
./extract.sh
```
Run main file to execute ```createTable```, ```loadDimTable``` and ```loadFactTable```
```
python3 main.py
```
Result if run successfully:
```
Connect to postgres successfully
Drop table successfully
Create table successfully
Done load dim location
Done load dim artist
Done load dim user
Done load dim date
Done load dim time
Done load dim song
Done load fact songPlay
```