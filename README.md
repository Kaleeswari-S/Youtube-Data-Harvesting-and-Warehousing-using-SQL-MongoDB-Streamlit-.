# Youtube-Data-Harvesting-and-Warehousing-using-SQL-MongoDB-Streamlit.

## DOMAIN:
**Social Media**

## PROBLEM STATEMENT:

The task is to build a Streamlit app that permits users to analyze data from multiple YouTube channels. Users can input a YouTube channel ID to access data like channel information, video details, and user engagement. The app should facilitate storing the data in a MongoDB database and allow users to collect data from up to 10 different channels. Additionally, it should offer the capability to migrate selected channel data from the data lake to a SQL database for further analysis. The app should enable searching and retrieval of data from the SQL database, including advanced options like joining tables for comprehensive channel information.

## SKILLS TAKE AWAY FROM THIS PROJECT:
- Python scripting
- Data Collection
- MongoDB
- Streamlit
- API integration
- Data Management using MongoDB (Atlas) and SQL

## TOOLS TO BE USED :

* *Streamlit* library was used to create a user-friendly UI that enables users to interact with the programme and carry out data retrieval and analysis operations.

* *Python* is a powerful programming language renowned for being easy to learn and understand. Python is the primary language employed in this project for the development of the complete application, including data retrieval, processing, analysis, and visualisation.

* *MongoDB* is built on a scale-out architecture that has become popular with developers of all kinds for developing scalable applications with evolving data schemas. As a document database, MongoDB makes it easy for developers to store structured or unstructured data. It uses a JSON-like format to store documents.

* *PostgreSQL* is an open-source, advanced, and highly scalable database management system (DBMS) known for its reliability and extensive features. It provides a platform for storing and managing structured data, offering support for various data types and advanced SQL capabilities.

## APPROACH:

1. Start by setting up a Streamlit application using the python library "streamlit", which provides an easy-to-use interface for users to enter a YouTube channel ID, view channel details, and select channels to migrate.
2. Establish a connection to the YouTube API V3, which allows me to retrieve channel and video data by utilizing the Google API client library for Python. 
3. Store the retrieved data in a MongoDB data lake, as MongoDB is a suitable choice for handling unstructured and semi-structured data. This is done by firstly writing a    method to retrieve the previously called api call and storing the same data in the database in 3 different collections.
4. Transferring the collected data from multiple channels namely the channels,videos and comments to a SQL data warehouse, utilizing a SQL database like MySQL or PostgreSQL for this purpose.
5. Utilize SQL queries to join tables within the SQL data warehouse and retrieve specific channel data based on user input. For that the SQL table previously made has to be properly given the the foreign and the primary key. 

## CONCLUSION:

This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on a YouTube channel, stores it in a MongoDB database, migrates it to a SQL data warehouse, and enables users to search for channel details and join tables to view data in the Streamlit app.

*Please watch my application demo video in below link and let me know your feedbacks.*

Video URL : https://lnkd.in/g3Pj7dK4
