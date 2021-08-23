import os
import thej

def fixStr(string: str):
  return str(string).replace("\\n", "\n").replace("('", "").replace("',)", "")

print("Test.")
