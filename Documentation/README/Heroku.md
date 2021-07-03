heroku run bash
heroku builds:cancel

# BACKUP AND RESTORE

1. pg_dump -U postgres vggkbs_db > vggkbs_db_dumpfile
2. heroku pg:psql DATABASE_URL --app docking-vggkbs < vggkbs_db_dumpfile
3. heroku pg:reset DATABASE_URL --app docking-vggkbs --confirm docking-vggkbs

--confirm docking-vggkbs
psql -U postgres --clean -d vggkbs_db -f db.sql

# not for heroku

heroku pg:psql --app docking-vggkbs < db.sql

heroku psql:pg:pg_restore --app docking-vggkbs < db.sql

# Locally backup and restoe

pg_dump -Fc -U postgres vggkbs_db > db.sql

pg_restore --clean -U postgres -d vggkbs_db db.sql

heroku pg:backups:restore DATABASE_URL --app docking-vggkbs < db.sql

# CREATE heroku app

heroku create docking-vggkbs

# push to heroku

1. heroku stack:set container
2. git add heroku.yml
3. git commit -m "Added heroku.yml"

4. heroku git:remote -a docking-vggkbs

5. git:push
   heroku git:push heroku main
   git push heroku main

6. Optional:
   git remote remove heroku
   git add ClientApp/dist
