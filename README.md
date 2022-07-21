# capstone

### DEPLOY STACK
 - aws cloudformation deploy --template-file ./NULLstack.json --stack-name NULLstack --parameter-overrides KeyName=NULLkey --tags course=IEA cohort=7

### GET OUTPUTS
 - aws cloudformation describe-stacks --stack-name NULLstack

### DELETE STACK
 - aws cloudformation delete-stack --stack-name NULLstack

### INSTALL DOCKER, DOCKER EBS VOLUMES, AND SPLUNK ON EC2 INSTANCES. 
 - RUN ANSIBLE PLAYBOOK (run from ansible dir/use describe-stacks to update hosts file) 
 - sudo ansible-playbook playbook_final.yaml

### INSTALL BAMBOO
#### ANSIBLE
 - sudo ansible-playbook ansible-bamboo-install.yaml
 - NOTE: Bamboo Projects, Plans, and Tasks are manually created.

#### CMD LINE (run from infra)
 - sudo docker run --log-driver=splunk --log-opt splunk-token=9df68219-4642-41cc-ad0d-f60ca01c1062 --log-opt splunk-url=https://prd-p-s74ir.splunkcloud.com:8088 --log-opt splunk-insecureskipverify="true" --log-opt tag="{{.ImageName}}/{{.Name}}/{{.ID}}" --group-add $(getent group docker | cut -d ":" -f 3) -v /var/run/docker.sock:/var/run/docker.sock -v /mnt/bamboo:/var/atlassian/application-data/bamboo --name="bamboo" --init -d -p 54663:54663 -p 8085:8085 jrrickerson/capstone-bamboo

### INSTALL WORDPRESS AND MYSQL
#### Utilize Bamboo build pipeline
 - Bamboo tasks are using the docker-compose.yaml file to deploy and confiure Wordpress and MYSQL.
 - Task is using the command line of 'sudo docker-compose up -d' to build the environment.

#### PYBLOG BUILD
 - Python project using pytest and flake8 to test code.
Bamboo is running the automaiton to build a docker image and store it in docker hub.
