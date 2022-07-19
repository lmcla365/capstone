# capstone

DEPLOY STACK
aws cloudformation deploy --template-file ./NULLstack.json --stack-name NULLstack --parameter-overrides KeyName=NULLkey --tags course=IEA cohort=7

GET OUTPUTS
aws cloudformation describe-stacks --stack-name NULLstack

DELETE STACK
aws cloudformation delete-stack --stack-name NULLstack

RUN ANSIBLE PLAYBOOK (run from ansible dir/use describe-stacks to update hosts file) 
sudo ansible-playbook playbook_final.yaml

INSTALL BAMBOO (run from infra)
sudo docker run --log-driver=splunk --log-opt splunk-token=9df68219-4642-41cc-ad0d-f60ca01c1062 --log-opt splunk-url=https://prd-p-s74ir.splunkcloud.com:8088 --log-opt splunk-insecureskipverify="true" --log-opt tag="{{.ImageName}}/{{.Name}}/{{.ID}}" --group-add $(getent group docker | cut -d ":" -f 3) -v /var/run/docker.sock:/var/run/docker.sock -v /mnt/bamboo:/var/atlassian/application-data/bamboo --name="bamboo" --init -d -p 54663:54663 -p 8085:8085 jrrickerson/capstone-bamboo
