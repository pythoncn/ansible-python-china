init:
	@ansible-playbook -vvvv --ask-vault-pass -i production playbook.yml

deploy:
	@ansible-playbook --ask-vault-pass -i production playbook.yml --tags deploy
