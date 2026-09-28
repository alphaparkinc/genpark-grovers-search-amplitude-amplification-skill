import sys
import json
from client import GroverSearch

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "grover_search_simulate",
                        "description": "Simulate Grover's amplitude amplification iterations for unstructured database search",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "num_items": {"type": "integer"},
                                "target_index": {"type": "integer"},
                                "iterations": {"type": "integer", "default": 1}
                            },
                            "required": ["num_items", "target_index"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "grover_search_simulate":
            g = GroverSearch(args["num_items"], args["target_index"])
            for _ in range(args.get("iterations", 1)):
                g.step()
            prob = g.get_target_probability()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"target_probability": prob, "amplitudes": g.state})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
