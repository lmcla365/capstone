# capstone

DEPLOY STACK
aws cloudformation deploy --template-file ./NULLtest.json --stack-name NULLstack --parameter-overrides KeyName=NULLkey --tags course=IEA cohort=7

GET OUTPUTS
aws cloudformation describe-stacks --stack-name NULLstack

DELETE STACK
aws cloudformation delete-stack --stack-name NULLstack

RUN ANSIBLE PLAYBOOK
ansible-playbook <path>/playbook.yml
