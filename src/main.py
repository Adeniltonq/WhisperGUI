import subprocess


response = subprocess.run(['./whisper.cpp/build/bin/whisper-cli'])

print(response)