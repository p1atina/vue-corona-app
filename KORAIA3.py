import subprocess

process = subprocess.Popen("./sp_firedetect", stdout=subprocess.PIPE, shell=True)

print("||||First")

while True:
    output = process.stdout.readline()
    print("||||First 0000")
    if output == b'' and process.poll() is not None:
        print("||||F11111")
        break
    if b'mpeg4' in output:
        process.terminate()
        print("||||F22222")
        break
    if output:
        print(output.strip())
        print("||||F33333")