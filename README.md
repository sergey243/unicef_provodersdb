<h2>Deployment steps</h2>
<p>
  <ol>
    <li>Make a copy of the projecct to the deployment server</li>
    <li>Change directory to the copied repositry into the repository and buld the docker containers using the command: <b>\&gt;docker-compose build</b></li>
    <li>Open the web application container: <b>docker-compose run web bash</b></li>
    <li>Within the web application container, run the base configuration file: <b>\&gt;bash ./initapp.sh && exit</b></br>You will be prompted to enter the details of the superuser</li>
  </ol>
</p>
