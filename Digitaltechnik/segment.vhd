ENTITY segment IS
    PORT (
        value : IN STD_LOGIC_VECTOR(3 DOWNTO 0); -- Value ist 4-Bit breit und kann die Zahlen 0-15 kodieren
        leds_n : OUT STD_LOGIC_VECTOR(6 DOWNTO 0) -- Jedes Bit des Vektors ist einem Segment 'CA'-'CG' zugeordnet
    );
END segment;

ARCHITECTURE behavioral OF segment IS
BEGIN
    -- Zahl (Dez.) Zahl (Bin.) CA CB CC CD CE CF CG
    -- 0 0000 0 0 0 0 0 0 1
    -- 1 0001 1 0 0 1 1 1 1
    -- 2 0010 0 0 1 0 0 1 0
    -- 3 0011 0 0 0 0 1 1 0
    -- 4 0100 1 0 0 1 1 0 0
    -- 5 0101 0 1 0 0 1 0 0
    -- 6 0110 0 1 0 0 0 0 0
    -- 7 0111 0 0 0 1 1 1 1
    -- 8 1000 0 0 0 0 0 0 0
    -- 9 1001 0 0 0 0 1 0 0
    -- >9 else 1 1 1 1 1 1 0
    leds_n <=
        "0000001" WHEN value = "0000" ELSE -- 0
        "1001111" WHEN value = "0001" ELSE -- 1
        "0010010" WHEN value = "0010" ELSE -- 2
        "0000110" WHEN value = "0011" ELSE -- 3
        "1001100" WHEN value = "0100" ELSE -- 4
        "0100100" WHEN value = "0101" ELSE -- 5
        "0100000" WHEN value = "0110" ELSE -- 6
        "0001111" WHEN value = "0111" ELSE -- 7
        "0000000" WHEN value = "1000" ELSE -- 8
        "0000100" WHEN value = "1001" ELSE -- 9
        "1111110"; -- >9
END behavioral;