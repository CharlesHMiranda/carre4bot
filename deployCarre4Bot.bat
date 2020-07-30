@echo on
exit

git init
heroku git:remote --app carre4bot
echo worker: python src/core.py > Procfile
git add .
git commit -m "Deploying carre4boat"
git push heroku master
heroku ps:scale worker=1
heroku ps
heroku logs --tail
