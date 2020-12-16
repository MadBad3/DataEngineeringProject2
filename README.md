# DataEngineeringProject2
Web application for NLP into docker containers

The web application will get an input key words from the user, and will return him the top 20 most similar tweets of Donald J. Trump twitter account.

- Clone the project into a directory, then do this command: `docker-compose up`

The application will build an image and run it in a docker container on localhost on port 5000.

- Then to try the integration tests functions, enter this command into a new terminal at the same directory of the docker container: `python unit_tests.py`

- Then to try the stress tests functions, enter this command into a new terminal at the same directory of the docker container: `python stress_tests.py`

If you want to train the model again you should delete the model.pkl, because after the train it will load a new one, and you should do this command to train: `python model.py`

You can also train the model by running model.ipynb which is the python notebook for the model.

You can monitor the application by installing Prometheus, and Node Exporter. Then run the them.

After install and run Grifana on the port that you want.
