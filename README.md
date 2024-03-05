<h2>Containers structure</h2>
<p>The applciation has been deployed in 4 containers: <br/>
  <ol>
    <li>The web application container (django app) that exposes  on dev configuration the port 8000</li>
    <li>The web server (nginx) through which the web application will be accessed on 443</li>
    <li>The Postgres administration server that exposes the 80 as 8001</li>
    <li>The relational database management server (Postgres)</li>
  </ol>
</p>
<h2>Switching to production settings</h2>
<p>For developement and debuging purse some paremeters have been set, while moving to production make sure the following is done:<br/>
<ol>
  <li>Change the credentials details in the file <b>./web/.env</b></li>
  <li>Set the <b>DEBUG</b> variable to <b>0</b> to disable the debug mode</li>
  <li>Within the <b>docker-compose</b> file, update the <b>pg_admin</b> container credentials as required</li>
  <li>Within the <b>docker-compose</b> file, update the <b>web</b> container parmeters by commenting the <b>port</b> section. This will the keept the server from exposing internal ports</li>
</ol>
</p>
<h2>Deployment steps</h2>
<p>
  <ol>
    <li>Make a copy of the projecct to the deployment server</li>
    <li>Under the repository web/ create a file named .env with the content below: <br/>
      DEBUG=0<br/>
      SECRET_KEY="django-insecure-yx%@%k82qg7_*^y^%sxblp8or-ksxx30n%^3+3-^7kawt2x%lh"<br/>
      DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 142.93.46.193 web<br/>
      CSRF_TRUSTED_ORIGINS=http://localhost:1337 http://nginx https://nginx http://web https://web https://localhost http://localhost<br/>
      ENGINE=django.contrib.gis.db.backends.postgis<br/>
      DATABASE=providers_dev<br/>
      DB_USER=django_admin<br/>
      DB_PASSWORD=hello_django<br/>
      DB_HOST=db<br/>
      DB_PORT=5432<br/>
    </li>
    <li>Change directory to the copied repositry and from within the repository buld the docker containers using the command: <b>$ docker-compose build</b></li>
    <li>Open the web application container: <b>$ docker-compose run web bash</b></li>
    <li>Within the web application container, run the base configuration file: <b>$ bash ./initapp.sh && exit</b></br>You will be prompted to enter the details of the superuser</li>
    <li>Generate an SSL Certificatte store it undern <b>./nginx/certs</b></li>
    <li>Switch to production configuration by commenting the following line <b>command: bash -c "python manage.py makemigrations  && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"</b> on the Dockercompse file, and uncommenting the following <b>command: bash -c "python manage.py makemigrations && python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --certfile=/etc/certs/localhost.crt --keyfile=/etc/certs/localhost.key provider_mngt.wsgi:application --bind 0.0.0.0:443"</b></li>.<br/>Replace <b>localhost.key</b> by the actual SSL Certification file name.
    <li>Run the container: <b>$ docker-compose up -d</b></li>
  </ol>
</p>


