# action-server-example-python

Action Server example, written in Python

## Deployment

Below you will find instructions to deploy this Action Server example to Heroku.

Prerequisites:

- Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
- Create a Heroku account (if you don't have one already)
- Clone this repository: `git clone git@github.com:botpress/action-server-example-python.git`
- `cd action-server-example-python`

Now deploy the app:

1. `heroku login`
2. `heroku create`
3. `git push heroku master`
4. Set the `BOTPRESS_SERVER_URL` to the public URL of your Botpress server, e.g. `https://34.56.178.34:3000` or `https://botpress.mydomain.com`, using the following command: `heroku config:set BOTPRESS_SERVER_URL={your Botpress server URL}`
