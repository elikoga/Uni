----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06/08/2022 04:13:34 PM
-- Design Name: 
-- Module Name: state_machine - Behavioral
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
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

ENTITY state_machine IS
    PORT (
        clk100mhz : IN STD_LOGIC;
        start : IN STD_LOGIC;
        stop : IN STD_LOGIC;
        pause : IN STD_LOGIC;
        en : OUT STD_LOGIC;
        rst : OUT STD_LOGIC);
END state_machine;

ARCHITECTURE Behavioral OF state_machine IS

BEGIN

    RUN_STATE : PROCESS (clk100mhz, start, stop, pause)
        VARIABLE state : STD_LOGIC_VECTOR(2 DOWNTO 0) := "100"; -- 100 is stop, 010 is run, 001 is pause
    BEGIN
        IF rising_edge(clk100mhz) THEN
            IF state = "100" THEN
                IF start = '1' THEN
                    state := "010";
                ELSIF pause = '1' THEN
                    state := "001";
                END IF;
            ELSIF state = "010" THEN
                IF stop = '1' THEN
                    state := "100";
                ELSIF pause = '1' THEN
                    state := "001";
                END IF;
            ELSIF state = "001" THEN
                IF stop = '1' THEN
                    state := "100";
                ELSIF start = '1' THEN
                    state := "010";
                END IF;
            END IF;
            IF state = "100" THEN
                rst <= '1';
                en <= '0';
            ELSIF state = "010" THEN
                rst <= '0';
                en <= '1';
            ELSIF state = "001" THEN
                rst <= '0';
                en <= '0';
            END IF;
        END IF;
    END PROCESS;

END Behavioral;