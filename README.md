
<h1 align="center">Blogs</h1>

<img src="https://github.com/gurupratap-matharu/blogs/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

## LIVE

<https://midware.herokuapp.com/api/v1/>

## Motivation 🎯

- App suggestion based on book assignment
- Deployment with docker on heroku
- Working with tools that are free for open source
- Working with payment methods like stripe and REST apis

## Features ✨

- Logs Requests and responses using logging module
- Save Requests and responses to database for persistency
- Connects with Stripe payments to creates a payment upon POST
- Versioning of api possible see `/api/v1/`
- Fast response time
- Easily customizable with Login | Logout | reset password features and rest-token authentication
- Make file for faster setup and reusability

## Development setup 🛠

Steps to locally setup development after cloning the project.

`docker-compose up -d --build`
or simple
`make build` ;)

Make sure you rename .env.example to .env and declare the environment variables in root folder for docker to pickup!
