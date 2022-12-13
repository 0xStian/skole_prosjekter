import zlib
import sys

with open(sys.argv[1], "rb") as f:
    data = f.read()
    
compressed_data = zlib.compress(data)
Decompressed_data = zlib.decompress(compressed_data)
exec(Decompressed_data)