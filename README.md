# scrapping-service

## Overview

This project implements a Facebook scrapping service using FastAPI to retrieve data from one public page. The scrapping data is saved in a database (postgresql). Both the service and the database are dockerized for easy deployment (using docker-compose.yaml). Additionally, a test is included to ensure the functionality of the scrapping service.

## Features

- Facebook scrapping using FastAPI.
- Database storage for scrapping data.
- Dockerized service and database.
- Included test for scrapping service.


### Prerequisites

- Docker installed on your machine.

### Build Facebook (1 public page)

- For this step we create a facebook page named [Scrapping service Page](https://www.facebook.com/profile.php?id=61553942488650) for the PAGE_ID  then we create a developers facebook account then a [graph api application](https://developers.facebook.com/docs/graph-api/) for the ACCESS_TOKEN. 

### Save scrapping data

- We create a app directory for this step with three files (db, main and scraper)


<div align="center">
    <img src="readme-images/browser_data.png " >
    <p>the data in browser url http://172.18.0.1/scrape</p>
</div>

<div align="center">
    <img src="readme-images/db_data.png " >
    <p>data in database</p>
</div>

### Dockerization

- This step include a Dockerfile for the FastAPI service and a docker-compose for the two container and a .env file to secure our sensitive data.

### Test

- A simple test to assert that the data exposed correctly on the browser.

<div align="center">
    <img src="readme-images/test.png " >
    <p>test the service</p>
</div>











