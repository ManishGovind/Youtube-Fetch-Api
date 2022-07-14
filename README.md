# Youtube-Fetch-Api

# Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Functionalities covered :

- Server calls the YouTube API continuously in background using celery  with some interval for fetching the latest videos for a predefined search query and store the data of videos (such as Video title, description, publishing datetime, thumbnails URLs etc) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerization of the  project.

# Instructions to start App locally :
### Using Docker :
```bash
  # Clone the repository
  $ git clone https://github.com/ManishGovind/Youtube-Fetch-Api.git
  $ cd FetchApi/
  # Set up the  following settings attrbutes and run below commad  ,  
  $ docker-compose up -d --build  
  ```
* Incase you have problems related to docker and processes running  , remove all the volumes and containers :
```
   $ docker rm $(docker ps -a -q)
```   
API and Settings 
* Visit http://localhost:8000/api/get-videos/
* configure the following as per requirement  in settings.py file  from FetchApi/FetchApi/settings.py  :
  - **`DEVELOPER_KEY`:**  youtube Api key
  - **`SEARCH_QUERY`:**  search query
  - **`MAX_RESULTS`:** The max number of results to fetch from youtube api 
  - **`REST_FRAMEWORK.PAGE_SIZE`:** The size of the paginated response 
