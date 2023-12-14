# Star Wars Project
This project involves pulling data on all available starships from the [Star Wars API](https://swapi.dev/). The API provides information about various entities in the Star Wars universe, including starships and characters.

## Data Source
The data used in this project has been sourced from the [Star Wars API](https://swapi.dev/). The API provides a RESTful interface to access a wealth of information about Star Wars, including details about starships and characters.

## Task Overview
The primary task of this project is to pull data on all available starships from the API. The "pilots" key in the starships data contains URLs pointing to the characters who pilot the starship. 

The goal is to replace 'pilots' with a list of ObjectIDs from our characters collection. After this transformation, the starships data will be inserted into its own collection.

## Implementation
To achieve this task, Python scripts have been developed. The following steps outline the process:


## - Data Retrieval:
- Utilize the requests library to fetch data on all available starships from the Star Wars API.

## - Data Transformation:
- Implement functions to transform the starships data, specifically replacing 'pilots' with a list of ObjectIDs from our characters collection.
- Insertion into Collection: Use functions to insert the transformed starships data into its own collection.

## Requiremnts:
- Latest Python version (3.11)
- MongoDB 5.0 or later
  - MongoDB Compass
  - MongoDB Shell
  - MongoDB Database Tools
- pip install pymongo

## Amazing Contributers:
- Jesse Rolfe (<https://github.com/jvrolfe>)
- T Oladimeji (<https://github.com/T-meji>)
- Medan Grant-Anderson (<https://github.com/MedanG-A>)
- Aymen Shallal (<https://github.com/Shalala06>)
- Seb Manley (<https://github.com/SebManley>)
- Richard Van Parys (<https://github.com/ReggieVP>)
