<a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>
<a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a>
[![Build Status](https://travis-ci.org/SimonAwiti/API-endpoints.svg?branch=master)](https://travis-ci.org/SimonAwiti/API-endpoints)


# API-endpoints

## Postman API Documentation
[API Documentation](https://documenter.getpostman.com/view/5353857/RWgjZhQb)

## The following are API endpoints enabling one to: 
* Place a new order for food.
* Get a list of orders.
* Fetch a specific order.
* Update the order status.
## Here is a list of the functioning endpoints

| EndPoint                | Functionality        | Routes            |
| :---                    |     :---:            | :---              |
| GET /orders             | Get all orders       | /api/v1/orders    |
| GET /orders/<orderId>   | Get order by order id| /api/v1/orders/id |
| POST /orders            | Adds an order        | /api/v1/orders    |
| PUT /orders             | Edit orders          | /api/v1/orders/id |
  
## Testing the endpoints

* Install python then using pip instal .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use unittest to run the the tests

## This application has been deployed on Heroku 
[click to view](https://dashboard.heroku.com/apps/fast-food-ap/logs)

# Written by: Simon Awiti
#### Copyright © Andela 2018 
