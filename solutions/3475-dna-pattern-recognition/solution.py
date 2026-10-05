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
