
<h1 align="center">Blogs</h1>

<img src="https://github.com/gurupratap-matharu/blogs/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

## LIVE

<https://pondering-thoughts.herokuapp.com/>

## Motivation 🎯

- Development of personal blog site
- Deployment with docker on heroku
- Working with tools that are free for open source
- Working with databases, markdown, ci/cd tools and unit testing

## Features ✨

- Light and dark modes
- Markdown support
- Full text search support using django postgres awesome combination
- Send email notifications
- Share blogs via loved ones
- Custom template tags and template filters for quick access
- API (coming soon)

## Development setup 🛠

Steps to locally setup development after cloning the project.

`docker-compose up -d --build`

or simply

`make build`

Make sure you rename .env.example to .env and declare the environment variables in root folder for docker to pickup!
