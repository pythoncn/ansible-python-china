init:
	@ansible-playbook -vvvv --ask-vault-pass -i production playbook.yml
