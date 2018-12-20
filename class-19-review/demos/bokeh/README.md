# Stock Portfolio

- **Author**: Hannah Sindorf
- **Version**: 1.1.0

## Overview
Stock portfolio that allows users to search for a company and add to their stock portfolio

## Getting Started
1. Visit [http://ec2-54-202-13-238.us-west-2.compute.amazonaws.com/](http://ec2-54-202-13-238.us-west-2.compute.amazonaws.com/)
2. Click 'Portfolio' to view portfolio
3. Click 'search to search for new stocks'
    - if you have already added the stock you will just be taken to your portfolio
    - if the stock is not found you will get a 404

## Architecture

### Tools used
- Python
- Flask
  - Flask-WTF
  - Flask-SQLAlchemy
- Postgres database

### Deployment

- deployed on amazon EC2
- database on AWS RDS
- Uses nginx as proxy to serve externally
- gunicorn to serve site to proxy

## Credits
Tips I've found on the internet that helped me out.

- [How to tell if variable exists in flask session](https://stackoverflow.com/questions/28925602/how-can-i-detect-whether-a-variable-exists-in-flask-session)
- [create-dynamic-urls-in-flask-with-url-for](https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for)
- [don't escape something jinja](https://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2)
- [how to plot by datetime bokeh](https://stackoverflow.com/questions/33869292/how-can-i-set-the-x-axis-as-datetimes-on-a-bokeh-plot)

## Change Log

- 1.1.0 12-12-2018 06:00p: Added functionality to site to choose whether or not to add a company after searching
- 1.0.0 12-06-2018 05:00p: Deployed on AWS, added companies showing on portfolio
- 0.2.0 12-06-2018 09:43a: Basic database implemented
- 0.1.0 12-05-2018 06:00p: Basic rendering/ form
