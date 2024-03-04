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
    <li>Change directory to the copied repositry into the repository and buld the docker containers using the command: <b>$ docker-compose build</b></li>
    <li>Open the web application container: <b>$ docker-compose run web bash</b></li>
    <li>Within the web application container, run the base configuration file: <b>$ bash ./initapp.sh && exit</b></br>You will be prompted to enter the details of the superuser</li>
  </ol>
</p>
