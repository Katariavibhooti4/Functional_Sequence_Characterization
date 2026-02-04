from Bio import SeqIO
from collections import Counter

record = SeqIO.read("data/input_sequence.fasta", "fasta")

seq = record.seq
length = len(seq)

aa_count = Counter(seq)
total = sum(aa_count.values())

print("Sequence ID:", record.id)
print("Sequence Length:", length)
print("\nAmino Acid Composition:")
for aa, count in aa_count.items():
    print(f"{aa}: {count} ({count/total*100:.2f}%)")

with open("results/qc_summary.txt", "w") as f:
    f.write(f"Sequence ID: {record.id}\n")
    f.write(f"Length: {length}\n")
    f.write("Amino Acid Composition:\n")
    for aa, count in aa_count.items():
        f.write(f"{aa}: {count}\n")
