# 3475. DNA Pattern Recognition 

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/dna-pattern-recognition/](https://leetcode.com/problems/dna-pattern-recognition/)  
**Topics:** Database

---

## 📝 Problem Statement

Table: `Samples`

```

+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| sample_id      | int     |
| dna_sequence   | varchar |
| species        | varchar |
+----------------+---------+
sample_id is the unique key for this table.
Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.

```

Biologists are studying basic patterns in DNA sequences. Write a solution to identify `sample_id` with the following patterns:

	- Sequences that **start** with **ATG** (a common **start codon**)

	- Sequences that **end** with either **TAA**, **TAG**, or **TGA** (**stop codons**)

	- Sequences containing the motif **ATAT** (a simple repeated pattern)

	- Sequences that have **at least** `3` **consecutive** **G** (like **GGG** or **GGGG**)

Return *the result table ordered by **sample_id in **ascending** order*.

The result format is in the following example.

 
Example:

**Input:**

Samples table:

+-----------+------------------+-----------+
| sample_id | dna_sequence     | species   |
+-----------+------------------+-----------+
| 1         | ATGCTAGCTAGCTAA  | Human     |
| 2         | GGGTCAATCATC     | Human     |
| 3         | ATATATCGTAGCTA   | Human     |
| 4         | ATGGGGTCATCATAA  | Mouse     |
| 5         | TCAGTCAGTCAG     | Mouse     |
| 6         | ATATCGCGCTAG     | Zebrafish |
| 7         | CGTATGCGTCGTA    | Zebrafish |
+-----------+------------------+-----------+

**Output:**

+-----------+------------------+-------------+-------------+------------+------------+------------+
| sample_id | dna_sequence     | species     | has_start   | has_stop   | has_atat   | has_ggg    |
+-----------+------------------+-------------+-------------+------------+------------+------------+
| 1         | ATGCTAGCTAGCTAA  | Human       | 1           | 1          | 0          | 0          |
| 2         | GGGTCAATCATC     | Human       | 0           | 0          | 0          | 1          |
| 3         | ATATATCGTAGCTA   | Human       | 0           | 0          | 1          | 0          |
| 4         | ATGGGGTCATCATAA  | Mouse       | 1           | 1          | 0          | 1          |
| 5         | TCAGTCAGTCAG     | Mouse       | 0           | 0          | 0          | 0          |
| 6         | ATATCGCGCTAG     | Zebrafish   | 0           | 1          | 1          | 0          |
| 7         | CGTATGCGTCGTA    | Zebrafish   | 0           | 0          | 0          | 0          |
+-----------+------------------+-------------+-------------+------------+------------+------------+

**Explanation:**

	Sample 1 (ATGCTAGCTAGCTAA):
	
		- Starts with ATG (has_start = 1)

		- Ends with TAA (has_stop = 1)

		- Does not contain ATAT (has_atat = 0)

		- Does not contain at least 3 consecutive 'G's (has_ggg = 0)

	
	
	Sample 2 (GGGTCAATCATC):
	
		- Does not start with ATG (has_start = 0)

		- Does not end with TAA, TAG, or TGA (has_stop = 0)

		- Does not contain ATAT (has_atat = 0)

		- Contains GGG (has_ggg = 1)

	
	
	Sample 3 (ATATATCGTAGCTA):
	
		- Does not start with ATG (has_start = 0)

		- Does not end with TAA, TAG, or TGA (has_stop = 0)

		- Contains ATAT (has_atat = 1)

		- Does not contain at least 3 consecutive 'G's (has_ggg = 0)

	
	
	Sample 4 (ATGGGGTCATCATAA):
	
		- Starts with ATG (has_start = 1)

		- Ends with TAA (has_stop = 1)

		- Does not contain ATAT (has_atat = 0)

		- Contains GGGG (has_ggg = 1)

	
	
	Sample 5 (TCAGTCAGTCAG):
	
		- Does not match any patterns (all fields = 0)

	
	
	Sample 6 (ATATCGCGCTAG):
	
		- Does not start with ATG (has_start = 0)

		- Ends with TAG (has_stop = 1)

		- Starts with ATAT (has_atat = 1)

		- Does not contain at least 3 consecutive 'G's (has_ggg = 0)

	
	
	Sample 7 (CGTATGCGTCGTA):
	
		- Does not start with ATG (has_start = 0)

		- Does not end with TAA, "TAG", or "TGA" (has_stop = 0)

		- Does not contain ATAT (has_atat = 0)

		- Does not contain at least 3 consecutive 'G's (has_ggg = 0)

	
	

**Note:**

	- The result is ordered by sample_id in ascending order

	- For each pattern, 1 indicates the pattern is present and 0 indicates it is not present

---

## 💻 Implementation (python3)

```py
SELECT 
    sample_id,
    dna_sequence,
    species,
    -- Check if the sequence starts with 'ATG'
    CASE 
        WHEN dna_sequence LIKE 'ATG%' THEN 1 
        ELSE 0 
    END AS has_start,
    -- Check if the sequence ends with 'TAA', 'TAG', or 'TGA'
    CASE 
        WHEN dna_sequence REGEXP '(TAA|TAG|TGA)$' THEN 1 
        ELSE 0 
    END AS has_stop,
    -- Check if the motif 'ATAT' is present
    CASE 
        WHEN dna_sequence LIKE '%ATAT%' THEN 1 
        ELSE 0 
    END AS has_atat,
    -- Check for at least 3 consecutive 'G's
    CASE 
        WHEN dna_sequence LIKE '%GGG%' THEN 1 
        ELSE 0 
    END AS has_ggg
FROM 
    Samples
ORDER BY 
    sample_id ASC;
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The objective is to scan DNA sequences and flag the presence or absence of specific nucleotide motifs:
1. **Start Codon (`has_start`)**: Must start with `ATG`. A prefix check can be cleanly handled using `LIKE 'ATG%'`.
2. **Stop Codon (`has_stop`)**: Must end with `TAA`, `TAG`, or `TGA`. Using a regular expression `REGEXP '(TAA|TAG|TGA)$'` is both concise and expressive for alternating suffix conditions.
3. **Repeated Motif (`has_atat`)**: Must contain `ATAT` anywhere. A substring match `LIKE '%ATAT%'` is optimal.
4. **Triple Guanine (`has_ggg`)**: Must have at least three consecutive `G`s. Notice that any sequence containing three or more consecutive `G`s (e.g., `GGGG`) inherently contains `GGG` as a substring. Therefore, checking `LIKE '%GGG%'` accurately captures $\ge 3$ consecutive `G`s.

Using `CASE WHEN ... THEN 1 ELSE 0 END` guarantees standard SQL compatibility across various database engines, ensuring boolean evaluation outputs integer flags `1` or `0` deterministically.

---

### Step-by-Step Approach

1. **Projection**: Select `sample_id`, `dna_sequence`, and `species` directly from `Samples`.
2. **Pattern Matching**:
   - `has_start`: Evaluate `dna_sequence LIKE 'ATG%'`.
   - `has_stop`: Evaluate `dna_sequence REGEXP '(TAA|TAG|TGA)$'`.
   - `has_atat`: Evaluate `dna_sequence LIKE '%ATAT%'`.
   - `has_ggg`: Evaluate `dna_sequence LIKE '%GGG%'`.
3. **Ordering**: Apply `ORDER BY sample_id ASC` as required by the specification.

---

### Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N \times L)$, where $N$ is the number of rows in the `Samples` table and $L$ is the maximum length of a DNA sequence. String searches (`LIKE` and `REGEXP`) evaluate in linear time relative to sequence length. The sorting step takes $\mathcal{O}(N \log N)$, making the overall time complexity $\mathcal{O}(N \times L + N \log N)$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space (excluding the output buffer), as processing occurs row-by-row in a streaming fashion.

---

### Common Pitfalls / Mistakes Candidates Make

1. **Overcomplicating Consecutive Characters**: Over-engineering the $\ge 3$ check with complex regex like `G{3,}` or quantifiers, when a simple substring search `LIKE '%GGG%'` is faster and handles 3, 4, or more consecutive 'G's identically.
2. **Case Sensitivity**: In MySQL, `LIKE` and `REGEXP` can be case-insensitive depending on the collation (e.g., `utf8mb4_0900_ai_ci`). For strictly case-sensitive DNA sequences, casting to `BINARY` (e.g., `dna_sequence LIKE BINARY 'ATG%'`) or configuring binary collation prevents false positives if lower-case letters exist.
3. **NULL Handling**: Relying solely on raw boolean expressions (e.g., `dna_sequence LIKE 'ATG%'` directly) can result in `NULL` rather than `0` if `dna_sequence` is null. The `CASE WHEN ... THEN 1 ELSE 0 END` structure explicitly prevents `NULL` outputs.

---

### Real Interview Follow-Up Questions

1. **Scale & Indexing: How would you optimize this query on a table with 100M+ sequences?**
   - *Answer*: Wildcard searches like `%ATAT%` and `%GGG%` cannot leverage standard B-Tree indexes and require a full table scan. To scale:
     - Generate precomputed boolean flag columns or a bitmask using generated columns (e.g., `STORED` virtual columns) and index them.
     - For arbitrary k-mer / motif searches at scale, use specialized biological sequence indexing (such as FM-index / Burrows-Wheeler Transform or k-mer hash indexes), or full-text/trigram indexes (e.g., `pg_trgm` in PostgreSQL).
2. **Genomic Considerations: What if sequences are millions of base pairs long (e.g., whole chromosomes)?**
   - *Answer*: Relational databases are not designed to store megabase/gigabase strings in single rows. Sequences are typically chunked into fixed-size overlapping windows (e.g., FASTA/FASTQ records), or processed via distributed streaming pipelines (e.g., Apache Spark with BioJava/BioPython) using algorithms like Aho-Corasick to locate all patterns simultaneously in a single linear pass.
