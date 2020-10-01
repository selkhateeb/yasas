import pexpect

p = pexpect.spawn('python yasas.py')
p.expect('Username: ')
p.sendline('anonymous')
p.expect('Password: ')
p.sendline('123')
p.expect("('anonymous', '123')")