from time import sleep
import paramiko
ssh = paramiko.SSHClient()
host = '192.168.86.61'
UserName = 'pabsgaming'
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=UserName)


print('Done')
for x in range(5):
    stdin, stdout, stderr = ssh.exec_command('DISPLAY=:0 xdotool getactivewindow key ')
    print('done')
    sleep(1)
sleep(1)
