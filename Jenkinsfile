pipeline {
  agent any
  stages {
    stage('Building, Running, Testing Flask app') {
      parallel {
        stage('Build and Running Flask app') {
          steps {
            bat 'docker-compose up'
          }
        }

        stage('Testing') {
          steps {
            sleep 90
            script {
              if(env.BRANCH_NAME != 'master' && env.BRANCH_NAME != 'release' && env.BRANCH_NAME != 'develop'){
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

        stage('Docker images down') {
          steps {
            sleep 150
            script {
              if(env.BRANCH_NAME != 'master'){
                bat 'docker-compose down'
              }
            }

          }
        }

      }
    }
  }
}

