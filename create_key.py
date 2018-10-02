default_file = '/root/.ssh/id_rsa'
filee = file(default_file)
key=""
out = filee.read()
for line in out.split('\n'):
    key = key + line + '\\n'

print key

