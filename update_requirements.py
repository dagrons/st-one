import re
from pathlib import Path

dir_path = Path("").resolve()

deps = []
for file in dir_path.glob("**/*.py"):
    ma1 = re.compile("^\s*import\s+(\S+)")
    ma2 = re.compile("^\s*from\s+(\S+)\s+import\s+\S+")
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            re1 = ma1.match(line)
            re2 = ma2.match(line)
            if re1:
                deps.append(re1.group(1).split('.')[0])
            if re2:
                deps.append(re2.group(1).split('.')[0])
exclude_dir = [dir.name for dir in dir_path.iterdir()]
deps = set(deps) - set(exclude_dir)

with open('requirements.txt', 'w+') as f:
    f.write('\n'.join(deps))


