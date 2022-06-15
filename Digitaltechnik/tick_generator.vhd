----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06/08/2022 02:50:07 PM
-- Design Name: 
-- Module Name: tick_generator - Behavioral
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

ENTITY tick_generator IS
    PORT (
        clk100mhz : IN STD_LOGIC;
        tick : OUT STD_LOGIC;
        divider : IN STD_LOGIC_VECTOR(31 DOWNTO 0);
        en : IN STD_LOGIC);
END tick_generator;

ARCHITECTURE Behavioral OF tick_generator IS

BEGIN
    -- this is a divider
    ADD_VAR : PROCESS (clk100mhz)
        VARIABLE counter : INTEGER := 1;
    BEGIN
        IF rising_edge(clk100mhz) AND en = '1' THEN
            IF counter = 1 THEN
                tick <= '1';
            ELSE
                tick <= '0';
            END IF;
            -- divider :=
            --     0 WHEN divider = 100000
            --     ELSE
            --     divider + 1;
            -- VHDL 2008 feature cannot be used
            IF counter = to_integer(unsigned(divider)) THEN
                counter := 1;
            ELSE
                counter := counter + 1;
            END IF;
        END IF;
    END PROCESS;

END Behavioral;