<h2>Containers structure</h2>
<p>The applciation has been deployed in 4 containers: <br/>
  <ol>
    <li>The web application container (django app)</li>
    <li>The web server (nginx)</li>
    <li>The Postgres administration server</li>
    <li>The relational database management server (Postgres)</li>
  </ol>
</p>
<h2>Deployment steps</h2>
<p>
  <ol>
    <li>Make a copy of the projecct to the deployment server</li>
    <li>Change directory to the copied repositry and from within the repository buld the docker containers using the command: <b>$ docker-compose build</b></li>
    <li>Open the web application container: <b>$ docker-compose run web bash</b></li>
    <li>Within the web application container, run the base configuration file: <b>$ bash ./initapp.sh && exit</b></br>You will be prompted to enter the details of the superuser</li>
    <li>Generate an SSL Certificatte store it undern <b>./nginx/certs</b></li>
    <li>Switch to production configuration by commenting the following line <b>command: bash -c "python manage.py makemigrations  && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"</b> on the Dockercompse file, and uncommenting the following <b>command: bash -c "python manage.py makemigrations && python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --certfile=/etc/certs/localhost.crt --keyfile=/etc/certs/localhost.key provider_mngt.wsgi:application --bind 0.0.0.0:443"</b></li>.<br/>Replace <b>localhost.key</b> by the actual SSL Certification file name.
    <li>Run the container: <b>$ docker-compose up -d</b></li>
  </ol>
</p>

