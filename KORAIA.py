import subprocess

process = subprocess.Popen("./sp_firedetect", stdout=subprocess.PIPE, shell=True)

while True:
    output = process.stdout.readline()
    if output == b'' and process.poll() is not None:
        break
    if b'mpeg4' in output:
        process.terminate()
        break
    if output:
        print(output.strip())