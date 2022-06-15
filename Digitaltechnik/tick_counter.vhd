----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06/08/2022 02:50:07 PM
-- Design Name: 
-- Module Name: tick_counter - Behavioral
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

ENTITY tick_counter IS
    PORT (
        tick : IN STD_LOGIC;
        an_cnt : OUT STD_LOGIC_VECTOR (1 DOWNTO 0));
END tick_counter;

ARCHITECTURE Behavioral OF tick_counter IS

BEGIN
    -- on rising edge, increment counter
    COUNT : PROCESS (tick)
        VARIABLE cnt : INTEGER RANGE 0 TO 3 := 0;
    BEGIN
        IF rising_edge(tick) THEN
            cnt := cnt + 1;
        END IF;
        an_cnt <= STD_LOGIC_VECTOR(to_unsigned(cnt, 2));
    END PROCESS;
END Behavioral;