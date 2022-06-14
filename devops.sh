#! /bin/bash
COMPOSE="docker-compose"
COPIED=false
export LOC=${LOC:-local}

function install() {
  #if file does not exist
  if [ ! -f docker-compose.yml ] && [ ! -f vue.config.js ];then
    cp .deploy/${LOC}/docker-compose.yml docker-compose.yml || true
    cp .deploy/${LOC}/vue.config.js frontend-ui/vue.config.js || true
    COPIED=true
  fi
}

function cleanUp() {
  if [ "$COPIED" = true ];then
    rm docker-compose.yml
    rm frontend-ui/vue.config.js
  fi
}

if [ $# -gt 0 ]
then
  if [ "$1" == "exit" ];then
    install
    $COMPOSE down
    cleanUp
  elif [ "$1" == "runserver" ];then
    install
    shift 1
    $COMPOSE run --rm \
      backend-part \
      gunicorn vote_app_backend.wsgi:application "$@"
    cleanUp
  elif [ "$1" == "migrate" ];then
    install
    $COMPOSE run --rm \
      backend-part \
      python manage.py migrate
    cleanUp
  elif [ "$1" == "makemigrations" ];then
    install
    $COMPOSE run --rm \
      backend-part \
      python manage.py makemigrations showvotes
    cleanUp
  elif [ "$1" == "flush" ];then
    install
    $COMPOSE run --rm \
      backend-part \
      python manage.py flush
    cleanUp
  elif [ "$1" == "npm" ]; then
    install
    shift 1
    $COMPOSE run --rm \
      frontend-part \
      npm run serve "$@"
    cleanUp
  elif [ "$1" == "test" ];then
    install
    shift 1
    $COMPOSE run --rm \
      backend-part \
      pytest "$@"
    cleanUp
  elif [ "$1" == "push" ];then 
    git add * && \
    git commit -m "$2" && \
    shift 2
    git push "$@"
  elif [ "$1" == "pullserver" ];then
    #check if .env exists
    if [ -f .env ]; then
      #import environment variables from .env
      export $(cat .env | xargs)
      #check if GITHUB_USER and GITHUB_TOKEN strings exist in .env
      if grep -Fq GITHUB_USER .env && grep -Fq GITHUB_TOKEN .env
      then
        #check if variables are unset
        if [ -z "$GITHUB_USER" ] && [ -z "$GITHUB_TOKEN" ];then
          echo "environment variables unset in .env file"
        else
          ./pullserverbot.exp $GITHUB_USER $GITHUB_TOKEN
        fi
      else
        echo "environment variables missing in .env file"
      fi
    else
      echo ".env file missing"
    fi
  elif [ "$1" == "sshserver" ];then
    if [ -f .env ]; then
      export $(cat .env | xargs)
      if grep -Fq SERVER_USER .env && grep -Fq SERVER_IP .env && grep -Fq SERVER_PASSPHRASE .env
      then
        if [ -z "$SERVER_USER" ] && [ -z "$SERVER_IP" ] && [ -z "$SERVER_PASSPHRASE" ];then
          echo "environment variables unset in .env file"
        else
          ./sshserverbot.exp $SERVER_USER $SERVER_IP $SERVER_PASSPHRASE
        fi
      else
        echo "environment variables missing in .env file"
      fi
    else
      echo ".env file missing"
    fi
  else
    install
    $COMPOSE "$@"
    cleanUp
  fi
else
  install
  $COMPOSE up
  cleanUp
fi
