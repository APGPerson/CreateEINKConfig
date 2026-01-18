import shutil,os
import socketserver
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
src = Path.cwd() / "output" / "data.json"
dst = Path.cwd() / "dist" / "data.json"
if __name__ == "__main__":
    if dst.is_file():
        os.remove(dst)
    shutil.copy(src,dst)
    os.chdir(Path.cwd() / "dist")
    with socketserver.TCPServer(("",8000),SimpleHTTPRequestHandler) as httpserver:
        print("serving at port 8000")
        httpserver.serve_forever()
