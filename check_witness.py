# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Steven Minh Phat Duong
"""Verify the published Q8 local-identifying-code witness (standard library)."""
from pathlib import Path
import hashlib
import json

def verify(path):
    path = Path(path)
    words = path.read_text().split()
    if len(words) != 40 or len(set(words)) != 40:
        raise ValueError("Expected exactly 40 distinct codewords")
    if any(len(word) != 8 or set(word) - {"0", "1"} for word in words):
        raise ValueError("Every codeword must be an eight-bit binary string")
    code = {int(word, 2) for word in words}
    signatures = {
        v: ({v} | {v ^ (1 << i) for i in range(8)}) & code
        for v in range(256)
    }
    if not all(signatures.values()):
        raise ValueError("Witness does not dominate every vertex")
    edges = [(v, v ^ (1 << i)) for v in range(256)
             for i in range(8) if v < (v ^ (1 << i))]
    if len(edges) != 1024 or any(signatures[u] == signatures[v] for u, v in edges):
        raise ValueError("Witness does not separate every adjacent pair")
    return {"codewords": 40, "vertices_covered": 256, "edges_separated": 1024,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "status": "PASS"}

if __name__ == "__main__":
    print(json.dumps(verify(Path(__file__).with_name("q8_k40.txt")), indent=2))
