@echo on

git init
heroku git:remote --app carre4bot
git add .
git commit -m "Deploying carre4boat"
