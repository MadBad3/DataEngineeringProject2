pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        bat 'docker build -t myflaskapp .'
      }
    }
    stage('Run Flask App'){
      steps{
        bat 'docker run -d -p 5000:5000 --name myflaskapp_c myflaskapp'
      }
    }
    stage('Testing'){
      steps{
        script{
          if(env.BRANCH_NAME == 'web_interface'){
            echo "We are in feature branch, will run unit tests !"
	    bat 'python unit_tests.py'
	    echo "Going to proceed with push into develop branch !"
          }else if(env.BRANCH_NAME == 'develop'){
	    echo "We are in develop branch, will run stress tests !"
	    bat 'python stress_tests.py'
	    echo "Going to proceed to push into release branch !"
          }else if(env.BRANCH_NAME == 'release'){
            echo "We are in release branch !"
	    input "proceed with deployment to live ?"
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if(env.BRANCH_NAME != 'master'){
            bat 'docker rm -f myflaskapp_c'
            bat 'docker rmi -f myflaskapp'
          }
        }
      }
    }
  }
}
