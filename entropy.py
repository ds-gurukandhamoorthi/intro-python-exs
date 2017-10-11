from strutils import metric_entropy
with open('/usr/share/dict/words') as words:
    for line in words:
        line = line.strip()
        print(metric_entropy(line), line, sep='\t')
