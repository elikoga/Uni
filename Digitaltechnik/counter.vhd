----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06/08/2022 04:12:40 PM
-- Design Name: 
-- Module Name: counter - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
USE IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

ENTITY counter IS
    PORT (
        tick_in : IN STD_LOGIC;
        rst : IN STD_LOGIC;
        max_count : IN STD_LOGIC_VECTOR (3 DOWNTO 0);
        digit_out : OUT STD_LOGIC_VECTOR (3 DOWNTO 0);
        tick_out : OUT STD_LOGIC);
END counter;

ARCHITECTURE Behavioral OF counter IS

BEGIN

    ADD_COUNTER : PROCESS (tick_in, rst, max_count)
        VARIABLE count : INTEGER RANGE 0 TO 9;

    BEGIN
        IF (rst = '1') THEN
            count := 0;
            digit_out <= STD_LOGIC_VECTOR(to_unsigned(count, 4));
        ELSE
            IF rising_edge(tick_in) THEN
                IF count = to_integer(unsigned(max_count)) THEN
                    tick_out <= '1';
                    count := 0;
                ELSE
                    tick_out <= '0';
                    count := count + 1;
                END IF;
                digit_out <= STD_LOGIC_VECTOR(to_unsigned(count, 4));
            END IF;
        END IF;
    END PROCESS;
END Behavioral;