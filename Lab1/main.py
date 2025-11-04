import subprocess
import valMin
import valMax
import valMedie
import valMediana
import valNorm
import weightedSum

result = subprocess.run(
    ["python", "valMin.py"], capture_output=True, text=True
)

result = subprocess.run(
    ["python", "valMax.py"], capture_output=True, text=True
)

result = subprocess.run(
    ["python", "valMedie.py"], capture_output=True, text=True
)

result = subprocess.run(
    ["python", "valMediana.py"], capture_output=True, text=True
)

result = subprocess.run(
    ["python", "valNorm.py"], capture_output=True, text=True
)

result = subprocess.run(
    ["python", "weightedSum.py"], capture_output=True, text=True
)