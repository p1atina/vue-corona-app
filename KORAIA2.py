import subprocess

process = subprocess.Popen("./sp_firedetect", stdout=subprocess.PIPE, shell=True)

print("실행타나요?")

while True:
    output = process.stdout.readline()
    print("실행타나요? 111")
    if output == b'' and process.poll() is not None:
        print("실행타나요?첫번째")
        break
    if b'mpeg4' in output:
        process.terminate()
        print("실행타나요? 두번째")
        break
    if output:
        print(output.strip())
        print("실행타나요? 세번째")
