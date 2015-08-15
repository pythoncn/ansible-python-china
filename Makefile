msg=$(shell git log -1 --pretty=%B)
revision=$(shell git rev-parse HEAD)

init:
	@ansible-playbook -vvvv --ask-vault-pass -i production playbook.yml

deploy:
	@ansible-playbook --ask-vault-pass -i production playbook.yml --tags deploy -e 'deploy_revision=${revision} deploy_message="${msg}"'
