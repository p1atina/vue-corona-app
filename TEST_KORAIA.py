import subprocess

process = subprocess.Popen("./sp_firedetect", stdout=subprocess.PIPE, shell=True)

while True:
    output = process.stdout.readline()
    if output == b'' and process.poll() is not None:
        break
    if b'CConsoleServer::initialize() [127.0.0.1:35000] initialized' in output:
        process.kill()
        subprocess.call("kill $(ps aux | grep 'sp_firedetect\|sp_yolofire' | awk '{print $2}')", shell=True)
        break
    if output:
        print(output.strip())
